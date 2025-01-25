# file code.py
# file code.py
# author Samuel Faucher
# date novembre 2024
# brief Tests unitaires pour la manette dans le cours de Prototypage
# inspired from: SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries (SPDX-License-Identifier: MIT)

# Add boot.py AND hid_gamepad.py
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices#custom-hid-devices-3096614-9

import board
import digitalio
import analogio
import usb_hid
import adafruit_hid

from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
button_pins = (board.D6, board.D10, board.D5, board.D9, board.D12, board.D11, board.D8)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 3, 4, 9, 10, 11)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Connect an analog two-axis joystick to A4 and A5.
ax = analogio.AnalogIn(board.A3)
ay = analogio.AnalogIn(board.A4)

# DEL -----------------------------------------
del_num1 = digitalio.DigitalInOut(board.D3)
del_num1.direction = digitalio.Direction.OUTPUT

del_num2 = digitalio.DigitalInOut(board.D4)
del_num2.direction = digitalio.Direction.OUTPUT

# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# main --------------------------------------------------------------------------
flip = False

while True:
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end="")

    # Convert range[0, 65535] to -127 to 127
    gp.move_joysticks(
        x=range_map(ax.value, 0, 65535, 127, -127),
        y=range_map(ay.value, 0, 65535, 127, -127),
    )
    print(" x", ax.value, "y", ay.value)

    #flip = not(flip)
    #del_num1.value = not(flip)
    #del_num2.value = flip
    # time.sleep(2.0)

















