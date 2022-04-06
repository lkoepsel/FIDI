import board
from digitalio import DigitalInOut, Direction


RED = DigitalInOut(board.LED_R)
GREEN = DigitalInOut(board.LED_G)
BLUE = DigitalInOut(board.LED_B)


def red(indicator):
    if indicator == 'Off':
        RED.direction = Direction.INPUT
    else:
        RED.direction = Direction.OUTPUT
        RED.value = False

def green(indicator):
    if indicator == 'Off':
        GREEN.direction = Direction.INPUT
    else:
        GREEN.direction = Direction.OUTPUT
        GREEN.value = False

def blue(indicator):
    if indicator == 'Off':
        BLUE.direction = Direction.INPUT
    else:
        BLUE.direction = Direction.OUTPUT
        BLUE.value = False


def rgb(colors):
    if len(colors) <= 3:
        if 'r' in colors:
            red('On')
        else:
            red('Off')
        if 'g' in colors:
            green('On')
        else:
            green('Off')
        if 'b' in colors:
            blue('On')
        else:
            blue('Off')
