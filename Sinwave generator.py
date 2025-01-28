import board
import digitalio
import time
import math
#Pin A3 is a pwm output
Pin_generator = digitalio.DigitalInOut(board.D5)
Pin_generator.direction = digitalio.Direction.OUTPUT
frequency = 10


## Turns a designated digital pin into a PWM pin the goal cannot be over 3.3V pin should be a digital pin variable
def ADC (goal,pin):
    ratio = goal/3.3
    pin.value = True
    time.sleep(ratio*frequency)
    pin.value = False
    time.sleep((1-ratio)*frequency)

while True:
    ADC(1.7,Pin_generator)