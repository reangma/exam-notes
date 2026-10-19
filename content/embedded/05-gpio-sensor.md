# 5. RPi GPIO 및 센서 활용

## GPIO (General Purpose Input Output)

**GPIO**: 마이크로프로세서가 **주변장치와 통신하기 위해 범용으로 사용되는 입출력 포트**

### GPIO 핀의 성질

- **3.3V를 기본 전압**으로 사용
- **입력 또는 출력으로 설정**하여 사용

| | 값 |
|---|---|
| **입력** | 0V(Low, False, 0) 또는 3.3V(High, True, 1)를 **입력받음** |
| **출력** | 0V(Low, False, 0) 또는 3.3V(High, True, 1)를 **출력함** |

### 40핀 구성

| 종류 | 개수 |
|---|---|
| **3.3V 전원용 핀** | **2개** |
| **5V 전원용 핀** | **2개** |
| **GND (0V, −극) 핀** | **8개** |
| SPI, I2C, UART 통신용 핀 | — |

### GPIO Pinout (RPi 3 / 4 동일)

| Functions | GPIO | Pin | Pin | GPIO | Functions |
|---|---|---|---|---|---|
| | 3.3V | 1 | 2 | 5V | |
| **SDA1 (I²C)** | **GPIO2** | 3 | 4 | 5V | |
| **SCL1 (I²C)** | **GPIO3** | 5 | 6 | GND | |
| GCLK | GPIO4 | 7 | 8 | GPIO14 | TXD0 (UART) |
| | GND | 9 | 10 | GPIO15 | RXD0 (UART) |
| | GPIO17 | 11 | 12 | **GPIO18** | **PWM0**, CLK (PCM) |
| | GPIO27 | 13 | 14 | GND | |
| | GPIO22 | 15 | 16 | GPIO23 | |
| | 3.3V | 17 | 18 | GPIO24 | |
| **MOSI (SPI)** | **GPIO10** | 19 | 20 | GND | |
| **MISO (SPI)** | **GPIO9** | 21 | 22 | GPIO25 | |
| **SCLK (SPI)** | **GPIO11** | 23 | 24 | **GPIO8** | **CE0 (SPI)** |
| | GND | 25 | 26 | GPIO7 | CE1 (SPI) |
| | ID_SD | 27 | 28 | ID_SC | |
| | GPIO5 | 29 | 30 | GND | |
| | GPIO6 | 31 | 32 | GPIO12 | PWM0 |
| PWM1 | GPIO13 | 33 | 34 | GND | |
| FS (PCM), PWM1 | GPIO19 | 35 | 36 | GPIO16 | |
| | GPIO26 | 37 | 38 | GPIO20 | DIN (PCM) |
| | GND | 39 | 40 | GPIO21 | DOUT (PCM) |

{: .시험 }
> **반드시 외울 핀**
>
> - **I2C**: SDA = **GPIO2**, SCL = **GPIO3**
> - **SPI**: MOSI = **GPIO10**, MISO = **GPIO9**, SCLK = **GPIO11**, CE0 = **GPIO8**
> - **PWM**: **GPIO18** (실습에서 항상 사용)
> - **UART**: TXD = GPIO14, RXD = GPIO15

### 핀 번호 모드

| 모드 | 의미 |
|---|---|
| `GPIO.BOARD` | **순서대로 나열된 물리 핀 번호** 사용 (1~40) |
| `GPIO.BCM` | **미리 정의된 GPIO 핀 번호** 사용 (GPIO4, GPIO18 …) |

{: .중요 }
> 5강의 **모든 실습은 `GPIO.BCM` 모드**를 사용한다. (3강의 첫 LED 예제만 BOARD 모드)

### 참고 용어

| 용어 | 의미 |
|---|---|
| **Vcc** (collector 전원), **Vdd** (drain 전원) | **+ 전원** |
| **Vee** (emitter 전원), **Vss** (source 전원) | **− 전원 또는 접지(GND)** |

---

## RPi.GPIO 기본 사용법

**RPi.GPIO**: 파이썬에서 라즈베리파이의 GPIO를 제어하기 위한 모듈. **Raspberry Pi OS에 기본 설치**되어 있어 따로 설치할 필요 없음.

```python
#-*-coding:utf-8-*-        # 한글 주석을 쓰려면 최상단에 추가
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)              # 불필요한 warning 제거
GPIO.setmode(GPIO.BCM)               # 핀 번호 모드 (BOARD / BCM)

GPIO.setup(channel, GPIO.OUT)        # 출력으로 설정
GPIO.setup(channel, GPIO.IN)         # 입력으로 설정

GPIO.output(channel, 1)              # 3.3V 출력 (High)
GPIO.output(channel, 0)              # 0V 출력 (Low)

value = GPIO.input(channel)          # 입력 읽기

time.sleep(delay)                    # delay 초 대기

GPIO.cleanup()                       # GPIO 설정 초기화
```

{: .중요 }
> **`GPIO.cleanup()`의 목적**: 리소스를 반환시켜 **중복 사용이나 GPIO 핀 쇼트 등의 하드웨어적 문제를 방지**

### 전압 ↔ 파이썬 표현

| 전압 | 파이썬 코드 표현 |
|---|---|
| **3.3V** | `GPIO.HIGH`, `True`, `1` |
| **0V** | `GPIO.LOW`, `False`, `0` |

---

## [실습 1] LED 켜고 끄기

### 배선

준비물: **1kΩ 저항, LED**

| 라즈베리파이 | LED |
|---|---|
| **GPIO 4** | **+ 극** |
| **GND** | **− 극** |

### 코드 (LED_Blink.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀 번호 설정 (BCM 모드)
led_pin = 4                      # GPIO 4

GPIO.setwarnings(False)          # 불필요한 warning 제거
GPIO.setmode(GPIO.BCM)           # GPIO 핀 번호 모드 설정
GPIO.setup(led_pin, GPIO.OUT)    # LED 핀을 출력으로 설정

for i in range(10):              # 10번 반복
    GPIO.output(led_pin, 1)      # LED 켜짐
    time.sleep(1)                # 1초 대기
    GPIO.output(led_pin, 0)      # LED 꺼짐
    time.sleep(1)                # 1초 대기

GPIO.cleanup()                   # GPIO 설정 초기화
```

```bash
$ python LED_Blink.py
```

→ LED가 **1초 간격으로 10번** 깜빡임

---

## [실습 2] 버튼 입력 — Polling 방식

### Floating 상태

{: .중요 }
> **Floating**: 스위치를 누르지 않았을 때 핀에 0V도 3.3V도 아닌, **부유하는 애매한 값**이 입력되는 상태

- 스위치를 누르면 → GPIO 15에 **3.3V(High, 1)** 입력
- 스위치를 안 누르면 → **floating 상태 발생**

### 해결책: Pull-down / Pull-up

| | Pull-**down** | Pull-**up** |
|---|---|---|
| 저항 위치 | 스위치 기준 **GND(−극, 0V)쪽** | 스위치 기준 **Vcc(+전원)쪽** |
| 역할 | 전압을 안정적으로 **Low(0V)로 끌어내림** | 전압을 안정적으로 **High(3.3V)로 끌어올림** |
| 안 눌렀을 때 | **0V (Low, 0)** | **3.3V (High, 1)** |
| 눌렀을 때 | **3.3V (High, 1)** | **0V (Low, 0)** |
| 저항값 | 일반적으로 **10kΩ** | 일반적으로 **10kΩ** |

{: .시험 }
> **라즈베리파이는 내부에 pull-up / pull-down 저항이 내장**되어 있어 별도 저항 설치 없이 `GPIO.setup()`에서 설정 가능하다. (아두이노는 외부 저항이 필요)

```python
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # pull-up 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # pull-down 설정
```

### 배선

| 라즈베리파이 | Tact 스위치 |
|---|---|
| **GPIO 15** | 핀 연결 |
| **VCC (3.3V)** | 핀 연결 |

### 코드 (Btn_Polling.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

button_pin = 15                  # GPIO 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 입력으로 설정하고 pull-down 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:                         # 무한루프 (polling 방식)
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")
    time.sleep(0.1)              # 0.1초 기다림

GPIO.cleanup()
```

**Polling 방식**
: 계속해서 **주기적으로 상태를 확인**하면서 조건이 만족될 때 처리하는 방식

---

## [실습 3] 버튼 입력 — Event handling 방식

**Event handling 방식**
: **Event가 발생했을 때** 미리 정의해둔 함수(**callback 함수**)를 수행하는 방식

```python
GPIO.add_event_detect(button_pin, GPIO.RISING,
                      callback=button_callback, bouncetime=300)
```

| 인자 | 의미 |
|---|---|
| `GPIO.RISING` | 입력이 **0V(0) → 3.3V(1)로 변할 때** (rising event) |
| `callback=` | event 발생 시 실행할 **callback 함수** |
| `bouncetime=` | **bouncing 방지 지연시간 (ms)** |

### Bouncing 현상

{: .시험 }
> **Bouncing**: 실제로 버튼이 동작할 때 **순간적으로 전압이 불규칙해지는 현상**
>
> → bouncing되는 전압을 무시하기 위해 **ms 단위의 bounce time(지연시간)** 을 설정하여, 이 시간 뒤에 event를 감지하도록 하여 **잘못된 전압 입력을 방지**한다.
>
> 예: `bouncetime=300` → 버튼을 눌러 RISING event로 callback이 실행되면, **300ms(0.3초) 뒤**에야 다시 event를 감지

### 배선 (버튼으로 LED 토글)

준비물: Tact 스위치, 1kΩ 저항, LED

| 라즈베리파이 | 전자부품 |
|---|---|
| **GPIO 15** | 스위치 연결 |
| **VCC (3.3V)** | 스위치 연결 |
| **GPIO 4** | 저항 |
| **GND** | LED − 극 |

### 코드 (Btn_callbak.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

button_pin = 15
led_pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

light_on = False                 # boolean 변수 설정

def button_callback(channel):
    global light_on              # 함수 내에서 수정하기 위해 global 선언
    if light_on == False:        # LED가 꺼져 있을 때
        GPIO.output(led_pin, 1)  # LED 켬
        print("LED ON!")
    else:                        # LED가 켜져 있을 때
        GPIO.output(led_pin, 0)  # LED 끔
        print("LED OFF!")
    light_on = not light_on      # False <=> True swapping

# rising event 감지 시 button_callback 실행, bounce time 300ms
GPIO.add_event_detect(button_pin, GPIO.RISING,
                      callback=button_callback, bouncetime=300)

while 1:                         # 프로그램을 종료시키지 않기 위한 무한루프
    time.sleep(0.1)

GPIO.cleanup()
```

→ 버튼을 누르면 LED가 켜지고, 다음 번 누르면 꺼짐

{: .중요 }
> callback 함수 안에서 바깥 변수를 수정하려면 **`global` 선언이 반드시 필요**하다.

---

## PWM (Pulse Width Modulation)

**PWM**: 주기적으로 반복되는 디지털 신호인 **on 신호(1; 3.3V)와 off 신호(0; 0V)** 를 통해서 **모터·팬의 속도, LED 등의 밝기를 제어**

- **주파수(frequency)**: 1Hz는 1초에 1번, 2Hz는 1초에 2번 주기적 현상이 일어나는 것
- **Duty cycle**: 반복되는 pulse 신호의 주기에서 **on 신호가 지속되는 시간의 비율**

{: .시험 }
> **Duty cycle이 클수록 팬 속도와 LED의 밝기가 증가**한다.

### PWM 라이브러리 사용법

```python
p = GPIO.PWM(channel, frequency)   # PWM 인스턴스 생성 (핀번호, 주파수 Hz)
p.start(dc)                        # 초기 duty cycle 설정하며 PWM 시작
p.ChangeDutyCycle(dc)              # duty cycle 변경 (0 <= dc <= 100.0)
p.ChangeFrequency(freq)            # 주파수 변경
p.stop()                           # PWM 종료
```

---

## [실습 4] PWM으로 LED 밝기 조정

### 배선

| 라즈베리파이 | LED |
|---|---|
| **GPIO 18 (PWM)** | **+ 극** |
| **GND** | **− 극** |

### 코드 (PWM_LED.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

led_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

p = GPIO.PWM(led_pin, 50)        # GPIO 18, 주파수 50Hz
p.start(0)                       # duty cycle 0으로 PWM 시작

try:
    while 1:
        for dc in range(0, 101, 5):      # 0 → 100, 5씩 증가
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):    # 100 → 0, 5씩 감소
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:        # Ctrl+C 눌렀을 때 예외 발생
    pass

p.stop()                         # PWM 종료
GPIO.cleanup()                   # GPIO 설정 초기화
```

→ LED가 **밝아졌다 어두워지는 것을 반복**

---

## [실습 5] PWM으로 부저 음 조정

### 부저의 종류

| 종류 | 동작 |
|---|---|
| **Active** | **일정한 전원(3.3V)만 가해주면 소리가 남** |
| **Passive** | 전원만으로는 소리가 안 나고 **일정한 주파수를 가해줘야** 소리가 남. **주파수 높낮이로 음 조정 가능** |

### 배선

| 라즈베리파이 | 부저 |
|---|---|
| **VCC (3.3V)** | + 극 |
| **GPIO 18** | I/O |
| **GND (0V, −극)** | GND |

### 코드 (PWM_Buzzer.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

bz_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(bz_pin, GPIO.OUT)

p = GPIO.PWM(bz_pin, 100)        # GPIO 18, 주파수 100Hz

# 4옥타브 도~시, 5옥타브 도의 주파수
Frq = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5                      # 음과 음 사이 연주 시간 (0.5초)

p.start(10)                      # duty cycle 10으로 PWM 시작

try:
    while 1:
        for fr in Frq:
            p.ChangeFrequency(fr)    # 주파수 변경
            time.sleep(speed)        # 0.5초 딜레이
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
```

{: .시험 }
> **음계 주파수 (4옥타브 도 ~ 5옥타브 도)**
>
> | 도 | 레 | 미 | 파 | 솔 | 라 | 시 | 도(5옥타브) |
> |---|---|---|---|---|---|---|---|
> | 262 | 294 | 330 | 349 | 392 | 440 | 493 | 523 |
>
> 음 높이는 `ChangeDutyCycle`이 아니라 **`ChangeFrequency`로 조정**한다.

---

## [실습 6] PWM으로 서보모터 각도 조정

**서보모터는 duty cycle에 따라 각도가 변경**된다.

{: .중요 }
> | 각도 | Duty cycle |
> |---|---|
> | **0°** | **2.5** |
> | **90°** | **7.5** |
> | **180°** | **12.5** |

### 배선 (SG-90)

| 라즈베리파이 | SG-90 서보모터 |
|---|---|
| **VCC (5V)** | **빨간색** |
| **GPIO 18** | **오렌지색** |
| **GND (0V, −극)** | **갈색** |

### 코드 (PWM_Servo.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # 주파수 50Hz
servo.start(0)                   # duty cycle 0으로 PWM 시작

try:
    while True:
        servo.ChangeDutyCycle(7.5)      # 90도
        time.sleep(1)
        servo.ChangeDutyCycle(12.5)     # 180도
        time.sleep(1)
        servo.ChangeDutyCycle(2.5)      # 0도
        time.sleep(1)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
```

{: .참고 }
> LED 밝기 조정과 서보모터는 둘 다 **주파수 50Hz**, 부저는 **100Hz**로 시작한다.

---

## [실습 7] 초음파 센서 (HC-SR04)

### 동작 원리

1. **Trigger 핀에 10μs 동안 start pulse 신호**를 준다
2. 초음파 센서가 **8개의 사운드 웨이브**를 전방으로 발사
3. 물체에 반사되어 돌아오는 **시간만큼 Echo 핀으로 pulse 신호**를 보냄

### 거리 계산

{: .시험 }
> **초음파의 속도는 340m/s로 일정**
>
> ```
> 물체와의 거리 = 소리의 속도 × (걸린 시간 / 2)
> ```
>
> **예제**: 걸린 시간이 588μs일 때
>
> ```
> = 340 m/s × (588μs / 2)
> = 34000 cm/s × (0.000588s / 2)
> = 9.996 cm
> ```
>
> 왕복 시간이므로 **÷2 를 빼먹지 말 것**

### 데이터시트

- **측정 거리: 2 ~ 400cm**
- **전방 15도 각도 이내** 측정 가능

### 배선

준비물: HC-SR04, **1kΩ 저항, 2kΩ 저항**

| 라즈베리파이 | 초음파 센서 |
|---|---|
| **VCC (5V)** | VCC |
| **GPIO 23** | **Trigger 핀** |
| **GPIO 24** | **Echo 핀** |
| **GND (0V, −극)** | GND |

### 5V를 3.3V로 낮추기 (전압 분배)

{: .중요 }
> **라즈베리파이의 GPIO 핀은 3.3V 이상 입력하면 안 된다.**
> HC-SR04는 **5V로 동작**하므로 Echo 핀의 5V 신호를 **전압 분배 회로로 3.3V로 낮춰서** 입력받아야 한다.

```
회로에 흐르는 전류
  5V = (1000Ω + 2000Ω) × I
  I  = 5V / 3000Ω = 0.00166667 A

Vout
  Vout = 5V − (1000Ω × 0.00166667A) = 3.33333 V
```

### 코드 (HC_SR04.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance measurement in process")

GPIO.setup(TRIG, GPIO.OUT)       # trigger 핀은 출력
GPIO.setup(ECHO, GPIO.IN)        # echo 핀은 입력

GPIO.output(TRIG, False)         # trigger 핀 0V 출력
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)          # 초음파 발사
        time.sleep(0.00001)              # 10us 기다림
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == False: # echo 핀에 0V가 입력되는 동안
            start = time.time()
        while GPIO.input(ECHO) == True:  # echo 핀에 3.3V가 입력되는 동안(초음파 수신)
            stop = time.time()

        check_time = stop - start             # 발사 → 수신까지 걸린 시간
        distance = check_time * 34000 / 2     # 거리 계산 (cm)
        print("Distance : %.1f cm" % (distance))

        time.sleep(0.4)                       # 0.4초 간격 측정
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
```

{: .참고 }
> `time.time()` 은 **1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초 단위로 반환**한다.
> `distance = check_time * 34000 / 2` 에서 **34000은 cm/s 단위의 음속**이다.

---

## [실습 8] PIR 인체감지 센서 (HC-SR501)

**PIR (Passive InfraRed) 센서**: **적외선을 통해 사람의 움직임을 감지**하는 센서

- 감지 각도 범위 안에 **적외선의 변화가 있으면 3.3V(High, 1)**, **없으면 0V(Low, 0)** 출력
- 예: 복도나 현관문 천장 조명에 설치되어 **움직임 감지 시 자동으로 조명을 켬**

| 설정 | 범위 |
|---|---|
| **감지 범위** | **3m ~ 7m** |
| **지연 시간** | High 신호 감지 후 **상태 유지 시간** (0.3s ~ 5m) |

{: .주의 }
> 실습 시 **지연 시간 값을 최소로 설정**하여 사람의 움직임을 신속히 감지하도록 한다.

### 배선

준비물: HC-SR501, 1kΩ 저항 2개, 노란색 LED, 빨간색 LED

| 라즈베리파이 | 부품 |
|---|---|
| **VCC (5V)** | PIR 센서 VCC |
| **GPIO 4** | PIR 센서 **Out** (3.3V 또는 0V) |
| **GPIO 20** | LED(red) + |
| **GPIO 21** | LED(yellow) + |
| **GND (0V, −극)** | GND |

### 코드 (HC_SR501.py)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

led_R = 20
led_Y = 21
sensor = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_Y, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)      # PIR 센서는 입력

print("PIR Ready ....")
time.sleep(5)                    # PIR 센서 준비 시간

try:
    while True:
        # 움직임 감지 → 센서가 3.3V(1) 출력
        if GPIO.input(sensor) == 1:
            GPIO.output(led_Y, 1)        # 노란색 LED 켬
            GPIO.output(led_R, 0)        # 빨간색 LED 끔
            print("Motion Detected !")
            time.sleep(0.2)

        # 미감지 → 센서가 0V(0) 출력
        if GPIO.input(sensor) == 0:
            GPIO.output(led_R, 1)        # 빨간색 LED 켬
            GPIO.output(led_Y, 0)        # 노란색 LED 끔
            print("Motion Not Detected !")
            time.sleep(0.2)
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()
```

---

## ADC (Analog to Digital Converter)

| 신호 | 설명 | 예 |
|---|---|---|
| **아날로그 신호** | 길이·각도·전압처럼 **외부 원인에 의해 연속적으로 변하는** 물리량 | 속도계 바늘 각도, 수은주 온도계, LP 음반 |
| **디지털 신호** | 데이터를 **0 또는 1**로 표현 | |

**ADC**: 아날로그 신호를 디지털 신호로 변환하는 전자회로

{: .중요 }
> **라즈베리파이는 ADC 기능이 있는 GPIO 핀이 없으며 디지털 입력만 가능하다.**
> 따라서 아날로그 값을 입력받으려면 **별도의 ADC 칩(MCP3008)** 으로 디지털 변환 후 입력받아야 한다.

### MCP3008

- ADC 기능을 하는 칩. 아날로그 전압값을 디지털로 변환
- 변환된 값을 **SPI 통신으로 마스터 장치(라즈베리파이/아두이노)에 전송**
- **8개의 아날로그 입력 채널 (CH0 ~ CH7)**
- **해상도(resolution): 10bits** → 2¹⁰ = **1024개의 디지털 값 (0 ~ 1023)**

#### 주요 핀

| 핀 | 역할 |
|---|---|
| **VDD** | 칩의 전원 전압 (+2.7V ~ 5.5V) |
| **VREF** | ADC를 위한 **기준 전압(reference voltage)**. 이 전압을 기준으로 디지털 값 계산 |
| **CLK** | 마스터로부터 **동기 신호(serial clock)** 를 받는 핀 |
| **DOUT** | 마스터로 **데이터를 보내는(data out)** 핀 |
| **DIN** | 마스터로부터 **데이터를 받는(data in)** 핀 |
| **CS** | 마스터로부터 slave로 선택받기 위한 **chip select 신호**를 받는 핀 |
| **AGND / DGND** | **아날로그 영역의 ground / 디지털 영역의 ground** |

### 변환 공식

{: .시험 }
> ```
> 디지털 전압값  = (아날로그 전압값 / VREF) × 1023
> 아날로그 전압값 = (디지털 전압값 × 3.3) / 1023
> ```
>
> VREF = 3.3V 기준 변환표
>
> | 아날로그 입력 | 디지털 값 |
> |---|---|
> | 0.00V | 0 |
> | 0.25V | 78 |
> | 0.50V | 155 |
> | 0.75V | 233 |
> | 1.00V | 310 |
> | **1.50V** | **465** |
> | 2.50V | 775 |
> | **3.30V** | **1023** |

---

## SPI (Serial Peripheral Interface) 통신

**마스터(master)와 슬레이브(slave) 장치 간의 동기식 직렬 통신 방식**

| 역할 | 장치 |
|---|---|
| **마스터** | 라즈베리파이, 아두이노 |
| **슬레이브** | ADC(MCP3008), 센서, 플래시 메모리, RTC(real time clock) |

### 직렬 vs 병렬

| | 설명 |
|---|---|
| **직렬 통신** | 데이터 전송 시 **한 번에 한 비트씩** 전송 |
| **병렬 통신** | 데이터 전송 시 **한 번에 여러 비트** 전송 |

### 비동기식 vs 동기식 직렬 통신

| | 설명 |
|---|---|
| **비동기식** | 송신자와 수신자가 서로 알 수 없는 상태 → 1 byte 전송 전에 **start bit**, 끝낸 후 **stop bit** 필요. 서로 **같은 속도**로 전송 |
| **동기식** | 데이터와 함께 **별도의 동기 신호(CLOCK)** 를 보냄. **데이터선 + CLOCK 신호선** 필요. 수신자가 **정확한 시간에 0/1 비트값을 읽을 수 있음** |

### SPI 신호선 4개

{: .시험 }
> | 신호선 | Full name | 방향 |
> |---|---|---|
> | **MISO** | **M**aster **I**n **S**lave **O**ut | 슬레이브 → 마스터 |
> | **MOSI** | **M**aster **O**ut **S**lave **I**n | 마스터 → 슬레이브 |
> | **SCLK** | **S**erial **CL**oc**K** | 마스터 → 슬레이브 (동기 신호) |
> | **CS / SS** | **C**hip **S**elect / **S**lave **S**elect | 슬레이브를 선택 |

### 통신 순서

```
마스터가 슬레이브로 CS 신호를 보냄
   ↓
마스터가 슬레이브에게 SCLK 신호를 보냄
   ↓
마스터와 슬레이브가 shift register(8bit)에 데이터를 담아
MOSI와 MISO 라인을 통해 데이터 통신
```

---

## [실습 9] 아날로그 전압을 MCP3008로 읽기

### SPI 활성화

GUI: `시작 메뉴 > 기본설정 > Raspberry Pi Configuration > Interfaces` → **SPI Enable** → 재부팅

터미널:

```bash
$ sudo raspi-config
```

→ **3 Interface Options** → **SPI** → **Yes** → OK → Finish

```bash
$ sudo reboot
```

### SPI 라이브러리 설치

```bash
# 모든 사용자가 사용 가능하도록 설치
$ sudo apt-get install python3-spidev
```

```bash
# 가상환경에 설치하는 경우
$ mkdir SPI
$ cd SPI
$ python3 -m venv .venv            # 가상환경 생성
$ source .venv/bin/activate        # 가상환경 활성화
$ pip3 install spidev              # 모듈 설치
$ deactivate                       # 가상환경 비활성화
```

```bash
# 가상환경에서 실행
$ cd SPI
$ source .venv/bin/activate
$ python MCP_3008.py
$ deactivate
```

### 가변저항 (potentiometer, POT)

- 내부에 **저항 물질이 둥글게** 자리잡고 있고, 손잡이를 돌리면 **다이얼 와이퍼가 회전**
- 와이퍼가 **1번 다리에 가까울수록** 1-2번 사이 저항은 **감소**, 2-3번 사이 저항은 **증가**
- 보통 **1번과 3번에 GND와 전원**을 연결하고, 와이퍼 회전에 따라 **2번 다리의 전압이 0V~3.3V(또는 5V)로 변함**

### 배선

| 라즈베리파이 | MCP3008 |
|---|---|
| **3.3V** | **VREF, VDD** |
| **GND** | **AGND, DGND** |
| **GPIO 11 (SCLK)** | **CLK** |
| **GPIO 9 (MISO)** | **DOUT** |
| **GPIO 10 (MOSI)** | **DIN** |
| **GPIO 8 (CS)** | **CS** |

{: .시험 }
> **MISO ↔ DOUT**, **MOSI ↔ DIN** 으로 **교차**된다는 점이 핵심.
> (마스터의 "들어옴"이 슬레이브의 "나감"과 연결)

### 코드 (MCP_3008.py)

```python
#-*-coding:utf-8-*-
import spidev
import time

delay = 0.5                      # 센서 측정 간격
pot_channel = 0                  # MCP3008 중 센서에 연결한 채널

spi = spidev.SpiDev()            # SPI 인스턴스 생성
spi.open(0, 0)                   # SPI 통신 시작
spi.max_speed_hz = 100000        # SPI 통신 속도 설정

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    pot_value = readadc(pot_channel)
    print("-----------------------------")
    print("POT Value: %d" % (pot_value))
    time.sleep(delay)
```

{: .중요 }
> **`readadc()` 해설** — 실기에서 그대로 쳐야 하는 부분
>
> - `r[0]`은 **무시**
> - `r[1]`의 **하위 2비트** → ADC 값의 **상위 2비트**
> - `r[2]`의 **8비트** → ADC 데이터의 **하위 8비트**
> - 둘을 합쳐 **총 10비트** 데이터가 최종 ADC 값
>
> `data = ((r[1] & 3) << 8) + r[2]`
> → `& 3` 으로 하위 2비트만 남기고, `<< 8` 로 8칸 왼쪽 이동한 뒤 `r[2]`를 더한다.

### 파이썬 비트 연산 정리

```python
>>> 0b0011 << 2        # shift 연산
12
>>> 3 << 2             # 내부적으로 이진수로 변환하여 shift
12
>>> bin(12)
'0b1100'

>>> bin(0b1101 & 0b1001)    # 비트 AND
'0b1001'
>>> 13 & 9
9

>>> bin(0b1101 | 0b1001)    # 비트 OR
'0b1101'
>>> 13 | 9
13

>>> bin(0b1101 ^ 0b1001)    # 비트 XOR
'0b100'
>>> 13 ^ 9
4

>>> bin(~0b1101)            # 비트 NOT
'-0b1110'
>>> ~13
-14
```

---

## [실습 10] LDR 조도 센서

**LDR (Light Dependent Resistor)**: **빛의 세기에 따라 저항값이 달라지는** 조도 센서

{: .시험 }
> | 주위 환경 | 저항값 | 전류 | 출력 전압 |
> |---|---|---|---|
> | **밝음** | **감소** | 많이 흐름 | **높아짐** |
> | **어두움** | **증가** | 적게 흐름 | **낮아짐** |

- **10kΩ pull-down 저항**을 사용하여 출력 전압에 입력되는 **내부 잡음을 흡수**
- 이 저항이 없으면 **어두운 곳에서도 출력 전압이 정상적으로 낮아지지 않음**
- pull-down 저항은 **GND에 연결되는 저항**이고, GND(−극, 0V)는 전류가 +극에서 −극으로 흐르도록 **경로를 제공**

### 배선

준비물: MCP3008, 10kΩ 저항, LDR 센서 (MCP3008 ↔ RPi 배선은 실습 9와 동일)

### 코드 (LDR.py)

실습 9의 `MCP_3008.py`와 **구조가 완전히 동일**하고 변수명만 다르다.

```python
#-*-coding:utf-8-*-
import spidev
import time

delay = 0.5
ldr_channel = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    ldr_value = readadc(ldr_channel)
    print("-----------------------------")
    print("LDR Value: %d" % (ldr_value))
    time.sleep(delay)
```

---

## [실습 11] 조이스틱

- **X축과 Y축 움직임에 따라 저항값이 변하는 가변저항**이 달려 있어 움직임이나 방향을 표현
- **수직으로 누르면 스위치 기능**도 가능

{: .중요 }
> **10kΩ pull-up 저항 사용**
>
> - 수직으로 **눌렀을 때** SW 핀 출력 전압 = **0V**
> - **누르지 않았을 때** SW 핀 출력 전압 = **3.3V**
> - 저항이 없으면 누르지 않았을 때 출력이 3.3V가 아닌 값이 될 수 있음

### 배선

| 라즈베리파이 | 조이스틱 모듈 |
|---|---|
| GND | GND |
| 3.3V | + |

| MCP3008 | 조이스틱 모듈 |
|---|---|
| **CH2** | **VRx** |
| **CH1** | **VRy** |
| **CH0** | **SW** |

### 코드 (Joystick.py)

```python
#-*-coding:utf-8-*-
import spidev
import time

delay = 0.5

# MCP3008 채널 설정
sw_channel  = 0
vrx_channel = 2
vry_channel = 1

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    sw_val  = readadc(sw_channel)
    vrx_pos = readadc(vrx_channel)
    vry_pos = readadc(vry_channel)

    print("X : {}, Y: {}, SW: {}".format(vrx_pos, vry_pos, sw_val))
    time.sleep(delay)
```

---

## I2C 통신

**I2C (Inter-Integrated Circuit, 아이-스퀘어-씨)**: SPI처럼 **동기식 직렬 통신**

### SPI와의 차이

{: .시험 }
> | | **SPI** | **I2C** |
> |---|---|---|
> | 통신 라인 | MISO, MOSI, SCLK, **CS** (4개) | **SDA, SCL** (2개) |
> | 슬레이브 추가 시 | **슬레이브마다 CS 라인 필요** | **CS 라인 불필요** |
> | 동시 연결 | 제한적 | **동시에 많은 슬레이브 연결 가능** |
> | 속도 | 빠름 | **느림** → 보통 **저속 주변장치** 통신에 사용 |

- **SDA (Serial Data Line)** = **GPIO 2**
- **SCL (Serial Clock Line)** = **GPIO 3**

### Pull-up 저항

- 전압을 안정적으로 **High(3.3V)로 끌어올리기 위해** 사용
- **라즈베리파이는 내부적으로 SDA와 SCL에 이미 pull-up 저항이 장착**되어 있으므로 추가 장착 불필요

### I2C 활성화

GUI: `시작 메뉴 > 기본설정 > Raspberry Pi Configuration > Interfaces` → **I2C Enable** → 재부팅

터미널:

```bash
$ sudo raspi-config
```

→ **3 Interface Options** → I2C → Yes → OK → Finish

```bash
$ reboot
$ ls /dev/i2c*         # I2C 디바이스 파일(/dev/i2c-1) 존재 확인
```

---

## [실습 12] OLED 디스플레이 (I2C)

**OLED 128×64 I2C**

- I2C 통신 방식의 작은 OLED 디스플레이 모듈
- 해상도 **128 × 64 픽셀**, **SSD1306 드라이버** 내장

### 배선

| 라즈베리파이 | OLED 모듈 |
|---|---|
| GND | GND |
| **VCC (3.3V)** | **VDD** |
| **SCL (GPIO3)** | **SCK** |
| **SDA (GPIO2)** | **SDA** |

### 연결 확인

```bash
$ i2cdetect -y 1
```

{: .중요 }
> 정상적으로 연결되었다면 **OLED의 I2C 주소인 `0x3c`** 가 표시된다.

### 라이브러리 설치

```bash
$ mkdir OLED
$ cd OLED
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install adafruit-circuitpython-ssd1306
$ pip3 install spidev
$ pip3 install pillow
$ deactivate
```

### 코드 (OLED_MCP3008_joystick.py)

```python
#-*-coding:utf-8-*-
import time
import spidev
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
from board import SCL, SDA
import busio

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

# MCP3008 채널 설정
sw_channel  = 0
vrx_channel = 2
vry_channel = 1

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

# I2C interface 생성
i2c = busio.I2C(SCL, SDA)

# 해상도 128 x 64 픽셀인 SSD1306 OLED 인스턴스 생성
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)                  # OLED 화면 초기화
display.show()                   # 갱신된 픽셀들로 화면 보여줌

# 출력할 직사각형과 문자열의 left top corner 위치
x = 0
padding = -2
y = padding

font = ImageFont.load_default()  # 폰트 설정

# mode('1': 흑백화면)과 크기로 이미지 생성
width  = display.width
height = display.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)     # 이미지상에 그리기를 수행할 object 생성

# 직사각형 그리기 (0: 검정색, 255: 흰색)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

while True:
    sw_val  = readadc(sw_channel)
    vrx_pos = readadc(vrx_channel)
    vry_pos = readadc(vry_channel)

    # 모니터 화면 출력
    print('Switch = {0:0.2f}'.format(sw_val))
    print('X-axis = {0:0.2f}'.format(vrx_pos))
    print('Y-axis = {0:0.2f}'.format(vry_pos))

    # OLED 화면 출력
    draw.text((x, y),    ' Switch = {0:0.2f}'.format(sw_val),  font=font, fill=255)
    draw.text((x, y+8),  ' X-axis = {0:0.2f}'.format(vrx_pos), font=font, fill=255)
    draw.text((x, y+16), ' Y-axis = {0:0.2f}'.format(vry_pos), font=font, fill=255)

    display.image(image)         # 갱신된 픽셀들로 구성된 화면 보여줌
    display.show()

    time.sleep(0.5)
```

{: .참고 }
> **OLED 그리기 흐름**
> `Image.new` → `ImageDraw.Draw` → `draw.text` / `draw.rectangle` → `display.image(image)` → `display.show()`
>
> `fill=255`는 흰색(켜짐), `fill=0`은 검정색(꺼짐).
