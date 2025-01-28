#import board
#import analogio
import time
import math
## Pin A3 is a analog output
#Pin_generator = analogio.AnalogOut(board.A3)

frequency = 10

while True:
    for i in range (360):
        Base_sin = (math.sin(i)+1)
        #Pin_generator.value - Base_sin * 65536
        print (Base_sin/2*65536)
        time.sleep(1)