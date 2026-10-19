# 7. CUDA 스레드 레이아웃과 인덱싱

{: .참고 }
> 이 강의는 **9주차(기말 범위)** 내용이지만, [5강의 "데이터가 1024개를 넘으면 결과가 틀리는 문제"](05-cuda-flow.html)를 해결하는 부분이라 이어서 정리한다.

## 스레드 인덱싱 (thread indexing)

**스레드 인덱싱**: 스레드를 식별하기 위해 제공하는 **인덱스 체계 전체**

| 구분 | 설명 | 변수 |
|---|---|---|
| **`gridDim`** | grid 내의 각 차원의 **block 수** | `.x` `.y` `.z` |
| **`blockIdx`** | grid 내의 각 차원의 **block 인덱스** | `.x` `.y` `.z` |
| **`blockDim`** | block 내의 각 차원의 **thread 수** | `.x` `.y` `.z` |
| **`threadIdx`** | block 내의 각 차원의 **thread 인덱스** | `.x` `.y` `.z` |

### 메모리 상의 배열

{: .중요 }
> **메모리에는 차원 개념이 없으며, 데이터(배열)는 연속된 메모리 공간에 저장된다.**
>
> 그래서 2차원 배열도 실제로는 1차원이고, 인덱스는 다음과 같이 계산한다.
>
> ```
> index = row * COL_SIZE + col
>       = (내 앞의 행 수) × (한 행의 길이) + (내 행에서 몇 번째)
> ```
>
> 이 식이 이후 모든 2차원 배열 예제에 등장한다.

---

## 스레드의 전역 번호 (global ID)

**전역 번호**: thread indexing을 이용하여 **그리드 내의 각 스레드에게 부여되는 고유한 번호**

스레드 레이아웃(배치)과 처리하려는 데이터가 **1:1로 매칭되는 경우** 사용한다.

### 블록 내의 전역 번호

{: .시험 }
> **차원이 올라갈수록 이전 차원 공식을 그대로 재사용**하는 구조다.
>
> **1차원 블록** — x 번호가 곧 전역 번호
>
> ```
> BLOCK_1D_TID = threadIdx.x
>              = 내가 x축에서 몇 번째인가
> ```
>
> **2차원 블록** — 내 앞의 행들을 통째로 세고, 내 행에서의 위치를 더한다
>
> ```
> BLOCK_2D_TID = threadIdx.y * blockDim.x + threadIdx.x
>              = (내 앞의 행 수) × (한 행의 스레드 수) + (내 행에서 몇 번째)
> ```
>
> **3차원 블록** — 내 앞의 층들을 통째로 세고, 2차원 공식을 더한다
>
> ```
> BLOCK_3D_TID = threadIdx.z * (blockDim.y * blockDim.x) + BLOCK_2D_TID
>              = (내 앞의 층 수) × (한 층의 스레드 수) + (내 층 안에서의 번호)
> ```

### 그리드 내의 전역 번호

한 블록 내의 스레드 수:

```
NUM_THREAD_IN_BLOCK = blockDim.x * blockDim.y * blockDim.z     (1024 이하)
                    = 블록 하나에 들어 있는 스레드의 총 개수
```

{: .시험 }
> 블록 공식과 **완전히 같은 모양**이고, "스레드" 자리에 "블록"이 들어갈 뿐이다.
>
> **1차원 그리드** — 내 앞의 블록들을 통째로 세고, 내 블록 안에서의 번호를 더한다
>
> ```
> GRID_1D_TID = blockIdx.x * NUM_THREAD_IN_BLOCK + BLOCK_3D_TID
>             = (내 앞의 블록 수) × (블록 1개의 스레드 수) + (내 블록 안에서의 번호)
> ```
>
> **2차원 그리드** — 내 앞의 "블록 행"들을 통째로 세고, 1차원 공식을 더한다
>
> ```
> GRID_2D_TID = blockIdx.y * (gridDim.x * NUM_THREAD_IN_BLOCK) + GRID_1D_TID
>             = (내 앞의 블록 행 수) × (블록 한 행의 스레드 수) + (내 블록 행 안에서의 번호)
> ```
>
> **3차원 그리드** — 내 앞의 "블록 층"들을 통째로 세고, 2차원 공식을 더한다
>
> ```
> GRID_3D_TID = blockIdx.z * (gridDim.y * gridDim.x * NUM_THREAD_IN_BLOCK) + GRID_2D_TID
>             = (내 앞의 블록 층 수) × (블록 한 층의 스레드 수) + (내 블록 층 안에서의 번호)
> ```

{: .중요 }
> **여섯 공식이 전부 같은 모양이다.** 외울 건 공식 여섯 개가 아니라 이 문장 하나.
>
> ```
> 전역 번호 = (내 앞에 있는 덩어리 수) × (덩어리 1개의 크기) + (그 덩어리 안에서의 번호)
> ```
>
> | 항 | 의미 | 무엇이 들어가나 |
> |---|---|---|
> | **1항** | 내 앞에 있는 덩어리 수 | **상위 차원의 인덱스** (`threadIdx.y`, `blockIdx.x` …) |
> | **2항** | 덩어리 1개의 크기 | **그 아래 차원들의 총 개수** (`blockDim.x`, `gridDim.x * NUM_THREAD_IN_BLOCK` …) |
> | **3항** | 그 덩어리 안에서의 번호 | **한 단계 아래 차원의 공식** |
>
> 차원이 하나 올라갈 때마다 **"앞선 덩어리를 통째로 세는 항"이 앞에 하나씩 붙을** 뿐이다.

---

## 공통 헤더 파일 (lec05_01.cuh)

전역 번호 계산은 자주 쓰이므로 매크로로 헤더에 정의해 둔다.

```c
// grid dimension
#define GDIM_X gridDim.x
#define GDIM_Y gridDim.y
#define GDIM_Z gridDim.z

// block index
#define BID_X blockIdx.x
#define BID_Y blockIdx.y
#define BID_Z blockIdx.z

// block dimension
#define BDIM_X blockDim.x
#define BDIM_Y blockDim.y
#define BDIM_Z blockDim.z

// thread index
#define TID_X threadIdx.x
#define TID_Y threadIdx.y
#define TID_Z threadIdx.z

// the number of threads in a block
#define NUM_THREAD_IN_BLOCK BDIM_X * BDIM_Y * BDIM_Z

// thread global id in block
#define BLOCK_2D_TID TID_Y * BDIM_X + TID_X
#define BLOCK_3D_TID TID_Z * (BDIM_Y * BDIM_X) + BLOCK_2D_TID

// thread global id in grid
#define GRID_1D_TID BID_X * NUM_THREAD_IN_BLOCK + BLOCK_3D_TID
#define GRID_2D_TID BID_Y * (GDIM_X * NUM_THREAD_IN_BLOCK) + GRID_1D_TID
#define GRID_3D_TID BID_Z * (GDIM_Y * GDIM_X * NUM_THREAD_IN_BLOCK) + GRID_2D_TID
```

---

## 1차원 배열 — 1차원 그리드 + 1차원 블록

{: .중요 }
> **가장 많이 쓰이는 인덱싱 공식.** 이것만큼은 반드시 외울 것.
>
> ```c
> index = (blockIdx.x * blockDim.x) + threadIdx.x;
> //    = (내 앞의 블록 수) × (블록당 스레드 수) + (내 블록에서 몇 번째)
> ```
>
> 위의 `GRID_1D_TID` 를 **1차원 블록(`blockDim.y = blockDim.z = 1`)** 에 대해 풀어 쓴 것과 같다.

### 5강의 문제 해결 (lec05_02.cu)

5강에서 `vecAdd <<<1, NUM_DATA>>>` 로는 **블록당 최대 스레드 수 1024**를 넘길 수 없어 결과가 틀렸다. 이를 **블록을 여러 개 사용**하도록 고친다.

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define NUM_DATA 134217728              // 1024 * 1024 * 128

__global__ void vecAdd(int *da, int *db, int *dc)
{
    // 1차원 그리드 내의 스레드 전역 번호 (GRID_1D_TID)
    int index = (blockIdx.x * blockDim.x) + threadIdx.x;

    if (index < NUM_DATA)               // 범위 검사 필수
        dc[index] = da[index] + db[index];
}
```

커널 호출 부분:

```c
// 한 그리드 내의 블록 수: NUM_DATA/256 을 올림 처리한 수
dim3 dimGrid(ceil((float)NUM_DATA / (float)256), 1, 1);
dim3 dimBlock(256, 1, 1);               // 한 블록 내의 스레드 수: 256

vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
cudaDeviceSynchronize();
```

{: .시험 }
> **왜 `ceil()` 이 필요한가?**
>
> `NUM_DATA / 256` 이 나누어떨어지지 않으면 **마지막 데이터들이 처리되지 않는다.**
> 올림 처리하면 블록이 하나 더 생기지만, 그만큼 **남는 스레드가 배열 범위를 벗어나므로** 커널 안에서 **`if (index < NUM_DATA)` 범위 검사가 반드시 필요**하다.
>
> **`ceil()` 과 `if` 범위 검사는 항상 세트**다.

### 실행 결과 (NUM_DATA = 134,217,728)

```
Computation on host (CPU):     392.813000 ms
Memory copy: host -> device:   108.794000 ms
Computation on device (GPU):     4.253000 ms
Memory copy: device -> host:    59.988000 ms
CUDA Total:                    173.049000 ms
```

- **GPU 연산 결과와 CPU 연산 결과가 같음**
- **GPU 연산 시간은 CPU 연산 시간보다 약 92배 적게 소요**
- **CUDA Total은 메모리 복사 시간 때문에 CPU 연산 시간보다 2.26배 적게 소요**

{: .중요 }
> **GPU 연산 자체는 92배 빠른데 전체로는 2.26배밖에 못 줄었다.**
> 그 차이가 전부 **메모리 복사(host와 device 사이) 비용**이다. CUDA 성능 분석의 핵심 포인트.

---

## 1차원 배열 — 2차원 그리드 + 2차원 블록

**스레드 indexing**

```c
index = GRID_2D_TID;
// = blockIdx.y * (gridDim.x * NUM_THREAD_IN_BLOCK) + GRID_1D_TID
```

### 코드 (lec05_06.cu)

```c
#include "lec05_01.cuh"                 // 매크로 헤더

#define ROW_SIZE (8192)
#define COL_SIZE (8192)
#define MAT_SIZE (ROW_SIZE * COL_SIZE)

__global__ void vecAdd(float *da, float *db, float *dc)
{
    unsigned int index = GRID_2D_TID;   // 매크로 사용

    if (index < MAT_SIZE)
        dc[index] = da[index] + db[index];
}
```

커널 호출:

```c
dim3 dimBlock(32, 32, 1);               // dim3 dimBlock(32, 32); 와 동일
dim3 dimGrid(ceil((float)COL_SIZE / (float)dimBlock.x),
             ceil((float)ROW_SIZE / (float)dimBlock.y), 1);

vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
```

결과: GPU 연산 시간이 CPU보다 **약 104배** 적게 소요, CUDA Total은 **2.7배** 적게 소요.

---

## 2차원 배열에 대한 인덱싱 — 3가지 조합

{: .시험 }
> **가장 출제 가능성이 높은 표.** 그리드·블록 차원 조합에 따라 `col`과 `row` 계산식이 어떻게 바뀌는지가 핵심이다.
>
> | 조합 | `col` | `row` |
> |---|---|---|
> | **1차원 그리드 + 1차원 블록** | `(blockIdx.x * blockDim.x) + threadIdx.x` | 커널 안에서 **for 루프로 순회** |
> | **2차원 그리드 + 1차원 블록** | `(blockIdx.x * blockDim.x) + threadIdx.x` | **`blockIdx.y`** |
> | **2차원 그리드 + 2차원 블록** | `(blockIdx.x * blockDim.x) + threadIdx.x` | **`(blockIdx.y * blockDim.y) + threadIdx.y`** |
>
> **`col` 계산식은 세 경우 모두 동일**하고, **`row`를 무엇으로 구하느냐만 달라진다.**

공통으로 사용하는 배열 인덱스:

```c
index = row * COL_SIZE + col;
```

---

### (1) 1차원 그리드 + 1차원 블록 (lec05_03.cu)

**한 스레드가 하나의 열(column) 전체를 처리**한다.

```c
__global__ void vecAdd(float *da, float *db, float *dc)
{
    unsigned int col = (blockIdx.x * blockDim.x) + threadIdx.x;

    if (col < COL_SIZE) {
        for (int row = 0; row < ROW_SIZE; row++) {   // row는 for 루프로 순회
            int index = row * COL_SIZE + col;
            dc[index] = da[index] + db[index];
        }
    }
}
```

커널 호출:

```c
dim3 dimBlock(32, 1, 1);
dim3 dimGrid(ceil((float)COL_SIZE / (float)dimBlock.x), 1, 1);
vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
```

결과: GPU가 CPU보다 **약 65배** 빠름 (세 방식 중 **가장 느림** — 한 스레드가 루프를 돌기 때문)

---

### (2) 2차원 그리드 + 1차원 블록 (lec05_04.cu)

**`row`를 `blockIdx.y`로 대체**하여 for 루프를 없앤다.

```c
__global__ void vecAdd(float *da, float *db, float *dc)
{
    unsigned int col = (blockIdx.x * blockDim.x) + threadIdx.x;
    unsigned int row = blockIdx.y;
    unsigned int index = row * COL_SIZE + col;

    if ((row < ROW_SIZE) && (col < COL_SIZE))
        dc[index] = da[index] + db[index];
}
```

커널 호출:

```c
dim3 dimBlock(32, 1, 1);
dim3 dimGrid(ceil((float)COL_SIZE / (float)dimBlock.x), ROW_SIZE, 1);
vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
```

{: .중요 }
> 그리드의 **y 차원 크기는 `ROW_SIZE` 를 그대로** 준다 (`ceil` 불필요).
> **블록 하나가 한 행(row)을 담당**하기 때문이다.

결과: GPU가 CPU보다 **약 94배** 빠름

---

### (3) 2차원 그리드 + 2차원 블록 (lec05_05.cu)

**`row`도 `col`과 같은 방식**으로 계산한다.

```c
__global__ void vecAdd(float *da, float *db, float *dc)
{
    unsigned int col = (blockIdx.x * blockDim.x) + threadIdx.x;
    unsigned int row = (blockIdx.y * blockDim.y) + threadIdx.y;
    unsigned int index = row * COL_SIZE + col;

    if ((row < ROW_SIZE) && (col < COL_SIZE))
        dc[index] = da[index] + db[index];
}
```

커널 호출:

```c
dim3 dimBlock(32, 32, 1);               // dim3 dimBlock(32, 32); 와 동일
dim3 dimGrid(ceil((float)COL_SIZE / (float)dimBlock.x),
             ceil((float)ROW_SIZE / (float)dimBlock.y), 1);
vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
```

{: .참고 }
> `dimBlock(32, 32, 1)` 이면 블록당 스레드 수는 **32 × 32 = 1024**. **블록당 최대 스레드 수 한계에 정확히 맞춘 값**이다.

결과: GPU가 CPU보다 **약 102배** 빠름

---

## 성능 비교 정리

{: .시험 }
> | 방식 | 배열 | GPU 대 CPU | CUDA Total 기준 |
> |---|---|---|---|
> | 1D 그리드 + 1D 블록 | 1차원 (1억 3천만) | **약 92배** | 2.26배 |
> | 1D 그리드 + 1D 블록 | 2차원 (8192×8192) | **약 65배** | 2.7배 |
> | 2D 그리드 + 1D 블록 | 2차원 | **약 94배** | 2.7배 |
> | 2D 그리드 + 2D 블록 | 2차원 | **약 102배** | 2.7배 |
> | 1D 배열 + 2D 그리드/블록 | 1차원 (8192×8192) | **약 104배** | 2.7배 |
>
> **결론 2가지**
>
> 1. **커널 안에서 for 루프를 도는 방식(1D+1D)이 가장 느리다.** 스레드를 더 많이 펼칠수록 빠르다.
> 2. **어떤 방식을 쓰든 CUDA Total은 2.7배 수준에서 더 좋아지지 않는다.** 병목이 **메모리 복사**이기 때문이다.
