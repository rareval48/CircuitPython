# Continuous Servo Test Program for CircuitPython
import time
import board
import pulseio
import touchio
from adafruit_motor import servo
 
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, frequency=50)
 
# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

touch_A0 = touchio.TouchIn(board.A0)  # Not a touch pin on Trinket M0!
touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
 
while True:
   
    if touch_A0.value:
        print("Touched A0!")
        my_servo.throttle = 1.0
        time.sleep(2.0)
        
    if touch_A1.value:
        print("Touched A1!")
        my_servo.throttle = -1.0
        time.sleep(2.0)
        
   