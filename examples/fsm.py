# fsm: Original finite state machine using conditional logic only
# retained to use to determine efficiency of new fsm
import board
from adafruit_debouncer import Debouncer
import digitalio
from RGB_led import rgb
from proto_buttons import buttons

state = 0
while True:
    # check button, if pressed respond appropriately
    change = False
    pressed = buttons()
    # print(f"{state=}{pressed=}{change=}")
    if (pressed is not None):
        change = True
        while (change and state == 0):
            change = False
            if pressed == "D0":
                rgb('g')
                state = 1
                print(f"in state 0 {state =}")

            elif pressed == "D1":
                rgb('b')
                state = 0

            else:
                rgb('r')

        while (change and state == 1):
            change = False
            if pressed == "D0":
                rgb('g')
                state = 2
                print(f"in state 1 {state =}")

            elif pressed == "D1":
                rgb('b')
                state = 1
                change = True

            else:
                rgb('r')

        while (change and state == 2):
            change = False
            if pressed == "D0":
                rgb('g')
                state = 3
                print(f"in state 2 {state =}")

            elif pressed == "D1":
                rgb('b')
                state = 2
                change = True

            else:
                rgb('r')

        while (change and state == 3):
            change = False
            if pressed == "D0":
                rgb('g')
                state = 0
                print(f"in state 3 {state =}")

            elif pressed == "D1":
                rgb('b')
                state = 3
                change = True

            else:
                rgb('r')
