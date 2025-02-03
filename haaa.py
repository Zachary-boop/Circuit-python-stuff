import board
import digitalio
import time

pin_5 = digitalio.DigitalInOut(board.D5)
pin_5.direction = digitalio.Direction.OUTPUT
pin_5.value = False
def back_90 ():
    pin_5.value = True
    time.sleep(0.001)
    pin_5.value = False
    time.sleep(0.019)

back_90()



