# 2. 개발 환경 구축

## RPi 4 Model B 하드웨어 구성

{: .시험 }
> 포트 이름과 **약어의 full name**(GPIO, CSI, DSI, PoE)을 묻기 좋음

| 번호 | 포트 | 설명 |
|---|---|---|
| ① | **GPIO** (general-purpose input/output) | 범용 입출력 포트. 디지털 값의 입력과 출력에 사용 |
| ② | USB 포트 | 마우스·키보드·무선랜카드 연결. USB 2.0과 3.0 지원 |
| ③ | Ethernet 포트 | 인터넷/인트라넷 네트워크 연결 |
| ④ | 아날로그 오디오 출력 | 오디오 연결 단자 |
| ⑤ | **CSI** (camera serial interface) | **카메라** 연결 인터페이스 |
| ⑥ | HDMI | **micro HDMI 2개** → 듀얼 모니터 가능 |
| ⑦ | USB-C | 전원. **5V, 700mA 이상** 공급. 스마트폰 충전 케이블과 연결 가능 |
| ⑧ | **DSI** (display serial interface) | **디스플레이 장치** 연결 인터페이스 |
| ⑨ | Micro SD 카드 슬롯 | 보드 **아래쪽**에 위치 |
| ⑩ | Wi-Fi 안테나 | |

### RPi 4 Model B 주요 스펙

- 고성능 **64비트 쿼드코어** 프로세서
- micro HDMI **2개** → **4K 해상도 듀얼 디스플레이**
- 최대 **4Kp60** 하드웨어 비디오 디코딩
- 최대 **8GB** RAM
- 듀얼 대역 **2.4/5.0GHz** 무선 LAN
- **Bluetooth 5.0**
- **기가비트** Ethernet
- USB 2.0 + USB 3.0
- **PoE (Power over Ethernet)**: Ethernet을 통한 전원 공급

{: .중요 }
> **Model A vs Model B**: Model B는 **유선 LAN(Ethernet 포트)이 있고**, Model A는 **없다**.

---

## 모델별 스펙 비교

| 모델 | RPi 4 Model B | RPi 3 Model B+ | RPi 3 Model B | RPi Zero |
|---|---|---|---|---|
| 출시일 | 2019.06.24 | 2018.03.14 | 2016.01.29 | 2015.11.25 |
| SoC | **BCM2711** | BCM2837B0 | BCM2837 | BCM2835 |
| CPU | Quad core **Cortex-A72** 64bit @1.5GHz | Quad core Cortex-A53 @1.4GHz | Quad core Cortex-A53 @1.2GHz | ARM11 @1GHz |
| RAM | 1/2/4/**8GB** | 1GB | 1GB | 512MB |
| Storage | Micro SD | Micro SD | Micro SD | Micro SD |
| Ethernet | **Gigabit** | Gigabit | 10/100 Mbit/s | **None** |
| 무선 LAN | 802.11 b/g/n/ac **dual band 2.4/5GHz** | b/g/n/ac dual band | b/g/n **single band 2.4GHz** | None |
| Bluetooth | **5.0** + BLE | 4.2 + BLE | 4.1 + BLE | None |
| **GPIO** | **40** | **40** | **40** | **40** |

{: .시험 }
> **GPIO 핀 수는 모든 모델이 40개로 동일**. RPi 3와 RPi 4는 **GPIO 핀 번호도 동일**하다.

### RPi 3부터 내장된 것

**Wi-Fi, 블루투스**가 기본 내장됨.

---

## 전원 / 케이블 준비물

| | RPi 4 Model B | RPi 3 Model B/B+ |
|---|---|---|
| 영상 | HDMI to **micro HDMI** 케이블 | **HDMI** 케이블 |
| 전원 | **5VDC 3A** 어댑터 (**USB-C**) | **5VDC 2.1A** 어댑터 (**micro 5pin**) |
| 저장 | Micro SD 16GB 이상 + 리더기 | 동일 |

---

## Raspberry Pi OS

- RPi의 **공식 운영체제** (이전 이름: **Raspbian**)
- **Debian 계열** 리눅스 배포판 — Debian을 RPi용으로 수정 후 **재빌드**한 것
- RPi는 **저전력을 목표로 한 ARM 아키텍처**를 사용하므로 Raspberry Pi OS가 **가장 안정적**
- LibreELEC, Ubuntu 등 다른 OS도 설치 가능

### 설치 흐름 (요약)

1. **SD Card Formatter**로 micro SD 포맷 (Overwrite format)
2. **Raspberry Pi Imager** 실행 → 장치 / 운영체제(**Raspberry Pi OS 64bit**) / 저장소 선택
3. "사용자 지정"에서 설정
   - **호스트 이름**: 네트워크에서 RPi를 구분하기 위해 부여하는 이름
   - 시간대(Asia/Seoul), 키보드 레이아웃(kr)
   - 사용자 ID / 비밀번호
   - **Wi-Fi SSID + 비밀번호**
   - **SSH 사용 켜기** (비밀번호 인증)
4. 기록 → SD 카드를 RPi 하단 슬롯에 삽입 → 부팅

{: .참고 }
> **Raspberry Pi Connect**: 라즈베리파이 재단이 공식 제공하는 **웹브라우저 기반 원격접속 서비스**

---

## 패키지 및 커널 업데이트

{: .시험 }
> 명령어와 **각 명령어의 의미**를 정확히 알아야 함

```bash
$ sudo apt-get update      # 설치된 패키지의 최신 버전 "정보" 확인
$ sudo apt-get upgrade     # 설치된 패키지를 최신 버전으로 "업그레이드"
```

```bash
$ sudo rpi-update          # Raspberry Pi OS "커널" 업데이트
$ sudo reboot              # 업데이트된 커널 반영을 위해 재시작
```

| 명령어 | 의미 |
|---|---|
| `sudo` | **super user(root)의 권한**(윈도우의 관리자 권한)으로 명령어를 실행 |
| `apt-get` | **데비안 계열**(Ubuntu, Raspberry Pi OS)의 **패키지 관리**(설치/삭제/업데이트) 명령어 |
| `rpi-update` | 커널 업데이트 |

설치 중 `y/n` 물음이 나오면 특별한 경우가 아니면 **y** 입력.

---

## 원격 접속 방법 4가지

{: .시험 }
> 어떤 방식이 **무엇을 제공하는지**(터미널 / GUI 화면 / 파일 전송 / 코드 편집) 구분

| 방식 | 제공 | 포트 |
|---|---|---|
| **Termius (SSH)** | 원격 터미널 + **SFTP 파일 송수신** | 22 |
| **VNC** | RPi의 **GUI 화면** 원격 조작 | — |
| **Windows 원격 데스크톱 (xrdp)** | RPi의 **데스크톱 화면** | **3389/tcp** |
| **VSCode Remote-SSH** | **소스코드 편집 + 터미널** | 22 |

### 1) Termius (SSH 원격 접속 + 파일 전송)

호스트 접속 정보:

| 항목 | 내용 |
|---|---|
| Address | 호스트의 **IP 주소** (예: 192.168.0.40) 또는 **도메인 이름** |
| General | 호스트 이름 설정 |
| SSH | 서버의 **port 번호** (예: **22**) |
| Credentials | 사용자 계정 이름 + 암호 |

파일 송수신은 화면 상단의 **SFTP** 클릭.

### 2) VNC

```bash
$ sudo raspi-config
```
→ **3 Interface Options** → **VNC** → **Yes** → OK → Finish → 재부팅

- PC에 **VNC Viewer** 설치 후 **RPi의 IP 주소** 입력
- **RPi와 PC가 같은 네트워크(같은 공유기)** 에 있어야 함

### 3) Windows 원격 데스크톱 (xrdp)

```bash
$ sudo apt-get update
$ sudo apt-get install xrdp
$ sudo systemctl enable xrdp
$ sudo systemctl start xrdp
$ sudo apt install ufw
$ sudo ufw allow 3389/tcp
$ sudo reboot
```

추가로 **Wayland → X11** 설정 필요:

```bash
$ sudo raspi-config
```
→ **6 Advanced Options** → **A7 Wayland** → **W1 X11** → OK → Finish → 재부팅

### 4) VSCode Remote-SSH

1. VSCode → Extensions → **remote-ssh** 검색 후 설치
2. 좌측 하단 **"open a remote window"** 아이콘 클릭
3. **Remote-SSH: Connect to Host...** → `사용자이름@IP주소` 입력 (예: `pi@192.168.0.5`)
4. 플랫폼은 **Linux** 선택 → 암호 입력
5. `File > Open Folder`로 작업 디렉토리 열기
6. `Terminal > New Terminal`로 터미널 생성

### RPi에 직접 VSCode 설치

```bash
$ sudo apt-get update
$ sudo apt-get install code
$ sudo reboot
```
실행: RPi 아이콘 → Programming → Visual Studio Code

{: .참고 }
> RPi에서 터미널 단축키: **Ctrl + Alt + T**

---

## 네트워크 구성 (핫스팟 활용)

RPi와 PC가 **같은 네트워크**에 있어야 원격 접속이 가능하다.

- 인터넷 공유기가 없으면 **Windows 노트북의 모바일 핫스팟** 또는 **스마트폰 핫스팟**이 공유기 역할
- Windows: `설정 > 네트워크 및 인터넷 > 모바일 핫스팟`에서 **SSID / 암호 / 대역(2.4GHz)** 설정
- 핫스팟 연결 목록에서 **RPi의 IP 주소 확인** 가능
- 스마트폰 핫스팟 사용 시 **Network Analyzer 앱**의 LAN → Scan으로 IP 확인

### iPhone 핫스팟 사용 시 (맥북 수동 IP 설정 예시)

| 항목 | 값 |
|---|---|
| IPv4 구성 | 수동 |
| IP 주소 | 172.20.10.2 |
| 서브넷 마스크 | 255.255.255.240 |
| 라우터 | 172.20.10.1 |
