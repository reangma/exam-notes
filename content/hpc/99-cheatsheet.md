# CUDA 치트시트

시험장에서 **머리에서 바로 꺼내 써야 하는 것**만 모았습니다.

## 1. CUDA 프로그램 전체 템플릿

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_DATA 1024

__global__ void vecAdd(int *da, int *db, int *dc)
{
    int index = (blockIdx.x * blockDim.x) + threadIdx.x;
    if (index < NUM_DATA)
        dc[index] = da[index] + db[index];
}

int main(void)
{
    int *a, *b, *c;
    int *da, *db, *dc;
    int memsize = sizeof(int) * NUM_DATA;

    // 1) 호스트 메모리 할당 + 초기화
    a = (int *)malloc(memsize);
    b = (int *)malloc(memsize);
    c = (int *)malloc(memsize);
    memset(a, 0, memsize);
    memset(b, 0, memsize);
    memset(c, 0, memsize);
    for (int i = 0; i < NUM_DATA; i++) {
        a[i] = rand() % 10;
        b[i] = rand() % 10;
    }

    // 2) 디바이스 메모리 할당 + 초기화
    cudaMalloc(&da, memsize);
    cudaMalloc(&db, memsize);
    cudaMalloc(&dc, memsize);
    cudaMemset(da, 0, memsize);
    cudaMemset(db, 0, memsize);
    cudaMemset(dc, 0, memsize);

    // 3) 메모리 복사 (host -> device)
    cudaMemcpy(da, a, memsize, cudaMemcpyHostToDevice);
    cudaMemcpy(db, b, memsize, cudaMemcpyHostToDevice);

    // 4) 커널 실행 + 동기화
    dim3 dimBlock(256, 1, 1);
    dim3 dimGrid(ceil((float)NUM_DATA / (float)dimBlock.x), 1, 1);
    vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
    cudaDeviceSynchronize();

    // 5) 메모리 복사 (device -> host)
    cudaMemcpy(c, dc, memsize, cudaMemcpyDeviceToHost);

    // 6) 해제
    cudaFree(da); cudaFree(db); cudaFree(dc);
    free(a); free(b); free(c);
    return 0;
}
```

{: .중요 }
> 순서: **호스트 할당 → 디바이스 할당 → H2D 복사 → 커널 → 동기화 → D2H 복사 → 해제**

---

## 2. 메모리 API

```c
cudaError_t cudaMalloc(void **ptr, size_t size);
cudaError_t cudaFree(void *ptr);
cudaError_t cudaMemset(void *ptr, int value, size_t size);
cudaError_t cudaMemcpy(void *dst, const void *src, size_t size, cudaMemcpyKind kind);
cudaError_t cudaMemGetInfo(size_t *free, size_t *total);
const char* cudaGetErrorName(cudaError_t error);
```

| 복사 방향 | 열거형 |
|---|---|
| 호스트 → 디바이스 | `cudaMemcpyHostToDevice` |
| 디바이스 → 호스트 | `cudaMemcpyDeviceToHost` |
| 디바이스 → 디바이스 | `cudaMemcpyDeviceToDevice` |
| 자동 판단 | `cudaMemcpyDefault` |

- 성공 = `cudaSuccess` (0)
- `cudaMalloc`의 첫 인자는 **`&포인터`** (포인터의 포인터)
- `cudaMemcpy`의 인자 순서는 **`dst, src`**

---

## 3. 인덱싱 공식

### 1차원 배열

```c
index = (blockIdx.x * blockDim.x) + threadIdx.x;
```

### 2차원 배열

```c
index = row * COL_SIZE + col;
```

| 조합 | `col` | `row` |
|---|---|---|
| 1D grid + 1D block | `blockIdx.x * blockDim.x + threadIdx.x` | for 루프 |
| 2D grid + 1D block | `blockIdx.x * blockDim.x + threadIdx.x` | `blockIdx.y` |
| 2D grid + 2D block | `blockIdx.x * blockDim.x + threadIdx.x` | `blockIdx.y * blockDim.y + threadIdx.y` |

### 전역 번호 (일반형)

```
NUM_THREAD_IN_BLOCK = blockDim.x * blockDim.y * blockDim.z

BLOCK_2D_TID = threadIdx.y * blockDim.x + threadIdx.x
BLOCK_3D_TID = threadIdx.z * (blockDim.y * blockDim.x) + BLOCK_2D_TID

GRID_1D_TID = blockIdx.x * NUM_THREAD_IN_BLOCK + BLOCK_3D_TID
GRID_2D_TID = blockIdx.y * (gridDim.x * NUM_THREAD_IN_BLOCK) + GRID_1D_TID
GRID_3D_TID = blockIdx.z * (gridDim.y * gridDim.x * NUM_THREAD_IN_BLOCK) + GRID_2D_TID
```

---

## 4. 숫자로 외울 것

| 항목 | 값 |
|---|---|
| **워프 크기** | **32** |
| **블록당 최대 스레드 수** | **1024** |
| `blockDim.x`, `blockDim.y` 최대 | **1024** |
| `blockDim.z` 최대 | **64** |
| `gridDim.x` 최대 | **2³¹ − 1** |
| `gridDim.y`, `gridDim.z` 최대 | **65535** |
| 그리드·블록 최대 차원 | **3** |
| 스레드당 최대 32-bit 레지스터 | **255** |
| 스레드당 최대 local memory | **512KB** |
| Constant memory size | **64KB** |
| Perf 등급 | **P0 ~ P12** (작을수록 좋음) |
| MIG 최대 분할 | **7개** |

---

## 5. 계층 대응

| 소프트웨어 | 하드웨어 |
|---|---|
| **스레드(thread)** | **CUDA core** |
| **블록(block)** | **SM (Streaming Multiprocessor)** |
| **그리드(grid)** | **GPU (device)** |

---

## 6. 키워드 / 확장자

| 키워드 | 호출 | 실행 |
|---|---|---|
| `__host__` (기본값) | host | host |
| `__device__` | device | device |
| `__global__` (커널) | **host** | **device** |

| | 호스트 | 디바이스 |
|---|---|---|
| 소스 | `.c` / `.cpp` | **`.cu`** |
| 헤더 | `.h` | **`.cuh`** |

---

## 7. 컴파일 / 실행 명령어

```bash
$ nvcc -o prog prog.cu                      # 컴파일
$ nvcc -o prog dev.cu host.cpp              # 분리 컴파일
$ ./prog

$ nvcc --version                            # NVCC 버전
$ nvidia-smi                                # GPU 상태
$ watch -n 1 -d "nvidia-smi"                # 1초마다 갱신

$ sbatch job_gpu.sh                         # Slurm job 제출
$ cat prog.log                              # 결과 확인
$ tail -f prog.log

$ quota -s                                  # 디스크 할당량 확인
$ passwd                                    # 비밀번호 변경
```

### Slurm job 스크립트

```bash
#!/bin/sh
#SBATCH -J job_name
#SBATCH -p gpu
#SBATCH --wait
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH -t 01:30:00
#SBATCH -o job_stdout.%j.log
#SBATCH -e job_stderr.%j.log

cd $SLURM_SUBMIT_DIR
./prog >& prog.log
```

---

## 8. 시간 측정

```c
#include <time.h>
clock_t start, end;

start = clock();
kernel <<<dimGrid, dimBlock>>> (...);
cudaDeviceSynchronize();          // 반드시 end 앞에!
end = clock();

printf("%f ms\n", (double)(end - start) * 1000.0 / CLOCKS_PER_SEC);
```

**CUDA Total = 메모리 복사 시간 + GPU 연산 시간**

---

## 9. 자주 틀리는 것

{: .주의 }
> - **`cudaDeviceSynchronize()` 빠뜨림** → `printf` 안 나옴, 시간 측정 엉뚱해짐
> - `cudaMalloc`에 **`&` 빠뜨림**
> - `cudaMemcpy` 인자 순서 (**`dst` 먼저**)
> - **`ceil()` 쓰면 커널 안 `if` 범위 검사 필수** (둘은 항상 세트)
> - **블록당 스레드 1024 초과** → 결과가 조용히 틀림
> - `<<< >>>` 를 **`.cpp` 파일에 쓰면 컴파일 에러** (`.cu`에만 가능)
> - **`Dim`은 개수, `Idx`는 번호** / **`grid-`는 블록용, `block-`은 스레드용**
> - **SIMT(GPU, 스레드) vs SIMD(CPU, 데이터)**
> - quota 표에서 **`quota` 열 = soft, `limit` 열 = hard**
