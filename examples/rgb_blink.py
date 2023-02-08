import time
import board
from digitalio import DigitalInOut, Direction


RED = DigitalInOut(board.LED_R)
GREEN = DigitalInOut(board.LED_G)
BLUE = DigitalInOut(board.LED_B)


def red(indicator):
    if indicator:
        RED.direction = Direction.INPUT
    else:
        RED.direction = Direction.OUTPUT
        RED.value = False


def green(indicator):
    if indicator:
        GREEN.direction = Direction.INPUT
    else:
        GREEN.direction = Direction.OUTPUT
        GREEN.value = False


def blue(indicator):
    if indicator:
        BLUE.direction = Direction.INPUT
    else:
        BLUE.direction = Direction.OUTPUT
        BLUE.value = False


while True:
    blue(False)
    time.sleep(0.5)
    blue(True)
    time.sleep(0.5)
