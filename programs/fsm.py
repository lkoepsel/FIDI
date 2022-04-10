import board
from adafruit_debouncer import Debouncer
import digitalio
from RGB_led import rgb
from proto_buttons import buttons

while True:
    # check button, if pressed respond appropriately
    state = 0
    pressed = buttons()
    if pressed == "N":
        change = False

    else:
        while (state == 0):
            if pressed == "UP":
                rgb('g')
                state = 1
                pressed = False
                change = True
                print(f"in state 0 {state =}")

            elif pressed == "ENTER":
                rgb('b')
                state = 10
                change = True

            else:
                rgb('r')

        while (state == 1):
            if pressed == "UP":
                rgb('g')
                state = 2
                pressed = False
                change = True
                print(f"in state 1 {state =}")

            elif pressed == "ENTER":
                rgb('b')
                state = 1
                change = True

            else:
                rgb('r')

        while (state == 2):
            if pressed == "UP":
                rgb('g')
                state = 0
                change = True
                print(f"in state 2 {state =}")

            elif pressed == "ENTER":
                rgb('b')
                state = 1
                change = True

            else:
                rgb('r')
