# 고성능 컴퓨팅

HPC 클러스터와 CUDA를 이용한 CPU·GPU 병렬 프로그래밍 정리.

## 강의 목록

| 강의 | 주차 | 핵심 |
|---|---|---|
| [1. HPC 개요](01-hpc-overview.html) | 1주차 | 슈퍼컴퓨터, HPC 특징, SW 구성요소 |
| [2. 개발 환경 구축](02-dev-env.html) | 2주차 | HPC 클러스터 접속, quota |
| [3. GPGPU 및 병렬처리](03-gpgpu-parallel.html) | 5주차 | SIMD/SIMT, CPU vs GPU |
| [4. CUDA 개요](04-cuda-intro.html) | 5주차 | host/device, 키워드, Hello CUDA, Slurm |
| [5. CUDA 프로그램의 기본 흐름](05-cuda-flow.html) | 6주차 | 메모리 API, 벡터합, 성능 측정 |
| [6. CUDA 스레드 계층](06-cuda-thread-hierarchy.html) | 7주차 | thread/warp/block/grid, 내장 변수 |
| [7. 스레드 레이아웃과 인덱싱](07-cuda-thread-indexing.html) | 9주차 | 전역 번호, 1D/2D 인덱싱 |
| [코드 모음](98-code.html) | — | API 레퍼런스 + 전체 소스코드 |
| [CUDA 치트시트](99-cheatsheet.html) | — | 시험 직전 훑어보기 |

## 중간고사 범위

**8주차 중간고사 = 1~7주차**, **프로그래밍 문제**로 출제됩니다.

위 목록에서 **1~6강**이 중간고사 범위입니다. (7강은 9주차 내용이지만 5강에서 발생한 문제를 해결하는 부분이라 같이 정리해뒀습니다.)

프로그래밍 문제이므로 아래 세 가지는 **코드를 외워서 바로 칠 수 있어야** 합니다.

1. **CUDA 프로그램 3단계** — H2D 복사 → 커널 실행 → D2H 복사
2. **메모리 API** — `cudaMalloc` / `cudaMemset` / `cudaMemcpy` / `cudaFree`
3. **인덱싱 공식** — `(blockIdx.x * blockDim.x) + threadIdx.x`

→ [코드 모음](98-code.html)에 실습 코드 전부, [CUDA 치트시트](99-cheatsheet.html)에 핵심 요약을 모아뒀습니다.

{: .주의 }
> **강의계획서와 실제 자료가 다른 부분**
>
> - 계획서상 3~4주차는 **"PBS를 이용한 CPU 병렬 프로그래밍"** 이지만, **해당 PDF 자료가 없습니다.**
> - 또한 슬라이드의 모든 실행 예제는 PBS가 아니라 **Slurm**(`sbatch`, `#SBATCH`)을 사용합니다.
> - PBS 관련 자료를 받으면 추가 정리가 필요합니다.

## 기말고사 범위 (9~15주차, 정리 예정)

| 주차 | 내용 |
|---|---|
| 9 | CUDA 스레드 레이아웃과 인덱싱 ([정리 완료](07-cuda-thread-indexing.html)) |
| 10 | CUDA 실행 모델 |
| 11 | CUDA 기반 행렬 곱셈 프로그램 |
| 12 | CUDA 메모리 계층 |
| 13 | 공유 메모리 기반 행렬 곱셈 프로그램 |
| 14 | CUDA 메모리 접근 성능 최적화 |
