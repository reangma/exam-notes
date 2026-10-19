# 2. 개발 환경 구축

## HPC 클러스터 원격 접속 (Termius)

**Termius**: SSH를 이용한 **원격 접속(로그인) 및 파일 송수신** 기능 제공

### 호스트 접속 정보 설정 항목

| 항목 | 내용 |
|---|---|
| **Address** | 호스트의 **IP 주소**(예: 192.168.0.40) 또는 **도메인 이름** |
| **General** | 호스트 이름 설정 |
| **SSH** | 호스트 내 서버의 **port 번호** |
| **Credentials** | 사용자 계정 이름과 암호 |

### 본 강의 HPC 클러스터 접속 정보

| 구분 | 설정값 |
|---|---|
| **IP address** | **203.237.178.18** |
| General | HPC |
| **Port** | **19134** |
| User ID | `user##` |
| Password | 핸드폰 번호 뒤 4자리 |

{: .주의 }
> **Port가 22가 아니라 19134**다. 기본 SSH 포트를 그대로 쓰면 접속되지 않는다.

### 파일 송수신

화면 상단의 **SFTP** 클릭 → 접속할 호스트 선택 → 좌측(내 컴퓨터) / 우측(접속한 호스트) 파일 시스템을 오가며 전송.

---

## passwd — 비밀번호 변경

```bash
$ passwd
Changing password for user kjsung.
Current password:
```

---

## 디스크 할당량 (quota)

**quota**: 사용자의 **디스크 사용량**과 **생성할 수 있는 파일의 수(inode 수)** 를 제한하는 것

{: .시험 }
> **Hard limit vs Soft limit** — 둘의 차이와 유예기간(grace time) 동작이 핵심
>
> | 구분 | 의미 |
> |---|---|
> | **Hard limit** | 사용자/그룹의 디스크 사용량과 생성 가능한 파일 개수의 **최대값**. 절대 초과 불가 |
> | **Soft limit** | 초과하더라도 **hard limit를 넘지 않는다면**, **유예기간(grace time) 동안만** 경고를 받으며 **초과한 값을 사용 가능** |
>
> - 유예기간 동안 사용량이 다시 **soft limit보다 작아지면 유예기간 타이머는 리셋**된다.
> - **유예기간의 초기값은 7일**이다.

### 본 강의에서 할당되는 quota

| 대상 | Soft limit | Hard limit |
|---|---|---|
| 홈 디렉토리 **디스크 공간** | **9GB** | **10GB** |
| 홈 디렉토리 **생성 가능 파일 수** | **190,000** | **200,000** |

### quota 확인

```bash
$ quota -s
Disk quotas for user kjsung (uid 1000):
Filesystem   space   quota   limit   grace   files   quota   limit   grace
/dev/mapper/rl-home
             2172K   9216M  10240M              43    190k    200k
```

| 열 | 의미 |
|---|---|
| `space` | 현재 디스크 공간 사용량 |
| `quota` | **Soft limit** |
| `limit` | **Hard limit** |
| `grace` | soft limit 초과 시 **남은 유예기간** |
| `files` | 현재 생성한 파일 수 |

{: .중요 }
> 표에서 **`quota` 열이 soft limit, `limit` 열이 hard limit**이다. 이름이 헷갈리게 되어 있으니 주의.

---

## 리눅스 명령어

이 강의의 리눅스 명령어 부분은 **임베디드 IoT 프로그래밍 3강과 내용이 완전히 동일**하다.

→ [임베디드 3. 리눅스 기초](../embedded/03-linux.html) 참고

다루는 내용:

| 항목 | 내용 |
|---|---|
| 디렉토리 구조 | `/`, `/bin`, `/sbin`, `/dev`, `/lib`, `/root`, `/etc`, `/proc`, `/usr/*`, `/home` |
| 파일 목록 | `ls` 와 옵션 `-l -a -h -r -t -F -R` |
| 이동 | `cd`, 메타심볼 `.` `..` `~` `-`, `pwd`, `echo $HOME` |
| 생성/삭제 | `mkdir -p`, `rm -rf` |
| 복사/이동 | `cp`, `cp -r`, `mv` |
| 내용 출력 | `cat`, `tail`, `tail -n`, `tail -f` |
| 압축 | `tar -cvf/-xvf`, `-zcvf`(gzip), `-jcvf`(bzip2), `zip -r`, `unzip` |
| 프로세스 | `ps -f`, `ps -ef`, `kill PID`, `kill -9 PID`, Ctrl+C(SIGINT) |

{: .참고 }
> HPC 강의에서 **추가로 나오는 것은 `passwd` 와 `quota -s` 두 가지**뿐이다.
