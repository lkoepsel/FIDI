import board
from digitalio import DigitalInOut, Direction


RED = DigitalInOut(board.LED_R)
RED.direction = Direction.OUTPUT
RED.value = True
GREEN = DigitalInOut(board.LED_G)
GREEN.direction = Direction.OUTPUT
GREEN.value = True
BLUE = DigitalInOut(board.LED_B)
BLUE.direction = Direction.OUTPUT
BLUE.value = True


def rgb(colors):
    if len(colors) <= 3:
        if 'r' in colors:
            RED.value = False
        else:
            RED.value = True
        if 'g' in colors:
            GREEN.value = False
        else:
            GREEN.value = True
        if 'b' in colors:
            BLUE.value = False
        else:
            BLUE.value = True


def rgb_blink(colors, rate, duration):
    if len(colors) <= 3:
        if 'r' in colors:
            RED.value = False
        else:
            RED.value = True
        if 'g' in colors:
            GREEN.value = False
        else:
            GREEN.value = True
        if 'b' in colors:
            BLUE.value = False
        else:
            BLUE.value = True
