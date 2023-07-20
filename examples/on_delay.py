""" on_delay: test a delay which switches off after a delay
"""
import board
from RGB_led import rgb
from proto_buttons import buttons
from digitalio import DigitalInOut, Direction
from adafruit_ticks import ticks_ms, ticks_add, ticks_less


bit_1 = DigitalInOut(board.D0)
bit_1.direction = Direction.OUTPUT

bit_0 = DigitalInOut(board.D1)
bit_0.direction = Direction.OUTPUT

status = DigitalInOut(board.D5)
status.direction = Direction.OUTPUT


def state_leds(n):
    if startup:
        print(f"{n=}")
        if n == 0:
            bit_0.value = 0
            bit_1.value = 0
        elif n == 1:
            bit_0.value = 1
            bit_1.value = 0
        elif n == 2:
            bit_0.value = 0
            bit_1.value = 1
        elif n == 3:
            bit_0.value = 1
            bit_1.value = 1
    else:
        bit_0.value = 0
        bit_1.value = 0


def error(e):
    print(f"{e=}")
    rgb('r')


def status_led(s):
    if startup:
        print(f"{s=}")
        status.value = s


init = True
while True:
    if init:
        init = False
        on_delay = 10000
        start_time = ticks_ms()
        off_time = ticks_add(start_time, on_delay)
        startup = False
        count = 0

    # check button, if pressed respond appropriately
    pressed = buttons()
    if (pressed is not None):
        if pressed == "STEP":
            count += 1
            state_leds(count)

        elif pressed == "ENTER":
            count -= 1
            state_leds(count)

        else:
            rgb('r')
        pressed = None
    if ticks_less(ticks_ms(), off_time):
        startup = True
    else:
        startup = False
        state_leds(0)
    pressed = None
