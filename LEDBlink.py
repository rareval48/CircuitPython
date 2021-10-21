from digitalio import DigitalInOut, Direction#pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
#import gc
from analogio import AnalogIn #pylint: disable-msg=import-error
#print(gc.mem_free())
#from fractions import Fraction #pylint: disable-msg=import-error
import time


red = DigitalInOut(board.D5)#red
red.direction = Direction.OUTPUT
green = DigitalInOut(board.D6)#green
green.direction = Direction.OUTPUT
blue = DigitalInOut(board.D7)#blue
blue.direction = Direction.OUTPUT

##################
oldseconds = 0.0
##################

potpin = AnalogIn(board.A2)
potpin2 = AnalogIn(board.A1)
potpin3 = AnalogIn(board.A0)

def mapp(x,in_min,in_max,out_min,out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

'''
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def reduceFraction(nume, deno) : #the differing denominators make it inconsistent

    if nume%2 != 0:#make it even for smaller fractions
       nume+=1

    f = gcd(deno, nume)

    nume = nume // f
    deno = deno // f

    output = (nume,deno)
    return output
'''
'''def ledset(a):
    if a == 0:
        test = red
        zoom = potpin
    if a == 1:
        test = green
        zoom = potpin2
    if a == 2:
        test = blue
        zoom = potpin3

    #The denominator is the length of the patern
    #duty_cycle = reduceFraction(int(mapp(potpin4.value,0,65535,0,128)),128)#maybe limit denominator, butit shouldn't go above 2^15
    #subtract the numerator from the denominator
    threshhold = mapp(zoom.value,0,65535,0,128)
    #print(threshhold*0.0001)
    global oldseconds
    seconds = time.monotonic()#updated seconds
    if((threshhold*0.0001)>=0.0122):#turns the led off if the threshold is too high
        test.value = False
    elif (seconds - oldseconds >= 0.0001*threshhold):
        test.value = True
        oldseconds = seconds
    else:
        test.value = False'''

def ledset():
    colors = [potpin.value,potpin2.value,potpin3.value]
    spot = colors.index(max(colors))
    print(spot)
    if spot == 0:
       red.value = False
       green.value = True
       blue.value = True
    elif spot == 1:
        green.value = False
        red.value = True
        blue.value = True
    elif spot == 2:
        blue.value = False
        red.value = True
        green.value = True

while True:
    '''ledset(0)#set led colors using function ledset(color)
    ledset(1)#set led colors using function ledset(color)
    ledset(2)#set led colors using function ledset(color)'''
    ledset()
