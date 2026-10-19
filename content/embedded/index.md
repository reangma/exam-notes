# 임베디드 IoT 프로그래밍

라즈베리파이(RPi) + 리눅스 + Python 기반 IoT 임베디드 프로그래밍 정리.

## 강의 목록

| 강의 | 주차 | 핵심 |
|---|---|---|
| [1. IoT와 오픈소스](01-iot-opensource.html) | 1주차 | 오픈소스 라이선스, 아두이노 vs RPi |
| [2. 개발 환경 구축](02-dev-env.html) | 2주차 | RPi 하드웨어 구성, 원격 접속 4종 |
| [3. 리눅스 기초](03-linux.html) | 3~4주차 | 디렉토리 구조, 쉘 명령어, 첫 LED |
| [4. 전자회로 기초](04-circuit.html) | 5주차 | 옴·키르히호프 법칙, 전자부품 |
| [5. GPIO 및 센서 활용](05-gpio-sensor.html) | 6~7주차 | GPIO, PWM, 센서, SPI/I2C |
| [코드 모음](98-code.html) | — | 함수 레퍼런스 + 전체 소스코드 |
| [실기 치트시트](99-cheatsheet.html) | — | 시험 직전 훑어보기 |

## 중간고사 범위

**8주차 중간고사 = 1~7주차** (위 5개 강의 전부), **필기 + 실기**.

실기는 제한 시간 내에 요구되는 사항을 프로그래밍하는 형태이므로, 아래 세 가지는 **코드를 외워서 바로 칠 수 있어야** 합니다.

1. `RPi.GPIO` 기본 템플릿 — setmode → setup → output/input → cleanup
2. PWM 템플릿 — `GPIO.PWM` → `start` → `ChangeDutyCycle` / `ChangeFrequency` → `stop`
3. SPI/MCP3008 템플릿 — `spidev` → `open(0,0)` → `readadc()`

→ [코드 모음](98-code.html)에 실습 코드 전부, [실기 치트시트](99-cheatsheet.html)에 핵심 요약을 모아뒀습니다.

## 기말고사 범위 (9~15주차, 정리 예정)

| 주차 | 내용 |
|---|---|
| 9~10 | Flask를 이용한 웹서버 구축 및 LED 제어 |
| 11~12 | 포트포워딩·슈퍼DMZ로 외부에서 LED 제어 |
| 13 | RPi 카메라를 이용한 Motion 감지 |
| 14 | NodeMCU로 MQTT 활용 |
