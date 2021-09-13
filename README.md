# CircuitPython1
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


### Evidence


### Images
<img src="https://user-images.githubusercontent.com/71342195/132705470-5ed55196-d533-40a7-8287-22687f17d50c.jpg"> <img src="https://user-images.githubusercontent.com/71342195/132705916-4f73c04e-05ac-4eff-89e7-fa6141bc669f.jpg"> <img src="https://user-images.githubusercontent.com/71342195/132704790-18001dc9-acca-49ba-9342-20a454e6e22e.jpg">

### Reflection
The first thing that I had to do was see what was happened to the Metro becasue the serial monitor kept printing "Hello World" even though I had "Make Colors" with the print funtion. Then once that was fixed I had to see if the code I was using actually worked. Once I found out it worked I then stated filling out my notebook.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

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
