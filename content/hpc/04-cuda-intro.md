# 4. CUDA 개요

## CUDA (Compute Unified Device Architecture)

**CUDA**: GPU를 **GPGPU 목적으로 사용할 수 있게 제공하는 프로그래밍 인터페이스**

### 제공 API

| 언어별 | 설명 |
|---|---|
| **CUDA C++** | C/C++ 언어로 작성되는 프로그램에서 사용 가능한 CUDA API |
| **CUDA Fortran** | Fortran 언어용 |
| **CUDA Python** | CUDA driver API와 runtime API에 대한 **wrapper** |

### driver API vs runtime API

{: .시험 }
> | | **CUDA driver API** | **CUDA runtime API** |
> |---|---|---|
> | 수준 | **저수준(low-level)** 제어 | **고수준(high-level)** 제어 |
> | 메모리 | 메모리 자원을 **더 효율적으로** 사용 가능 | — |
> | 난이도 | 구현 방법이 **복잡하여 사용하기 어려움** | **사용하기 간단함** |
> | 사용 | — | **대부분의 CUDA 프로그램이 사용**, **본 강의에서 사용** |

### CUDA-enabled GPU

CUDA 프로그래밍을 하려면 **CUDA를 지원하는 GPU**를 사용해야 한다.
지원 여부 확인: <https://developer.nvidia.com/cuda-gpus>

---

## Compute capability

**Compute capability**: **GPU 아키텍처(하드웨어)의 사양**(register, shared/local/constant memory 등)을 나타냄

{: .중요 }
> **Compute capability 버전 ≠ CUDA 버전**
>
> | | 의미 |
> |---|---|
> | **Compute capability 버전** | **GPU 아키텍처(하드웨어)** 의 버전 |
> | **CUDA 버전** | **CUDA 플랫폼(소프트웨어)** 의 버전. 여러 GPU 아키텍처를 지원 |

주요 사양 (compute capability 전반 공통값):

| 항목 | 값 |
|---|---|
| Number of 32-bit registers per SM | 64K |
| Maximum number of 32-bit registers per **thread** | **255** |
| Maximum amount of **local memory per thread** | **512KB** |
| **Constant memory size** | **64KB** |

---

## GPU 정보 확인 — nvidia-smi

```bash
$ nvidia-smi                      # GPU 상태 확인
$ watch -n 1 -d "nvidia-smi"      # 1초마다 GPU 상태 확인
```

`nvidia-smi` = **NVIDIA System Management Interface**

### 출력 항목

{: .시험 }
> 항목 중 **Perf, Persistence-M, Compute M., MIG M.** 의 설명을 묻기 좋다.

| 정보 | 설명 |
|---|---|
| **Driver Version** | GPU의 driver version |
| **CUDA Version** | CUDA의 version |
| **GPU** | 설치된 GPU의 ID (**0부터** 설정됨) |
| Fan | GPU fan 사용량(속도) |
| Name | GPU의 model명 |
| Temp | GPU의 현재 온도(섭씨) |
| **Perf** | GPU performance. **P0부터 P12까지** 존재하고 **숫자가 작을수록 성능이 좋음** |
| **Persistence-M** | 파워 지속성 모드. GPU를 사용하지 않아도 **nvidia driver를 항상 미리 로딩**해두는 모드. 빠른 GPU 사용에 유리하지만 **전력을 낭비** |
| Pwr:Usage/Cap | GPU의 현재 전력 사용량과 최대 용량 |
| Bus-ID | GPU가 설치된 PCI slot의 Bus ID |
| Disp.A | GPU를 **모니터 화면 출력용**으로 사용하면 on |
| **Memory-Usage** | 현재 사용 중인 GPU memory / 총 memory (1 MiB = 1024² byte) |
| GPU-Util | GPU 사용량 (최대 100%) |
| **Volatile Uncorr. ECC** | Volatile Uncorrectable error correction code. 데이터 처리 중 발생하는 에러 수치. 증가하면 **system이 hang 상태**가 될 수 있어 일반적으로 **N/A로 설정** |
| **Compute M.** | Compute-Mode (아래 표) |
| **MIG M.** | Multi-Instance GPU (아래 설명) |

### Compute Mode

| 모드 | 설명 |
|---|---|
| **Default** | 여러 host 스레드들이 GPU 사용 가능 (**여러 개의 CUDA context 생성**) |
| **Exclusive-process** | **단지 하나의 CUDA context**만 생성됨 |
| **Prohibited** | **CUDA context가 생성되지 않음** |

{: .참고 }
> **CUDA context**: CUDA 프로그램이 실행되는 데 필요한 **모든 GPU 하드웨어 리소스를 캡슐화**한 것

### MIG (Multi-Instance GPU)

- NVIDIA GPU를 **slice하는 기능**으로 **최대 7개의 개별 GPU instance**로 분할
- 여러 사용자에게 별도의 GPU를 제공하여 작업 가속화
- **NVIDIA H100, A100, A30에서만 가능**

---

## CUDA toolkit 설치 (Ubuntu)

**CUDA toolkit**: CUDA 프로그램 개발 도구(라이브러리, 디버깅·최적화 도구, **NVCC** 컴파일러) 제공

```bash
$ sudo apt update
$ sudo apt list nvidia-utils*            # 설치 가능한 nvidia-utils 패키지 확인
$ sudo apt install nvidia-utils-550      # GPU driver, nvidia-smi 설치
$ sudo apt install nvidia-cuda-toolkit   # CUDA 프로그램 개발 도구 설치

$ nvidia-smi                             # GPU 상태 확인
$ nvcc --version                         # 설치된 NVCC 버전 확인
```

**NVCC** = **NVIDIA CUDA Compiler**

---

## 호스트와 디바이스

{: .시험 }
> **확장자까지 묻는다.** 표를 통째로 외울 것.
>
> | | **호스트(host)** | **디바이스(device)** |
> |---|---|---|
> | 하드웨어 | **CPU** | **GPU** |
> | 메모리 | **호스트 메모리** (CPU가 사용) | **디바이스 메모리** (GPU가 사용) |
> | 코드 실행 위치 | **CPU에서 실행** | **GPU에서 실행** |
> | 문법 | **C/C++ 문법** | **CUDA 문법** |
> | 파일 확장자 | **`.c` 또는 `.cpp`** | **`.cu`** |
> | 헤더 확장자 | **`.h`** | **`.cuh`** |

---

## 함수 실행 위치 지정 키워드

{: .중요 }
> | 키워드 | 호출되는 곳 | 실행되는 곳 |
> |---|---|---|
> | **`__host__`** | **host** | **host** |
> | **`__device__`** | **device** | **device** |
> | **`__global__`** | **host** | **device** → 이것이 **커널(kernel)** |
>
> 함수 선언/정의 시 **키워드를 붙이지 않으면 기본값은 `__host__`** 이다.

---

## CUDA 프로그램의 구성과 컴파일

- CUDA 프로그램은 **호스트 코드(.c, .cpp)와 디바이스 코드(.cu)** 로 구성
- 호스트 코드와 디바이스 코드는 **NVCC 컴파일러로 컴파일 가능**
- **커널과 커널 호출 함수가 포함된 디바이스 코드는 NVCC 컴파일러만 컴파일 가능**

---

## Hello CUDA

### 커널 호출 문법

```
kernel <<< 스레드 블록 수, 블록당 스레드 수 >>> (인자);
```

- `<<< >>>` 를 **실행 구성(execution configuration) 문법**이라고 함
- 각 스레드는 **하나의 CUDA 코어**를 사용하여 **독립적으로** 커널 수행

### 코드 (lec02_01.cu)

```c
#include "cuda_runtime.h"              // CUDA runtime API 헤더 파일
#include "device_launch_parameters.h"
#include <stdio.h>

__global__ void helloCUDA(void)        // helloCUDA() 커널 정의
{
    printf("Hello CUDA from GPU!\n");
}

int main(void)
{
    printf("Hello CUDA from CPU!\n");

    // 1개의 스레드 블록, 블록당 10개의 스레드로 커널 실행
    helloCUDA <<<1, 10>>>();

    // 디바이스 동기화 (호스트가 커널 수행 완료까지 대기)
    cudaDeviceSynchronize();

    return 0;
}
```

{: .시험 }
> **`cudaDeviceSynchronize()` 를 왜 호출해야 하는가?**
>
> 호스트는 디바이스에게 task들(메모리 복사, 커널 실행 등)을 맡긴 뒤 **기다리지 않고 다음 작업을 수행(비동기적)** 한다.
> 따라서 **동기화 함수를 호출하지 않으면 커널 내의 `printf` 문이 출력되기 전에 프로그램이 종료**되어 버린다.

### 컴파일 및 실행

```bash
$ nvcc -o lec02_01 lec02_01.cu
$ ./lec02_01
Hello CUDA from CPU!
Hello CUDA from GPU!      ← 10번 출력
```

---

## 호스트/디바이스 코드 분리

### 올바른 분리

**lec02_02_device.cuh** (헤더)

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

__global__ void helloCUDA(void);
__host__ void helloCUDACall(void);      // __host__ 키워드는 생략 가능
```

**lec02_02_device.cu** (디바이스 코드)

```c
#include "lec02_02_device.cuh"

__global__ void helloCUDA(void)         // 커널 정의
{
    printf("Hello CUDA from GPU!\n");   // device에서 커널 실행
}

__host__ void helloCUDACall(void) {
    helloCUDA <<<1, 10>>> ();           // host에서 커널 호출
}
```

**lec02_02_host.cpp** (호스트 코드)

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

### 잘못된 분리 (에러 발생)

```cpp
// lec02_03_host.cpp
#include "lec02_03_device.cuh"

int main(void)
{
    printf("Hello CUDA from CPU!\n");
    helloCUDA <<<1, 10>>> ();      // 에러 발생 지점
    cudaDeviceSynchronize();
    return 0;
}
```

{: .시험 }
> **왜 에러가 나는가?**
>
> NVCC로 컴파일할 때 **NVCC는 `.cpp` 파일을 C++ 코드로 컴파일**하기 때문에, CUDA 문법인 **`<<<1, 10>>>` 을 해석하지 못해서 에러가 발생**한다.
>
> → **커널 호출(`<<< >>>`)은 반드시 `.cu` 파일 안에** 있어야 하고, `.cpp`에서는 그 커널 호출을 감싼 **일반 함수(`helloCUDACall`)를 호출**해야 한다.

---

## Slurm으로 CUDA 프로그램 실행

{: .중요 }
> 강의계획서에는 **PBS**라고 되어 있지만, 실제 슬라이드의 예제는 전부 **Slurm**(`sbatch`, `#SBATCH`)을 사용한다.

### 1) 컴파일

```bash
$ nvcc -o lec02_01 lec02_01.cu
```

### 2) Job 스크립트 작성 (job_gpu.sh)

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

### 3) Job 제출 및 결과 확인

```bash
$ sbatch job_gpu.sh
$ cat lec02_01.log
$ tail -f lec02_01.log
```

{: .시험 }
> **`#SBATCH` 옵션 의미**
>
> | 옵션 | 의미 |
> |---|---|
> | `-J` | Job name |
> | `-p gpu` | **Partition(queue) 이름** |
> | `--nodes=1` | 노드 수 |
> | `--ntasks-per-node=1` | 노드당 MPI task(프로세스) 수 |
> | **`--gres=gpu:1`** | **사용할 GPU 개수** |
> | `-t 01:30:00` | 실행 시간 제한 (hh:mm:ss) |
> | `-o` / `-e` | stdout / stderr 출력 파일명 (`%j` = jobId) |
> | `$SLURM_SUBMIT_DIR` | job을 제출한 디렉토리 |
