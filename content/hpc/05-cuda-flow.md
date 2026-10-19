# 5. CUDA 프로그램의 기본 흐름

## CUDA 프로그램의 실행 3단계

{: .시험 }
> **이 3단계가 모든 CUDA 프로그램의 뼈대다.** 순서를 그대로 외울 것.
>
> 1. **메모리 복사 (host → device)** — `cudaMemcpy()`
> 2. **GPU 연산** — 각 CUDA 스레드에서 커널을 **비동기적으로** 실행
> 3. **메모리 복사 (device → host)** — `cudaMemcpy()`

### 1단계: 메모리 복사 (host → device)

호스트 메모리에 있는, GPU에서 처리해야 할 데이터를 **디바이스 메모리로 복사**. 데이터는 **PCI bus**를 통해 이동한다.

### 2단계: GPU 연산

호스트에서 커널 호출을 하면 디바이스에서 **CUDA core들과 디바이스 메모리의 데이터**를 사용하여 각 CUDA 스레드가 커널을 실행.

{: .중요 }
> **커널은 비동기적으로 수행된다.**
> 호스트는 디바이스에게 커널 수행을 요청한 뒤 **완료될 때까지 기다리지 않고 다음 라인의 코드를 수행**한다.
> → 그래서 `cudaDeviceSynchronize()` 가 필요하다.

### 3단계: 메모리 복사 (device → host)

디바이스 메모리에 있는 GPU 연산 결과를 **호스트 메모리로 복사**.

{: .참고 }
> **커널은 비동기, `cudaMemcpy()`는 동기**다.
> 즉 `cudaMemcpy()`는 호스트가 메모리 복사가 완료될 때까지 기다린다.

---

## CUDA 기초 메모리 API 목록

| 함수 | 설명 |
|---|---|
| **`cudaMalloc()`** | 디바이스 메모리 **할당** |
| **`cudaFree()`** | 디바이스 메모리 **해제** |
| **`cudaMemset()`** | 디바이스 메모리 **초기화** |
| **`cudaMemcpy()`** | 호스트와 디바이스 사이의 **메모리 복사** |
| **`cudaMemGetInfo()`** | 디바이스 메모리의 **총 크기 및 사용 가능한 크기** 확인 |
| **`cudaGetErrorName()`** | **에러 코드(정수)를 문자열로 변환** |

{: .중요 }
> 모든 CUDA API는 **성공 시 `cudaSuccess` (0)** 을 반환하고, **실패 시 0 이외의 에러 코드**를 반환한다. 반환형은 **`cudaError_t` 열거형**이다.

---

## cudaMalloc()

```c
cudaError_t cudaMalloc(void **ptr, size_t size)
```

GPU에 **디바이스 메모리(global memory) 할당**

| 인자 | 설명 |
|---|---|
| `ptr` | 할당할 디바이스 메모리 공간의 **시작 주소의 포인터** |
| `size` | 할당할 메모리 공간의 크기 (**byte 단위**) |

```c
int *dDataPtr;
cudaMalloc(&dDataPtr, sizeof(int) * 32);     // 4 * 32 byte 할당
```

{: .주의 }
> 첫 번째 인자가 **포인터의 포인터(`void **`)** 이므로 **`&dDataPtr`** 처럼 **주소를 넘겨야** 한다.

---

## cudaFree()

```c
cudaError_t cudaFree(void *ptr)
```

디바이스 메모리 **해제**. 인자는 **해제할 메모리 공간의 시작 주소**.

```c
cudaFree(dDataPtr);
```

---

## cudaMemset()

```c
cudaError_t cudaMemset(void *ptr, int value, size_t size)
```

디바이스 메모리 **초기화**

| 인자 | 설명 |
|---|---|
| `ptr` | 초기화할 메모리 공간의 **시작 주소** |
| `value` | **초기화할 값** |
| `size` | 초기화할 메모리 공간의 크기 (byte 단위) |

```c
int *dDataPtr;
cudaMalloc(&dDataPtr, sizeof(int) * 32);     // 할당
cudaMemset(dDataPtr, 0, sizeof(int) * 32);   // 0으로 초기화
cudaFree(dDataPtr);                          // 해제
```

---

## cudaMemGetInfo() / cudaGetErrorName()

```c
cudaError_t cudaMemGetInfo(size_t *free, size_t *total);
const char* cudaGetErrorName(cudaError_t error);
```

| 인자 | 설명 |
|---|---|
| `free` | 디바이스 메모리의 **현재 사용 가능한 크기**를 저장할 변수의 주소 |
| `total` | 디바이스 메모리의 **총 크기**를 저장할 변수의 주소 |

### 코드 (lec03_03.cu)

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

void checkDeviceMemory(void)
{
    size_t free, total;
    cudaMemGetInfo(&free, &total);
    printf("Device memory (free/total) = %ld/%ld bytes\n", free, total);
}

int main(void)
{
    int *dDataPtr;
    cudaError_t errorCode;

    checkDeviceMemory();

    errorCode = cudaMalloc(&dDataPtr, sizeof(int) * 1024 * 1024);   // 4MB 할당
    printf("cudaMalloc - %s\n", cudaGetErrorName(errorCode));
    checkDeviceMemory();

    errorCode = cudaMemset(dDataPtr, 0, sizeof(int) * 1024 * 1024); // 초기화
    printf("cudaMemset - %s\n", cudaGetErrorName(errorCode));

    errorCode = cudaFree(dDataPtr);                                 // 해제
    printf("cudaFree - %s\n", cudaGetErrorName(errorCode));
    checkDeviceMemory();
}
```

```
Device memory (free/total) = 7444889600/8589410304 bytes
cudaMalloc - cudaSuccess
Device memory (free/total) = 7440695296/8589410304 bytes
cudaMemset - cudaSuccess
cudaFree - cudaSuccess
Device memory (free/total) = 7444889600/8589410304 bytes
```

{: .참고 }
> **free 크기와 total 크기가 같지 않은 이유**: GPU는 **화면 렌더링 등 다른 작업에도 사용**되기 때문.

---

## cudaMemcpy()

```c
cudaError_t cudaMemcpy(void *dst, const void *src, size_t size,
                       enum cudaMemcpyKind kind);
```

| 인자 | 설명 |
|---|---|
| `dst` | **복사될** 데이터(destination)의 시작 주소 |
| `src` | **복사할 원본** 데이터(source)의 시작 주소 |
| `size` | 복사할 원본 데이터의 크기 (byte 단위) |
| `kind` | **데이터 복사 방향** (`cudaMemcpyKind` 열거형) |

{: .시험 }
> **`cudaMemcpyKind` 열거형 — 인자 순서가 `dst, src` 임에 주의**
>
> | 열거형 | 복사 방향 |
> |---|---|
> | `cudaMemcpyHostToHost` | 호스트 → 호스트 |
> | **`cudaMemcpyHostToDevice`** | **호스트 → 디바이스** |
> | **`cudaMemcpyDeviceToHost`** | **디바이스 → 호스트** |
> | `cudaMemcpyDeviceToDevice` | 디바이스 → 디바이스 |
> | `cudaMemcpyDefault` | **통합 메모리(unified memory)** 를 지원하는 경우(CUDA 6.0 이상), 주소값을 통해 **런타임이 자동으로 복사 방향을 판단**. 단, **명시적으로 복사 방향을 설정하는 것을 권장** |

{: .참고 }
> **통합 메모리(unified memory)**: 호스트 메모리와 디바이스 메모리를 **하나의 논리적 주소 공간**으로 표현하는 기술

### 코드 (lec03_04.cu)

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

__global__ void printData(int *_dDataPtr)       // printData 커널
{
    printf("%d", _dDataPtr[threadIdx.x]);       // threadIdx.x: 블록 내 스레드 번호
}

__global__ void setData(int *_dDataPtr)         // setData 커널
{
    _dDataPtr[threadIdx.x] = 2;
}

int main(void)
{
    int data[10] = {0};                         // 호스트 메모리에 배열 할당
    for (int i = 0; i < 10; i++)
        data[i] = 1;                            // 1로 초기화

    int *dDataPtr;
    cudaMalloc(&dDataPtr, sizeof(int) * 10);    // 디바이스 메모리 할당
    cudaMemset(dDataPtr, 0, sizeof(int) * 10);  // 0으로 초기화

    printf("Data in device: ");
    printData <<<1, 10>>> (dDataPtr);

    // 호스트 -> 디바이스
    cudaMemcpy(dDataPtr, data, sizeof(int) * 10, cudaMemcpyHostToDevice);
    printf("\nHost -> Device: ");
    printData <<<1, 10>>> (dDataPtr);

    setData <<<1, 10>>> (dDataPtr);             // 값을 2로 변경

    // 디바이스 -> 호스트
    cudaMemcpy(data, dDataPtr, sizeof(int) * 10, cudaMemcpyDeviceToHost);
    printf("\nDevice -> Host: ");
    for (int i = 0; i < 10; i++)
        printf("%d", data[i]);
    printf("\n");

    cudaFree(dDataPtr);
}
```

```
Data in device: 0000000000
Host -> Device: 1111111111
Device -> Host: 2222222222
```

---

## CUDA 기반 벡터합 프로그램

### 벡터합

```
벡터 a = [a1, a2, ..., an]
벡터 b = [b1, b2, ..., bn]
벡터 c = a + b = [a1+b1, a2+b2, ..., an+bn]
```

### CPU만 사용한 벡터합 (lec03_05.cu)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_DATA 1024

int main(void)
{
    int *a, *b, *c;
    int memsize = sizeof(int) * NUM_DATA;

    // 호스트 메모리 할당
    a = (int *)malloc(memsize);
    b = (int *)malloc(memsize);
    c = (int *)malloc(memsize);

    // 호스트 메모리 초기화
    memset(a, 0, memsize);
    memset(b, 0, memsize);
    memset(c, 0, memsize);

    for (int i = 0; i < NUM_DATA; i++) {
        a[i] = rand() % 10;
        b[i] = rand() % 10;
    }

    for (int i = 0; i < NUM_DATA; i++)    // CPU 연산
        c[i] = a[i] + b[i];

    free(a); free(b); free(c);
    return 0;
}
```

---

### GPU를 이용한 벡터합 (lec03_06.cu)

{: .시험 }
> **실기에서 가장 중요한 코드.** 할당 → 초기화 → 복사 → 커널 → 동기화 → 복사 → 해제 순서를 그대로 쓸 수 있어야 한다.

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_DATA 1024

__global__ void vecAdd(int *_a, int *_b, int *_c)
{
    int tID = threadIdx.x;              // 블록 내 각 CUDA 스레드의 번호
    _c[tID] = _a[tID] + _b[tID];
}

int main(void)
{
    int *a, *b, *c, *hc;                // 호스트 메모리
    int *da, *db, *dc;                  // 디바이스 메모리
    int memsize = sizeof(int) * NUM_DATA;
    int result;

    // 1. 호스트 메모리 할당
    a  = (int *)malloc(memsize);
    b  = (int *)malloc(memsize);
    c  = (int *)malloc(memsize);
    hc = (int *)malloc(memsize);

    // 2. 호스트 메모리 초기화
    memset(a, 0, memsize);
    memset(b, 0, memsize);
    memset(c, 0, memsize);
    memset(hc, 0, memsize);

    for (int i = 0; i < NUM_DATA; i++) {
        a[i] = rand() % 10;
        b[i] = rand() % 10;
    }

    // 3. 호스트에서 벡터합 계산 (비교용 CPU 연산)
    for (int i = 0; i < NUM_DATA; i++)
        hc[i] = a[i] + b[i];

    // 4. 디바이스 메모리 할당
    cudaMalloc(&da, memsize);
    cudaMalloc(&db, memsize);
    cudaMalloc(&dc, memsize);

    // 5. 디바이스 메모리 초기화
    cudaMemset(da, 0, memsize);
    cudaMemset(db, 0, memsize);
    cudaMemset(dc, 0, memsize);

    // 6. 메모리 복사 (host -> device)
    cudaMemcpy(da, a, memsize, cudaMemcpyHostToDevice);
    cudaMemcpy(db, b, memsize, cudaMemcpyHostToDevice);

    // 7. GPU 연산 (커널은 비동기적 수행)
    vecAdd <<<1, NUM_DATA>>> (da, db, dc);
    cudaDeviceSynchronize();            // 커널 수행 완료까지 대기

    // 8. 메모리 복사 (device -> host)
    cudaMemcpy(c, dc, memsize, cudaMemcpyDeviceToHost);

    // 9. 디바이스 메모리 해제
    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);

    // 10. CPU와 GPU 결과 비교
    result = memcmp(c, hc, memsize);
    if (result == 0)
        printf("The vector sum on the device (GPU) is the same as the host (CPU)\n");
    else
        printf("The vector sum on the device (GPU) is not the same as the host (CPU)\n");

    // 11. 호스트 메모리 해제
    free(a); free(b); free(c); free(hc);
    return 0;
}
```

{: .중요 }
> **`memcmp(c, hc, memsize)`** 로 GPU 결과(`c`)와 CPU 결과(`hc`)를 비교한다. **같으면 0을 반환**한다.

---

## 연산 시간 측정 및 성능 분석

### 시간 측정 방법

```c
#include <time.h>

clock_t start, end;

start = clock();
// ... 측정할 구간 ...
end = clock();

printf("%f ms\n", (double)(end - start) * 1000.0 / CLOCKS_PER_SEC);
```

{: .중요 }
> **GPU 연산 시간을 측정할 때는 반드시 `cudaDeviceSynchronize()` 를 `end = clock()` 앞에 넣어야 한다.**
> 커널이 비동기적으로 수행되므로, 동기화 함수가 없으면 **커널 수행 시간이 정상적으로 측정되지 않는다.**
>
> ```c
> start = clock();
> vecAdd <<<1, NUM_DATA>>> (da, db, dc);
> cudaDeviceSynchronize();      // 이것이 없으면 측정값이 엉뚱해짐
> end = clock();
> ```

### 측정 구간 4개

1. CPU 연산
2. 메모리 복사 (host → device)
3. GPU 연산 (커널 실행)
4. 메모리 복사 (device → host)

**CUDA Total = 메모리 복사 시간 + GPU 연산 시간**

---

### 실행 결과 비교 (lec03_07.cu)

{: .시험 }
> **데이터 크기에 따라 결론이 뒤집힌다.** 이 비교가 핵심.

**NUM_DATA = 1024 인 경우**

```
Computation on host (CPU):     0.003000 ms
Memory copy: host -> device:   0.017000 ms
Computation on device (GPU):   0.223000 ms
Memory copy: device -> host:   0.012000 ms
CUDA Total:                    0.259000 ms
→ GPU 연산 결과와 CPU 연산 결과가 같음
```

- **GPU 연산 시간이 CPU 연산 시간보다 많이 소요됨** (데이터가 적으면 GPU가 오히려 느림)
- 메모리 복사 시간이 많이 소요됨

**NUM_DATA = 1048576 (1024×1024) 인 경우**

```
Computation on host (CPU):     3.054000 ms
Memory copy: host -> device:   0.866000 ms
Computation on device (GPU):   0.217000 ms
Memory copy: device -> host:   0.566000 ms
CUDA Total:                    1.657000 ms
→ GPU 연산 결과와 CPU 연산 결과가 다름
```

- **GPU 연산 시간이 CPU 연산 시간보다 적게 소요됨** (데이터가 많아지면 GPU가 유리)
- 그런데 **결과가 틀렸다!**

{: .주의 }
> **왜 결과가 달라졌는가?**
>
> `vecAdd <<<1, NUM_DATA>>>` 는 **블록 1개에 NUM_DATA개의 스레드**를 요청한다.
> 그런데 **한 블록 내의 최대 스레드 수는 1024개**다.
> → NUM_DATA가 1024를 넘으면 **스레드가 부족해서 일부 데이터가 계산되지 않는다.**
>
> 해결하려면 **스레드 계층 구조와 인덱싱**을 알아야 한다.
> → [6. CUDA 스레드 계층](06-cuda-thread-hierarchy.html), [7. 스레드 레이아웃과 인덱싱](07-cuda-thread-indexing.html)

{: .참고 }
> 메모리 복사 시간 때문에 **CUDA Total은 GPU 연산 시간보다 훨씬 크다.**
> 즉 **데이터가 충분히 크지 않으면 GPU를 써도 전체적으로는 이득이 없다**는 것이 이 실습의 결론이다.
