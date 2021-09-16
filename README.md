# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Here is the code to make the onboard led blink 3 different colors.  


```python
import board
import time

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

print("Make Colors")

while True:
    led[0] = (250, 0, 0)
    time.sleep(0.8)
    led[0] = (0, 250, 0)
    time.sleep(0.8)
    led[0] = (0, 0, 250)
    time.sleep(0.8)

```


### Images
<img src="https://user-images.githubusercontent.com/71342195/132705470-5ed55196-d533-40a7-8287-22687f17d50c.jpg"> <img src="https://user-images.githubusercontent.com/71342195/132705916-4f73c04e-05ac-4eff-89e7-fa6141bc669f.jpg"> <img src="https://user-images.githubusercontent.com/71342195/132704790-18001dc9-acca-49ba-9342-20a454e6e22e.jpg">

### Reflection
The first thing that I had to do was see what was happened to the Metro becasue the serial monitor kept printing "Hello World" even though I had "Make Colors" with the print funtion. Then once that was fixed I had to see if the code I was using actually worked. Once I found out it worked I then stated filling out my notebook.




## CircuitPython_Servo

### Description & Code
Here is the code than makes the servo spin 180 degrees.
```python
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, 5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence
https://www.tinkercad.com/things/2mqeFAH6V5Y-circuit-python-servo/editel?sharecode=9riTHswIG1vkKIqi_YGy5JY-OuLX_4ErNghG6g9OvSQ
### Images
<img src="https://user-images.githubusercontent.com/71342195/133264238-48bde56d-83d8-4563-89e4-3d9abb9a0ada.jpg"><img src="https://user-images.githubusercontent.com/71342195/133264256-2c03cd86-2a41-430d-8bce-b1d57e3de1d5.jpg">
### Reflection
Mainly, the only problem I had was getting the code running, I had to "Make sure you have downloaded the appropriate Adafruit CircuitPython library bundle. So, if you're running version 6.x of CircuitPython, grab the 6.x bundle. Click "Extract All", then you'll find a "lib" folder and inside that you'll find an "adafruit_motor" folder, which contains the "servo.mpy" library.  Copy that file to the lib folder on your Metro and you can use Adafruit's amazing servo object!  In other words, you can say stuff like myServo.angle = 90 instead of having to figure out PWM communication." That was the hardest part of the project. The circuitry was pretty easy because there were only 3 wires to plug in.



## CircuitPython_Distance_Sensor

### Description & Code

```python
import time
import board
import neopixel
from adafruit_hcsr04 import HCSR04

trig = board.A2
echo = board.A3
sonar = HCSR04(trig, echo)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.7
red = 225
green = 0
blue = 0

distance = 0

while True:
    dot.fill((red, green, blue))
    if distance <= 20:
        red = 255 - (12 * distance)
        blue = 0 + (12 * distance)
        green = 0
    if distance > 20:
        green = 0 + (12 * (distance - 20))
        blue = 225 - (12 * (distance - 20))
        red = 0
    if red <= 0:
        red = 0
    if blue >= 225:
        blue = 225
    if blue <= 0:
        blue = 0
    if green >= 225:
        green = 225
    try:
        print(int(sonar.distance))
        distance = int(sonar.distance)
    except RuntimeError:
        pass
        time.sleep(0.05)


```

### Evidence

### Images

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection
