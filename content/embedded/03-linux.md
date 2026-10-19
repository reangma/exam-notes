# 3. RPi를 위한 리눅스 기초

## 리눅스 디렉토리 구조

리눅스는 파일 관리를 위해 **트리(tree) 형태**의 디렉토리 구조를 사용한다.

- **하나의 루트 디렉토리(`/`)** 를 가짐
- 데이터를 저장하는 가장 기본 단위는 **파일**
- 리눅스는 일반 파일뿐 아니라 **디렉토리와 디바이스도 파일로 취급**

| 디렉토리 | 설명 |
|---|---|
| `/` | **루트 디렉토리**. 가장 최상위. **root의 홈 디렉토리인 `/root`와 다름** |
| `/bin` | 리눅스의 **기본 유틸리티** |
| `/sbin` | 리눅스의 **기본 시스템 유틸리티** |
| `/dev` | 장치에 대한 **디바이스 파일** |
| `/lib` | **공유 라이브러리** |
| `/root` | **super user(root)의 홈 디렉토리** |
| `/etc` | **시스템 설정** 관련 파일 |
| `/proc` | 프로세스(실행 중인 프로그램)와 시스템(커널)의 상태를 저장하는 **의사 파일 시스템(pseudo file system)** |
| `/usr` | 리눅스 **배포판이 제공**하는 유틸리티·헤더·라이브러리 |
| `/usr/include` | 프로그래밍 관련 **헤더 파일** |
| `/usr/lib` | 프로그래밍 관련 **라이브러리** |
| `/usr/bin` | `/bin`과 비슷하지만 **배포판이 제공**하는 유틸리티 |
| `/usr/sbin` | `/sbin`과 비슷하지만 **배포판이 제공**하는 시스템 유틸리티 |
| `/usr/local` | **시스템 관리자**가 제공하는 유틸리티·헤더·라이브러리 |
| `/home` | **사용자의 홈 디렉토리들** |

{: .시험 }
> `/bin` vs `/usr/bin` vs `/usr/local` 구분: **기본 / 배포판 제공 / 시스템 관리자 제공**

---

## ls — 파일 목록

```bash
$ ls [옵션] [파일 또는 디렉토리]
```

- **디렉토리**를 입력 → 해당 디렉토리 내의 파일과 디렉토리 출력
- **파일**을 입력 → 해당 파일 출력
- **아무것도 입력 안 함** → 현재 디렉토리의 파일과 디렉토리 출력

| 옵션 | 내용 |
|---|---|
| `-l` | 파일 속성 출력 (파일 종류, 권한, 하드링크 수, 소유자, 소유그룹, 크기, 마지막 변경 날짜, 파일 이름) |
| `-a` | **`.`으로 시작하는 숨긴 파일**과 디렉토리도 출력 |
| `-h` | 파일 크기를 **사람이 읽기 편한 단위(K, M, G)** 로 출력 |
| `-r` | **역순**으로 출력 |
| `-t` | **마지막 변경 날짜순**으로 출력 |
| `-F` | 실행파일 `*`, 디렉토리 `/`, 심볼릭 링크 `@` 를 끝에 출력 |
| `-R` | 해당 디렉토리 및 **하위 디렉토리 내용까지** 출력 |

옵션은 `-a -l -F`처럼 따로 주거나 `-alF`처럼 **한꺼번에** 쓸 수 있다.

```bash
$ ls -al
total 40
drwx------  6 kjsung smu   182 Jul 24 08:39 .
drwxr-xr-x. 3 root   root   20 Jul 22 03:17 ..
-rw-------  1 kjsung smu  7870 Jul 24 08:41 .bash_history
drwxr-xr-x  3 kjsung smu    22 Jul 22 10:10 cuda
```

---

## cd — 디렉토리 이동

```bash
$ cd 디렉토리
```

- 디렉토리명을 **안 쓰면 사용자의 홈 디렉토리로 이동**
- **절대경로**: 루트 디렉토리(`/`)로부터의 경로
- **상대경로**: 현재 디렉토리를 기준으로 나타낸 경로

| 메타 심볼 | 의미 |
|---|---|
| `.` | **현재** 디렉토리 |
| `..` | **한 단계 상위** 디렉토리 |
| `~` | **사용자의 홈** 디렉토리 |
| `-` | **이전** 디렉토리 |

`/usr/include` 에서 `/usr/local` 로 이동하는 경우:

```bash
$ cd /usr/local       # 절대경로
$ cd ../local         # 상대경로
```

### 홈 디렉토리

- 각 사용자마다 **`/home` 아래**에 있음
- **처음 로그인했을 때 위치**하는 디렉토리
- 경로는 환경변수 **`$HOME`** 에 저장됨

아래 4가지는 모두 홈 디렉토리로 이동:

```bash
$ cd
$ cd ~
$ cd $HOME
$ cd /home/사용자
```

---

## pwd / echo

```bash
$ pwd                  # 현재 위치한 디렉토리 경로 출력
/home/kwangjae

$ echo $HOME           # 명령어 다음에 나오는 문자열을 출력
/home/kwangjae
```

---

## mkdir / rm

```bash
$ mkdir 디렉토리
$ mkdir webapps                 # 디렉토리 webapps 생성
$ mkdir -p webapps/ch02         # 하위 디렉토리까지 한 번에 생성
```

```bash
$ rm read.txt                   # 파일 삭제
$ rm -rf directory              # 디렉토리 삭제
```

{: .주의 }
> 디렉토리를 만들거나 지울 때는 **`-p`(하위까지 생성)**, **`-rf`(디렉토리 삭제)** 옵션이 필수.

---

## cp — 복사

```bash
$ cp 원본_파일 복사본_파일
$ cp read.txt read_copy.txt                # 다른 이름으로 복사

$ cp 원본_파일 복사될_디렉토리
$ cp read.txt test                         # 디렉토리 안으로 복사

$ cp 원본_파일 복사될_디렉토리/복사본_이름
$ cp read.txt test/rename.txt              # 디렉토리 안에 다른 이름으로 복사

$ cp -r 원본_디렉토리 복사본_디렉토리
$ cp -r test test_copy                     # 디렉토리 복사는 -r
```

---

## mv — 이동 / 이름 변경

```bash
$ mv 파일_또는_디렉토리 이동할_디렉토리
$ mv myfile.txt test                 # 파일을 디렉토리 test로 이동

$ mv 파일_또는_디렉토리 변경할_이름
$ mv myfile.txt yourfile.txt         # 파일 이름 변경
$ mv testb testc                     # 디렉토리 이름 변경
```

{: .시험 }
> `mv`는 **이동과 이름 변경이 같은 명령어**. 두 번째 인자가 존재하는 디렉토리면 이동, 아니면 이름 변경.

---

## cat / tail — 파일 내용 출력

```bash
$ cat 파일              # 파일 내용을 화면에 출력
$ cat .bashrc
```

```bash
$ tail 파일             # 파일의 "마지막 10줄" 출력
$ tail -n 5 .bashrc     # 마지막 5줄 출력
$ tail -5 .bashrc       # 위와 동일
$ tail -f 파일          # 실시간으로 마지막 10줄 출력 (로그 확인에 유용)
```

`tail -f` 종료는 **Ctrl+C** 또는 **Ctrl+Z**.

---

## 압축 / 묶음

{: .중요 }
> **`tar`는 "묶음"이지 압축이 아니다.** 압축하려면 gzip(`z`) 또는 bzip2(`j`) 옵션을 붙여야 한다.

### tar (묶기만)

```bash
$ tar -cvf aaa.tar aaa       # 묶음 (c: create)
$ tar -xvf aaa.tar           # 묶음 해제 (x: extract)
```

### tar + gzip / bzip2 (압축)

```bash
$ tar -zcvf ccc.tar.gz  ccc  # gzip으로 압축
$ tar -jcvf ccc.tar.bz2 ccc  # bzip2로 압축

$ tar -zxvf ccc.tar.gz       # gzip 압축 해제
$ tar -jxvf ccc.tar.bz2      # bzip2 압축 해제
```

| 옵션 | 의미 |
|---|---|
| `c` | create (묶기) |
| `x` | extract (풀기) |
| `v` | verbose (과정 출력) |
| `f` | file (파일명 지정) |
| `z` | **gzip** |
| `j` | **bzip2** |

### zip

```bash
$ sudo apt-get install zip unzip    # 설치되어 있지 않은 경우
$ zip -r ccc.zip ccc                # 압축
$ unzip ccc.zip                     # 압축 해제
```

---

## ps — 프로세스 확인

```bash
$ ps -f      # foreground 프로세스만 확인
$ ps -ef     # foreground + background 프로세스 모두 확인
```

```
$ ps -f
UID       PID   PPID  C STIME TTY      TIME     CMD
kwangjae  2373  2362  0 09:46 pts/0    00:00:00 bash
kwangjae  8895  2373  0 20:31 pts/0    00:00:00 ps -f
```

---

## 프로세스 종료

### 터미널 단축키

**Ctrl + C** (인터럽트 키)를 입력하면 커널이 해당 프로세스에 **SIGINT 시그널**을 보내 종료시킨다.

### kill 명령어

**PID(프로세스 ID)** 를 이용해 해당 프로세스에 **시그널을 전송**하는 명령어. 주로 종료에 사용.

```bash
$ kill PID            # 프로세스 종료
$ kill -9 PID         # 프로세스 강제 종료

$ kill 5587           # 프로세스(5587) 종료
$ kill -9 5602        # 프로세스(5602) 강제 종료
```

---

## 첫 실습 — RPi로 LED 동작시키기

### 회로

| 라즈베리파이 | LED |
|---|---|
| **8번 핀** (BOARD 모드) | **긴 다리** (+극, anode) |
| **GND** | **짧은 다리** (−극, cathode) |

- 준비물: 암수 점퍼선 2개, **저항 100Ω**(1kΩ까지 가능), LED 1개, 브레드보드
- **GND(접지)**: 0V로써 전류의 흐름을 받는 곳(−극)
- **GPIO 핀들은 3.3V 회로만 사용 가능**
- RPi 3과 RPi 4의 **GPIO 핀 번호는 동일**

### 코드 (led_ex01.py)

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 8

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while 1:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
```

{: .중요 }
> 이 코드는 **BOARD 모드**이므로 `LED = 8`은 **물리적 8번 핀**을 의미한다. (5강부터는 주로 **BCM 모드**를 쓰므로 혼동 주의)

### 실행

- Geany 또는 VSCode에서 **F5**
- LED가 **0.5초 간격**으로 켜짐/꺼짐 반복
- 중단은 **Ctrl+C** → 프로세스에 interrupt 발생 → 프로그램 종료

### 작업 디렉토리 만들기

```bash
$ mkdir -p webapps/ch01/
```
