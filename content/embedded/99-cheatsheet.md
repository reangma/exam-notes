# 실기 치트시트

시험장에서 **머리에서 바로 꺼내 써야 하는 것**만 모았습니다.

## 1. 기본 템플릿 (이것만 외우면 절반)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

PIN = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN, 1)
        time.sleep(1)
        GPIO.output(PIN, 0)
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
```

{: .중요 }
> 순서는 항상 **setwarnings → setmode → setup → (동작) → cleanup**.
> `try/except KeyboardInterrupt`로 감싸야 Ctrl+C 로 깔끔히 빠져나온다.

---

## 2. 입력 (버튼)

### Polling

```python
GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
    if GPIO.input(BTN) == GPIO.HIGH:
        print("Button pushed!")
    time.sleep(0.1)
```

### Event handling

```python
def button_callback(channel):
    global light_on
    ...

GPIO.add_event_detect(BTN, GPIO.RISING,
                      callback=button_callback, bouncetime=300)

while 1:
    time.sleep(0.1)
```

| | pull-down | pull-up |
|---|---|---|
| 안 누름 | **0** | **1** |
| 누름 | **1** | **0** |

---

## 3. PWM

```python
p = GPIO.PWM(18, 50)        # 핀, 주파수(Hz)
p.start(0)                  # 초기 duty cycle
p.ChangeDutyCycle(dc)       # 0 ~ 100
p.ChangeFrequency(freq)
p.stop()
```

| 용도 | 핀 | 주파수 | 조정 대상 |
|---|---|---|---|
| LED 밝기 | GPIO 18 | **50Hz** | **Duty cycle** |
| 부저 음 | GPIO 18 | **100Hz** 시작 | **Frequency** |
| 서보 각도 | GPIO 18 | **50Hz** | **Duty cycle** |

**서보 각도** — 0° = **2.5**, 90° = **7.5**, 180° = **12.5**

**음계** — 262, 294, 330, 349, 392, 440, 493, 523 (도레미파솔라시도)

---

## 4. SPI / MCP3008

```python
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
```

{: .시험 }
> `readadc`는 **토씨 하나 안 틀리고** 쓸 수 있어야 한다. 실습 9~12에 전부 똑같이 등장한다.

---

## 5. 핀 번호 (BCM)

| 용도 | 핀 |
|---|---|
| **I2C** | SDA = **GPIO2**, SCL = **GPIO3** |
| **SPI** | MOSI = **GPIO10**, MISO = **GPIO9**, SCLK = **GPIO11**, CE0 = **GPIO8** |
| **PWM** | **GPIO18** |
| **UART** | TXD = GPIO14, RXD = GPIO15 |

### 실습별 사용 핀

| 실습 | 핀 |
|---|---|
| LED Blink | GPIO 4 |
| 버튼 | GPIO 15 (+ LED GPIO 4) |
| PWM 전부 | GPIO 18 |
| 초음파 HC-SR04 | TRIG **23**, ECHO **24** |
| PIR HC-SR501 | 센서 **4**, LED R **20**, LED Y **21** |

---

## 6. 계산 공식

| 항목 | 공식 |
|---|---|
| 옴의 법칙 | `V = I × R` |
| 직렬 합성저항 | `Rt = R1 + R2` |
| 병렬 합성저항 | `1/R = 1/R1 + 1/R2` |
| LED 보호저항 | `R = (전원V − V_F) / I_F` → 5V·2V·20mA 면 **150Ω** |
| 초음파 거리 | `거리 = 34000(cm/s) × 걸린시간 / 2` |
| 전압 분배 (5V→3.3V) | 1kΩ + 2kΩ, `Vout = 5 − 1000 × (5/3000) = 3.33V` |
| ADC → 전압 | `아날로그 = (디지털 × 3.3) / 1023` |
| 전압 → ADC | `디지털 = (아날로그 / 3.3) × 1023` |

---

## 7. 자주 쓰는 리눅스 명령어

```bash
$ sudo apt-get update && sudo apt-get upgrade   # 패키지 업데이트
$ sudo raspi-config                             # SPI / I2C / VNC 활성화
$ sudo reboot

$ mkdir -p webapps/ch01                         # 하위 디렉토리까지 생성
$ rm -rf dir                                    # 디렉토리 삭제
$ cp -r src dst                                 # 디렉토리 복사
$ tail -f log.txt                               # 실시간 로그
$ ps -ef                                        # 전체 프로세스
$ kill -9 PID                                   # 강제 종료

$ ls /dev/i2c*                                  # I2C 디바이스 확인
$ i2cdetect -y 1                                # I2C 주소 확인 (OLED = 0x3c)
$ python LED_Blink.py                           # 실행
```

### 가상환경

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install spidev
$ deactivate
```

---

## 8. 자주 틀리는 것

{: .주의 }
> - **BOARD vs BCM** — 5강 실습은 전부 **BCM**
> - 초음파 거리에서 **÷2 빠뜨림**
> - **MISO↔DOUT, MOSI↔DIN** 교차 연결
> - `GPIO.cleanup()` 빠뜨림
> - callback 함수 안 **`global` 빠뜨림**
> - 서보/LED는 duty cycle, **부저는 frequency**
> - HC-SR04의 Echo는 **5V → 전압분배 필수**
