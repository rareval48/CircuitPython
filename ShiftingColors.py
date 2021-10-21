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
