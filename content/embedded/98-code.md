# 코드 모음

실습에 나온 **함수 레퍼런스와 전체 소스코드**만 모은 페이지입니다. 설명은 각 강의 페이지에, 여기는 **칠 것**만 있습니다.

## 함수 레퍼런스

### RPi.GPIO

```python
import RPi.GPIO as GPIO
```

| 함수 | 설명 |
|---|---|
| `GPIO.setwarnings(False)` | 불필요한 warning 제거 |
| `GPIO.setmode(GPIO.BCM)` | 핀 번호 모드 설정 (`GPIO.BOARD` / `GPIO.BCM`) |
| `GPIO.setup(channel, GPIO.OUT)` | 핀을 출력으로 설정 |
| `GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)` | 초기값과 함께 출력 설정 |
| `GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)` | 입력 + pull-up |
| `GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)` | 입력 + pull-down |
| `GPIO.output(channel, 1)` | 3.3V 출력 (High) |
| `GPIO.output(channel, 0)` | 0V 출력 (Low) |
| `GPIO.input(channel)` | 입력 읽기 |
| `GPIO.add_event_detect(pin, GPIO.RISING, callback=f, bouncetime=300)` | 이벤트 감지 등록 |
| `GPIO.cleanup()` | GPIO 설정 초기화 |

**상수**

| 상수 | 값 |
|---|---|
| `GPIO.HIGH` | 3.3V, `True`, `1` |
| `GPIO.LOW` | 0V, `False`, `0` |
| `GPIO.RISING` | 0 → 1 변화 |

### PWM

```python
p = GPIO.PWM(channel, frequency)   # PWM 인스턴스 생성 (핀번호, 주파수 Hz)
p.start(dc)                        # 초기 duty cycle로 PWM 시작
p.ChangeDutyCycle(dc)              # duty cycle 변경 (0 ~ 100.0)
p.ChangeFrequency(freq)            # 주파수 변경
p.stop()                           # PWM 종료
```

### time

```python
import time

time.sleep(delay)                  # delay 초 대기
time.time()                        # 1970-01-01 00:00:00 이후 경과 시간(초)
```

### spidev (SPI / MCP3008)

```python
import spidev

spi = spidev.SpiDev()              # SPI 인스턴스 생성
spi.open(0, 0)                     # SPI 통신 시작
spi.max_speed_hz = 100000          # 통신 속도 설정
spi.xfer2([1, (8 + adcnum) << 4, 0])   # 데이터 송수신
```

### OLED (I2C)

```python
import adafruit_ssd1306
import busio
from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(SCL, SDA)                          # I2C 인터페이스 생성
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)                                    # 화면 초기화
display.image(image)                               # 이미지 전달
display.show()                                     # 화면에 표시
display.width / display.height                     # 해상도

image = Image.new('1', (width, height))            # '1' = 흑백
draw = ImageDraw.Draw(image)                       # 그리기 객체
draw.rectangle((0, 0, w, h), outline=0, fill=0)    # 0=검정, 255=흰색
draw.text((x, y), "text", font=font, fill=255)
font = ImageFont.load_default()
```

---

## 전체 소스코드

### led_ex01.py — 첫 LED (BOARD 모드)

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

### LED_Blink.py — LED 깜빡이기 (BCM 모드)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

led_pin = 4                      # GPIO 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin, 1)      # LED 켜짐
    time.sleep(1)
    GPIO.output(led_pin, 0)      # LED 꺼짐
    time.sleep(1)

GPIO.cleanup()
```

### Btn_Polling.py — 버튼 (polling)

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

button_pin = 15                  # GPIO 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")
    time.sleep(0.1)

GPIO.cleanup()
```

### Btn_callbak.py — 버튼으로 LED 토글 (event handling)

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

light_on = False

def button_callback(channel):
    global light_on
    if light_on == False:
        GPIO.output(led_pin, 1)
        print("LED ON!")
    else:
        GPIO.output(led_pin, 0)
        print("LED OFF!")
    light_on = not light_on

GPIO.add_event_detect(button_pin, GPIO.RISING,
                      callback=button_callback, bouncetime=300)

while 1:
    time.sleep(0.1)

GPIO.cleanup()
```

### PWM_LED.py — LED 밝기 조정

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

led_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

p = GPIO.PWM(led_pin, 50)        # 50Hz
p.start(0)

try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
```

### PWM_Buzzer.py — 부저 음 조정

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

bz_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(bz_pin, GPIO.OUT)

p = GPIO.PWM(bz_pin, 100)        # 100Hz

# 4옥타브 도~시, 5옥타브 도
Frq = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5

p.start(10)

try:
    while 1:
        for fr in Frq:
            p.ChangeFrequency(fr)
            time.sleep(speed)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
```

### PWM_Servo.py — 서보모터 각도 조정

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
servo.start(0)

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

### HC_SR04.py — 초음파 센서 거리 측정

```python
#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance measurement in process")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)          # 초음파 발사
        time.sleep(0.00001)              # 10us
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == False:
            start = time.time()
        while GPIO.input(ECHO) == True:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34000 / 2
        print("Distance : %.1f cm" % (distance))

        time.sleep(0.4)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
```

### HC_SR501.py — PIR 인체감지 센서

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
GPIO.setup(sensor, GPIO.IN)

print("PIR Ready ....")
time.sleep(5)

try:
    while True:
        if GPIO.input(sensor) == 1:
            GPIO.output(led_Y, 1)
            GPIO.output(led_R, 0)
            print("Motion Detected !")
            time.sleep(0.2)

        if GPIO.input(sensor) == 0:
            GPIO.output(led_R, 1)
            GPIO.output(led_Y, 0)
            print("Motion Not Detected !")
            time.sleep(0.2)
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()
```

### readadc() — MCP3008 공통 함수

{: .중요 }
> 아래 SPI 실습 4개(`MCP_3008`, `LDR`, `Joystick`, `OLED`)에 **똑같이** 들어간다.

```python
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

### MCP_3008.py — 가변저항 값 읽기

```python
#-*-coding:utf-8-*-
import spidev
import time

delay = 0.5
pot_channel = 0

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
    pot_value = readadc(pot_channel)
    print("-----------------------------")
    print("POT Value: %d" % (pot_value))
    time.sleep(delay)
```

### LDR.py — 조도 센서

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

### Joystick.py — 조이스틱

```python
#-*-coding:utf-8-*-
import spidev
import time

delay = 0.5

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

### OLED_MCP3008_joystick.py — OLED에 조이스틱 값 출력

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

sw_channel  = 0
vrx_channel = 2
vry_channel = 1

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

# I2C interface 생성
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.show()

x = 0
padding = -2
y = padding

font = ImageFont.load_default()

width  = display.width
height = display.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

while True:
    sw_val  = readadc(sw_channel)
    vrx_pos = readadc(vrx_channel)
    vry_pos = readadc(vry_channel)

    print('Switch = {0:0.2f}'.format(sw_val))
    print('X-axis = {0:0.2f}'.format(vrx_pos))
    print('Y-axis = {0:0.2f}'.format(vry_pos))

    draw.text((x, y),    ' Switch = {0:0.2f}'.format(sw_val),  font=font, fill=255)
    draw.text((x, y+8),  ' X-axis = {0:0.2f}'.format(vrx_pos), font=font, fill=255)
    draw.text((x, y+16), ' Y-axis = {0:0.2f}'.format(vry_pos), font=font, fill=255)

    display.image(image)
    display.show()

    time.sleep(0.5)
```

---

## 실행 / 설치 명령어

```bash
$ python LED_Blink.py                            # 실행 (VSCode에서는 F5)

$ sudo raspi-config                              # SPI / I2C / VNC 활성화
$ sudo reboot

$ sudo apt-get install python3-spidev            # SPI 라이브러리

$ python3 -m venv .venv                          # 가상환경 생성
$ source .venv/bin/activate
$ pip3 install spidev
$ pip3 install adafruit-circuitpython-ssd1306
$ pip3 install pillow
$ deactivate

$ ls /dev/i2c*                                   # I2C 디바이스 확인
$ i2cdetect -y 1                                 # I2C 주소 확인 (OLED = 0x3c)
```
