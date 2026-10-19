# 코드 모음

실습에 나온 **API 레퍼런스와 전체 소스코드**만 모은 페이지입니다. 설명은 각 강의 페이지에, 여기는 **칠 것**만 있습니다.

## API 레퍼런스

### 헤더

```c
#include "cuda_runtime.h"              // CUDA runtime API
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
```

### 함수 실행 위치 키워드

```c
__host__    void f(void);     // host에서 호출, host에서 실행 (기본값, 생략 가능)
__device__  void f(void);     // device에서 호출, device에서 실행
__global__  void f(void);     // host에서 호출, device에서 실행 → 커널(kernel)
```

### 커널 호출

```c
kernel <<< 그리드차원크기, 블록차원크기 >>> (인자);

kernel <<< 1, n >>> ();               // 블록 1개, 스레드 n개
kernel <<< n, m >>> ();               // 블록 n개, 블록당 스레드 m개

dim3 dimGrid(3, 2, 1);                // dim3 자료형 사용
dim3 dimBlock(6, 4, 2);
kernel <<< dimGrid, dimBlock >>> ();

dim3 dimGrid(4);                      // 차원 크기가 1이면 생략 가능
dim3 dimBlock(8);                     // = dim3 dimBlock(8,1,1);
```

### 동기화

```c
cudaDeviceSynchronize();              // 호스트가 디바이스의 커널 수행 완료까지 대기
```

### 메모리 API

```c
cudaError_t cudaMalloc(void **ptr, size_t size);
cudaError_t cudaFree(void *ptr);
cudaError_t cudaMemset(void *ptr, int value, size_t size);
cudaError_t cudaMemcpy(void *dst, const void *src, size_t size,
                       enum cudaMemcpyKind kind);
cudaError_t cudaMemGetInfo(size_t *free, size_t *total);
const char* cudaGetErrorName(cudaError_t error);
```

| 함수 | 설명 |
|---|---|
| `cudaMalloc()` | 디바이스 메모리(global memory) 할당 |
| `cudaFree()` | 디바이스 메모리 해제 |
| `cudaMemset()` | 디바이스 메모리 초기화 |
| `cudaMemcpy()` | 호스트와 디바이스 사이의 메모리 복사 |
| `cudaMemGetInfo()` | 디바이스 메모리 총 크기 / 사용 가능 크기 |
| `cudaGetErrorName()` | 에러 코드를 문자열로 변환 |

성공 시 **`cudaSuccess` (0)** 반환, 실패 시 0 이외의 값 반환.

**cudaMemcpyKind 열거형**

```c
cudaMemcpyHostToHost
cudaMemcpyHostToDevice      // 호스트 → 디바이스
cudaMemcpyDeviceToHost      // 디바이스 → 호스트
cudaMemcpyDeviceToDevice
cudaMemcpyDefault           // 통합 메모리 지원 시 자동 판단
```

### 내장 변수

```c
gridDim.x,   gridDim.y,   gridDim.z      // 그리드 내 각 차원의 블록 수
blockIdx.x,  blockIdx.y,  blockIdx.z     // 그리드 내 블록 번호
blockDim.x,  blockDim.y,  blockDim.z     // 블록 내 각 차원의 스레드 수
threadIdx.x, threadIdx.y, threadIdx.z    // 블록 내 스레드 번호
```

### 인덱싱 공식

```c
// 1차원 배열, 1차원 그리드 + 1차원 블록
index = (blockIdx.x * blockDim.x) + threadIdx.x;

// 2차원 배열 공통
index = row * COL_SIZE + col;

// 2차원 배열, 조합별 col / row
col = (blockIdx.x * blockDim.x) + threadIdx.x;   // 세 조합 모두 동일
row = /* 1D grid + 1D block */  for 루프로 순회
row = /* 2D grid + 1D block */  blockIdx.y;
row = /* 2D grid + 2D block */  (blockIdx.y * blockDim.y) + threadIdx.y;
```

### 시간 측정

```c
#include <time.h>
clock_t start, end;

start = clock();
kernel <<<dimGrid, dimBlock>>> (...);
cudaDeviceSynchronize();          // 반드시 end 앞에
end = clock();

printf("%f ms\n", (double)(end - start) * 1000.0 / CLOCKS_PER_SEC);
```

---

## 전체 소스코드

### lec02_01.cu — Hello CUDA

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

__global__ void helloCUDA(void)                 // 커널 정의
{
    printf("Hello CUDA from GPU!\n");
}

int main(void)
{
    printf("Hello CUDA from CPU!\n");

    helloCUDA <<<1, 10>>>();                    // 커널 호출

    cudaDeviceSynchronize();                    // 디바이스 동기화

    return 0;
}
```

### lec02_02 — 호스트/디바이스 코드 분리

**lec02_02_device.cuh**

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

__global__ void helloCUDA(void);
__host__ void helloCUDACall(void);              // __host__ 생략 가능
```

**lec02_02_device.cu**

```c
#include "lec02_02_device.cuh"

__global__ void helloCUDA(void)
{
    printf("Hello CUDA from GPU!\n");
}

__host__ void helloCUDACall(void) {
    helloCUDA <<<1, 10>>> ();                   // 커널 호출은 .cu 안에서만
}
```

**lec02_02_host.cpp**

```cpp
#include "lec02_02_device.cuh"

int main(void)
{
    printf("Hello CUDA from CPU!\n");
    helloCUDACall();
    cudaDeviceSynchronize();
    return 0;
}
```

```bash
$ nvcc -o lec02_02 lec02_02_device.cu lec02_02_host.cpp
```

### lec03_02.cu — 디바이스 메모리 할당/초기화/해제

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

int main(void)
{
    int *dDataPtr;
    cudaMalloc(&dDataPtr, sizeof(int) * 32);     // 할당
    cudaMemset(dDataPtr, 0, sizeof(int) * 32);   // 초기화
    cudaFree(dDataPtr);                          // 해제
}
```

### lec03_03.cu — 메모리 정보 + 에러 코드 확인

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

    errorCode = cudaMalloc(&dDataPtr, sizeof(int) * 1024 * 1024);
    printf("cudaMalloc - %s\n", cudaGetErrorName(errorCode));
    checkDeviceMemory();

    errorCode = cudaMemset(dDataPtr, 0, sizeof(int) * 1024 * 1024);
    printf("cudaMemset - %s\n", cudaGetErrorName(errorCode));

    errorCode = cudaFree(dDataPtr);
    printf("cudaFree - %s\n", cudaGetErrorName(errorCode));
    checkDeviceMemory();
}
```

### lec03_04.cu — cudaMemcpy

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

__global__ void printData(int *_dDataPtr)
{
    printf("%d", _dDataPtr[threadIdx.x]);
}

__global__ void setData(int *_dDataPtr)
{
    _dDataPtr[threadIdx.x] = 2;
}

int main(void)
{
    int data[10] = {0};
    for (int i = 0; i < 10; i++)
        data[i] = 1;

    int *dDataPtr;
    cudaMalloc(&dDataPtr, sizeof(int) * 10);
    cudaMemset(dDataPtr, 0, sizeof(int) * 10);

    printf("Data in device: ");
    printData <<<1, 10>>> (dDataPtr);

    cudaMemcpy(dDataPtr, data, sizeof(int) * 10, cudaMemcpyHostToDevice);
    printf("\nHost -> Device: ");
    printData <<<1, 10>>> (dDataPtr);

    setData <<<1, 10>>> (dDataPtr);

    cudaMemcpy(data, dDataPtr, sizeof(int) * 10, cudaMemcpyDeviceToHost);
    printf("\nDevice -> Host: ");
    for (int i = 0; i < 10; i++)
        printf("%d", data[i]);
    printf("\n");

    cudaFree(dDataPtr);
}
```

### lec03_05.cu — CPU 벡터합

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_DATA 1024

int main(void)
{
    int *a, *b, *c;
    int memsize = sizeof(int) * NUM_DATA;

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

    for (int i = 0; i < NUM_DATA; i++)
        c[i] = a[i] + b[i];

    free(a); free(b); free(c);
    return 0;
}
```

### lec03_06.cu — GPU 벡터합

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_DATA 1024

__global__ void vecAdd(int *_a, int *_b, int *_c)
{
    int tID = threadIdx.x;
    _c[tID] = _a[tID] + _b[tID];
}

int main(void)
{
    int *a, *b, *c, *hc;
    int *da, *db, *dc;
    int memsize = sizeof(int) * NUM_DATA;
    int result;

    // 호스트 메모리 할당
    a  = (int *)malloc(memsize);
    b  = (int *)malloc(memsize);
    c  = (int *)malloc(memsize);
    hc = (int *)malloc(memsize);

    // 호스트 메모리 초기화
    memset(a, 0, memsize);
    memset(b, 0, memsize);
    memset(c, 0, memsize);
    memset(hc, 0, memsize);

    for (int i = 0; i < NUM_DATA; i++) {
        a[i] = rand() % 10;
        b[i] = rand() % 10;
    }

    // CPU 연산 (비교용)
    for (int i = 0; i < NUM_DATA; i++)
        hc[i] = a[i] + b[i];

    // 디바이스 메모리 할당
    cudaMalloc(&da, memsize);
    cudaMalloc(&db, memsize);
    cudaMalloc(&dc, memsize);

    // 디바이스 메모리 초기화
    cudaMemset(da, 0, memsize);
    cudaMemset(db, 0, memsize);
    cudaMemset(dc, 0, memsize);

    // 메모리 복사 (host -> device)
    cudaMemcpy(da, a, memsize, cudaMemcpyHostToDevice);
    cudaMemcpy(db, b, memsize, cudaMemcpyHostToDevice);

    // GPU 연산
    vecAdd <<<1, NUM_DATA>>> (da, db, dc);
    cudaDeviceSynchronize();

    // 메모리 복사 (device -> host)
    cudaMemcpy(c, dc, memsize, cudaMemcpyDeviceToHost);

    // 디바이스 메모리 해제
    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);

    // 결과 비교
    result = memcmp(c, hc, memsize);
    if (result == 0)
        printf("The vector sum on the device (GPU) is the same as the host (CPU)\n");
    else
        printf("The vector sum on the device (GPU) is not the same as the host (CPU)\n");

    free(a); free(b); free(c); free(hc);
    return 0;
}
```

### lec03_07.cu — 시간 측정 (커널 호출 부분)

```c
start_total = clock();

// 메모리 복사 (host -> device)
start = clock();
cudaMemcpy(da, a, memsize, cudaMemcpyHostToDevice);
cudaMemcpy(db, b, memsize, cudaMemcpyHostToDevice);
end = clock();
printf("Memory copy: host -> device: %f ms\n",
       (double)(end - start) * 1000.0 / CLOCKS_PER_SEC);

// GPU 연산
start = clock();
vecAdd <<<1, NUM_DATA>>> (da, db, dc);
cudaDeviceSynchronize();          // 없으면 커널 수행 시간이 정상 측정되지 않음
end = clock();
printf("Computation on device (GPU): %f ms\n",
       (double)(end - start) * 1000.0 / CLOCKS_PER_SEC);

// 메모리 복사 (device -> host)
start = clock();
cudaMemcpy(c, dc, memsize, cudaMemcpyDeviceToHost);
end = clock();
printf("Memory copy: device -> host: %f ms\n",
       (double)(end - start) * 1000.0 / CLOCKS_PER_SEC);

end_total = clock();
printf("CUDA Total: %f ms\n",
       (double)(end_total - start_total) * 1000.0 / CLOCKS_PER_SEC);
```

### lec04_01.cu — 내장 변수 확인

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__global__ void checkIndex(void)
{
    printf("gridDim:(%d, %d, %d) blockDim:(%d, %d, %d) "
           "blockIdx:(%d, %d, %d) threadIdx:(%d, %d, %d)\n",
           gridDim.x,  gridDim.y,  gridDim.z,
           blockDim.x, blockDim.y, blockDim.z,
           blockIdx.x, blockIdx.y, blockIdx.z,
           threadIdx.x, threadIdx.y, threadIdx.z);
}

int main(void)
{
    dim3 dimGrid(2, 1, 1);                      // dim3 dimGrid(2); 와 동일
    dim3 dimBlock(3, 1, 1);                     // dim3 dimBlock(3); 와 동일

    checkIndex <<< dimGrid, dimBlock >>> ();    // checkIndex <<< 2, 3 >>> (); 와 동일
    cudaDeviceSynchronize();
}
```

### lec05_01.cuh — 스레드 전역 번호 매크로 헤더

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

### lec05_02.cu — 1차원 배열 / 1D 그리드 + 1D 블록

```c
#define NUM_DATA 134217728              // 1024 * 1024 * 128

__global__ void vecAdd(int *da, int *db, int *dc)
{
    int index = (blockIdx.x * blockDim.x) + threadIdx.x;

    if (index < NUM_DATA)
        dc[index] = da[index] + db[index];
}
```

커널 호출:

```c
dim3 dimGrid(ceil((float)NUM_DATA / (float)256), 1, 1);
dim3 dimBlock(256, 1, 1);
vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
cudaDeviceSynchronize();
```

### lec05_06.cu — 1차원 배열 / 2D 그리드 + 2D 블록

```c
#include "lec05_01.cuh"

#define ROW_SIZE (8192)
#define COL_SIZE (8192)
#define MAT_SIZE (ROW_SIZE * COL_SIZE)

__global__ void vecAdd(float *da, float *db, float *dc)
{
    unsigned int index = GRID_2D_TID;

    if (index < MAT_SIZE)
        dc[index] = da[index] + db[index];
}
```

커널 호출:

```c
dim3 dimBlock(32, 32, 1);
dim3 dimGrid(ceil((float)COL_SIZE / (float)dimBlock.x),
             ceil((float)ROW_SIZE / (float)dimBlock.y), 1);
vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
```

### lec05_03.cu — 2차원 배열 / 1D 그리드 + 1D 블록

```c
__global__ void vecAdd(float *da, float *db, float *dc)
{
    unsigned int col = (blockIdx.x * blockDim.x) + threadIdx.x;

    if (col < COL_SIZE) {
        for (int row = 0; row < ROW_SIZE; row++) {
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

### lec05_04.cu — 2차원 배열 / 2D 그리드 + 1D 블록

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

### lec05_05.cu — 2차원 배열 / 2D 그리드 + 2D 블록

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
dim3 dimBlock(32, 32, 1);
dim3 dimGrid(ceil((float)COL_SIZE / (float)dimBlock.x),
             ceil((float)ROW_SIZE / (float)dimBlock.y), 1);
vecAdd <<<dimGrid, dimBlock>>> (da, db, dc);
```

### 2차원 배열 CPU 연산 (비교용)

```c
for (int row = 0; row < ROW_SIZE; row++) {
    for (int col = 0; col < COL_SIZE; col++) {
        hc[row * COL_SIZE + col] = a[row * COL_SIZE + col]
                                 + b[row * COL_SIZE + col];
    }
}
```

---

## job_gpu.sh — Slurm Job 스크립트

```bash
#!/bin/sh
#SBATCH -J job_name               # Job name
#SBATCH -p gpu                    # Partition (queue) name
#SBATCH --wait
#SBATCH --nodes=1                 # number of nodes
#SBATCH --ntasks-per-node=1       # number of mpi tasks (processes) per a node
#SBATCH --gres=gpu:1              # number of GPUs
#SBATCH -t 01:30:00               # Run time (hh:mm:ss)
#SBATCH -o job_stdout.%j.log      # Name of stdout output file (%j expands to jobId)
#SBATCH -e job_stderr.%j.log      # Name of stderr output file

cd $SLURM_SUBMIT_DIR
./lec02_01 >& lec02_01.log
```

---

## 명령어

```bash
$ nvcc -o prog prog.cu                       # 컴파일
$ nvcc -o prog dev.cu host.cpp               # 분리 컴파일
$ ./prog                                     # 실행

$ nvcc --version                             # NVCC 버전
$ nvidia-smi                                 # GPU 상태
$ watch -n 1 -d "nvidia-smi"                 # 1초마다 GPU 상태

$ sbatch job_gpu.sh                          # Slurm job 제출
$ cat prog.log                               # 결과 확인
$ tail -f prog.log

$ passwd                                     # 비밀번호 변경
$ quota -s                                   # 디스크 할당량 확인
```

CUDA 개발 환경 설치 (Ubuntu):

```bash
$ sudo apt update
$ sudo apt list nvidia-utils*
$ sudo apt install nvidia-utils-550
$ sudo apt install nvidia-cuda-toolkit
```
