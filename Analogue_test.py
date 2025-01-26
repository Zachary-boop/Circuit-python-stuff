## Testing analog IO will blink pin 5 depending on the analog reading of A3
import board
import analogio
import digitalio
import time

a = analogio.AnalogIn(board.A3)
a_Tension = a.value

pin5 = digitalio.DigitalInOut(board.D5)
pin5.direction = digitalio.Direction.OUTPUT

while True :
    pin5.value = False
    time.sleep(a.value/65536)
    pin5.value = True
    time.sleep(a.value/65536)