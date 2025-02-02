import board
import digitalio
import time
import math
#Pin A3 is a pwm output
Pin_generator = digitalio.DigitalInOut(board.D5)
Pin_generator.direction = digitalio.Direction.OUTPUT
frequency = 52.5
period = 1/frequency

## Turns a designated digital pin into a PWM pin the goal cannot be over 3.3V pin should be a digital pin variable
def ADC (goal):
    ratio = goal/3.3
    global Pin_generator
    Pin_generator.value = True
    time.sleep(ratio*period)
    Pin_generator.value = False
    time.sleep((1-ratio)*period)


while True:
    
    # for i in range (360):
    #   x=i*(math.pi/180)
    #   ADC(math.sin(x))
