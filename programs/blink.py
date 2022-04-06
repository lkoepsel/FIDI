import time
import board
from digitalio import DigitalInOut, Direction

# RED = DigitalInOut(board.LED_R)
# RED.direction = Direction.OUTPUT
# GREEN = DigitalInOut(board.LED_G)
# GREEN.direction = Direction.OUTPUT
# BLUE = DigitalInOut(board.LED_B)
# BLUE.direction = Direction.OUTPUT

def red(indicator):
    RED = DigitalInOut(board.LED_R)
    if indicator == True:
        RED.direction = Direction.INPUT
    else:
        RED.direction = Direction.OUTPUT
        RED.value = False


while True:
    red(False)
    time.sleep(0.5)
    red(True)
    time.sleep(0.5)
