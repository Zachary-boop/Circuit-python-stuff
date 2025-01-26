## blink pin 5,scl,sda in order :3
import time
import digitalio
import board

pin_5 = digitalio.DigitalInOut(board.D5)
pin_5.direction = digitalio.Direction.OUTPUT

pin_sda = digitalio.DigitalInOut(board.D7)
pin_sda.direction = digitalio.Direction.OUTPUT

pin_scl = digitalio.DigitalInOut(board.D4)
pin_scl.direction = digitalio.Direction.OUTPUT

pin_5.value = False
pin_sda.value = False
pin_scl.value = False
while True:
     pin_5.value = True
     pin_sda.value = False
     time.sleep(0.5)
     pin_scl.value = True
     pin_5.value = False
     time.sleep(0.5)
     pin_sda.value = True
     pin_scl.value = False
     time.sleep(0.5)