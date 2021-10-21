# Continuous Servo Test Program for CircuitPython
import time
import board
import pulseio
from adafruit_motor import servo
 
# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.A2, frequency=50)
pwm2 = pulseio.PWMOut(board.A1, frequency=50)
 
# Create a servo object, my_servo.
my_servo1 = servo.ContinuousServo(pwm1)
my_servo2 = servo.ContinuousServo(pwm2)

while True:
    print("forward")
    my_servo1.throttle = 1.0
    my_servo2.throttle = 1.0
    time.sleep(2.0)
    print("stop")
    my_servo1.throttle = 0.0
    my_servo2.throttle = 0.0
    time.sleep(2.0)
    print("reverse")
    my_servo1.throttle = -1.0
    my_servo2.throttle = -1.0
    time.sleep(2.0)
    print("stop")
    my_servo1.throttle = 0.0
    my_servo2.throttle = 0.0
    time.sleep(4.0)