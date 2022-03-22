# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Distance_Sensor](#CircuitPython_Distance_Sensor)
* [LCD_Capacitive_Touch](#LCD_Capacitive_Touch)
* [Classes_Objects_and_Modules](#Classes_Objects_and_Modules)
* [Fun_With_RGB_LEDs](#Fun_With_RGB_LEDs)
---

## Hello_CircuitPython

 <details><summary>Click for Info.</summary>
 <p>  
```
  
 ### Description & Code
  Here is the code to make the onboard led blink 3 different colors.  
  
```python
import board
import time

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1) # This shows what led we are using

led.brightness = 0.3

print("Make Colors") # We use the serial monitor to display that the code is functioning

while True:
    led[0] = (250, 0, 0)
    time.sleep(0.8) # The amount the LED sleeps is how long it takes before it blinks again
    led[0] = (0, 250, 0)
    time.sleep(0.8)
    led[0] = (0, 0, 250)
    time.sleep(0.8)

```


### Evidence and Wiring
No wiring needed as I used onboard LED

<img src="https://user-images.githubusercontent.com/71342195/132705470-5ed55196-d533-40a7-8287-22687f17d50c.jpg"> <img src="https://user-images.githubusercontent.com/71342195/132705916-4f73c04e-05ac-4eff-89e7-fa6141bc669f.jpg"><img src= "https://user-images.githubusercontent.com/71342195/132704790-18001dc9-acca-49ba-9342-20a454e6e22e.jpg" width="250px">

### Reflection
The first thing that I had to do was see what was happened to the Metro becasue the serial monitor kept printing "Hello World" even though I had "Make Colors" with the print funtion. I had to reset the board everytime i updated my code to fix the problem. Once it was fixed the assignment got significantly easier.

'''
</p>
 </details>
  


  
## CircuitPython_Servo
 <details><summary>Click for Info.</summary>
 <p>  
```
  
### Description & Code

Here is the code than makes the servo spin 180 degrees.
```python
import time
import board
import pwmio
from adafruit_motor import servo # This shows what servo we are using

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



### Images and Wiring
<img src="https://user-images.githubusercontent.com/71342195/133264238-48bde56d-83d8-4563-89e4-3d9abb9a0ada.jpg">
This first image is at the beginning at the rotation to 180 degrees
<img src="https://user-images.githubusercontent.com/71342195/133264256-2c03cd86-2a41-430d-8bce-b1d57e3de1d5.jpg"> 
The second image is at the end of the rotation to 180 degrees
<img src="https://github.com/rareval48/CircuitPython/blob/main/Images/Servo.png?raw=true" width="800px">

### Reflection
The only problem I had was getting the code running, I had to "Make sure you have downloaded the appropriate Adafruit CircuitPython library bundle. So, if you're running version 6.x of CircuitPython, grab the 6.x bundle. Click "Extract All", then you'll find a "lib" folder and inside that you'll find an "adafruit_motor" folder, which contains the "servo.mpy" library.  Copy that file to the lib folder on your Metro and you can use Adafruit's amazing servo object!  In other words, you can say stuff like myServo.angle = 90 instead of having to figure out PWM communication." That was the hardest part of the project. The circuitry was pretty easy because there were only 3 wires to plug in.

'''
</p>
 </details>
 
## CircuitPython_Distance_Sensor
 <details><summary>Click for Info.</summary>
 <p>  
```

### Description & Code
Here's the code for sensing distance and using a LED to display it
```python
import time 
import board
import neopixel
from adafruit_hcsr04 import HCSR04 # This shows what sensor we are using

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
        red = 255 - (12 * distance) # This shows what distance is needed for that color
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

### Evidence and Wiring
<img src="https://github.com/rareval48/CircuitPython/blob/main/Images/distance_sensor.gif">

### Reflection
This assignment taught me many things including how to use a distance sensor and how to set up/ plug in the distance sensor to the board. It was pretty easy to get everything setup and get the code to work  all I had to do was to find out how to get the LED to change smoothly. I got it to run smoothly by mixing code from the Hello_CircuitPython assignment above and code from a couple of adafruits websites. :neckbeard:

'''
</p>
 </details>

## LCD_Capacitive_Touch
<details><summary>Click for Info.</summary>
 <p>  
```
  
### Description & Code
Here is the code for LCD capacitive touch
```python
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board
import time
import touchio # Let the board know what we wanted to do

touch = touchio.TouchIn(board.A0)
touch2 = touchio.TouchIn(board.A1)

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), 16, 2, 8)
print("Starting")
print("Chasing")
print("Caught")
lcd.print("Print Now!                 ") # I put this here to show when the board reset
time.sleep(1)
lcd.print("No!")
time.sleep(1)
lcd.clear()

testValue = 0

a = 0
b = 1

Increase = 1
ChangedAlready = 0

while True: # Almost everything below this point is from Logan Martins code for this assignment. The repo will be under the code.
    time.sleep(0.1)
    if touch.value:
        if Increase == 1:
            lcd.clear()
            a = a + b
            print(a)
            lcd.print("\nTouches:")
            lcd.print(str(a))
        if Increase == 0:
            lcd.clear()
            a = a - b
            print(a)
            lcd.print("\nTouches:") # Displays how many touches there are
            lcd.print(str(a))
    if touch2.value:
        print("Switch") # Switches from positive to negative touches
        if ChangedAlready == 0:
            if Increase == 1:
                ChangedAlready = 1
                Increase = 0
        if ChangedAlready == 0:
            if Increase == 0:
                ChangedAlready = 1
                Increase = 1
    if ChangedAlready == 1:
        time.sleep(1)
        ChangedAlready = 0
        

```
[Link for Logan Martins github](https://github.com/Logan-Martin)

### Evidence and Wiring
<img src="https://user-images.githubusercontent.com/71342195/138705220-4aaea59b-582e-4ce8-a230-049f65b8504c.png" width="800px">
<img src="https://user-images.githubusercontent.com/71342195/138706907-e211ae72-78aa-4830-a93c-60ff1ead6577.gif">

### Reflection
It took me a week of working to get this working and was the most difficult assignment. I learned many things while going through this assignment. On of them being, you cant use both lcd.message and lcd.print in the same code. Otherwise it wont do anythng and will show an error. I also had to go on different adafruit websites to try to find code that would work with the backpack on the back of the LCD. Mr. Deirolf ended up working out the code, so the top half of my code is based off of Mr. Deirolf's code.

'''
</p>
 </details>  
  
## Classes_Objects_and_Modules
<details><summary>Click for Info.</summary>
 <p>  
```

### Description and Code
This code allows another piece of code to run without the second piece of code having to be unnecessarily long.

```python
from digitalio import DigitalInOut, Direction
class RGB:
    # declare object with a red pin, green pin, blue pin
    def __init__(self, red, green, blue):
        self.RedLed = DigitalInOut(red)
        self.RedLed.direction = Direction.OUTPUT
        self.GreenLed = DigitalInOut(green)
        self.GreenLed.direction = Direction.OUTPUT
        self.BlueLed = DigitalInOut(blue)
        self.BlueLed.direction = Direction.OUTPUT

    # only red is on
    def red(self):
        self.RedLed.value = 255
        self.GreenLed.value = 0
        self.BlueLed.value = 0

    # only green is on
    def green(self):
        self.RedLed.value = 0
        self.GreenLed.value = 250
        self.BlueLed.value = 0

    # only blue is on
    def blue(self):
        self.RedLed.value = 0
        self.GreenLed.value = 0
        self.BlueLed.value = 255

    # only red and green are on
    def yellow(self):
        self.RedLed.value = 255
        self.GreenLed.value = 100
        self.BlueLed.value = 0

    # only red and blue are on
    def magenta(self):
        self.RedLed.value = 255
        self.GreenLed.value = 0
        self.BlueLed.value = 100

    # only blue and green are on
    def cyan(self):
        self.RedLed.value = 0
        self.GreenLed.value = 255
        self.BlueLed.value = 255
        

```
### Evidence & Wiring
The code below allows the LEDs to change colors by using a class. 

<img src="https://user-images.githubusercontent.com/71342195/157257842-6fb8c05a-99df-4a6d-9e72-c024db789b42.png"><img src="https://user-images.githubusercontent.com/71342195/157259088-ff4afe22-2708-456e-b7d6-e547a445cf44.gif">

'''
</p>
 </details>  
    
  
## Fun_With_RGB_LEDs
<details><summary>Click for Info.</summary>
 <p>  
```
 
### Description and Code
This code allows you to change the time that the leds blink and allows you to control how bright or dim they are.

```python
import time
import board
from rgbfade import RGB

r1 = board.D8
g1 = board.D9
b1 = board.D10

r2 = board.D4
g2 = board.D5
b2 = board.D7  # D6 is using the same timer as D8,9,10.  Avoid!


full = 65535
half = int(65535/10)

LED1 = RGB(r1, g1, b1)
LED2 = RGB(r2, g2, b2)


while True:

    LED1.red()
    LED2.cyan()
    time.sleep(1)
    LED1.red(half)
    LED2.cyan(half)
    time.sleep(1)

    LED1.blue()
    LED2.yellow()
    time.sleep(1)
    LED1.blue(half)
    LED2.yellow(half)
    time.sleep(1)

    LED1.green()
    LED2.magenta()
    time.sleep(1)
    LED1.green(half)
    LED2.magenta(half)
    time.sleep(1)

    LED1.white()
    LED2.white()
    time.sleep(.25)
    LED1.white(half)
    LED2.white(half)
    time.sleep(.25)
    LED1.white()
    LED2.white()
    time.sleep(.25)
    LED1.white(half)
    LED2.white(half)
    time.sleep(.25)


        

```

### Evidence and Wiring

This code was really easy as all you had to do was adapt the code from an earlier assignment to make sure that the dimmer worked. In the earlier code (in module Classes Objects and Modules) all you had to do was add full and half so the board knew what both those terms meant.
<img src="https://user-images.githubusercontent.com/71342195/158599840-17313220-4bc8-42ac-a560-13957b2a3371.gif"><img src="https://user-images.githubusercontent.com/71342195/158600613-babc5a84-a8eb-42d2-a0ed-cbd52d632336.png">

'''
</p>
 </details> 
