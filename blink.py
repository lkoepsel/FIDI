import time
import board
from digitalio import DigitalInOut, Direction

RED = DigitalInOut(board.LED_R)
RED.direction = Direction.OUTPUT
GREEN = DigitalInOut(board.LED_G)
GREEN.direction = Direction.OUTPUT
BLUE = DigitalInOut(board.LED_B)
BLUE.direction = Direction.OUTPUT

while True:
    RED.value = False
    BLUE.value = False
    time.sleep(0.5)
    # RED.value = True
    BLUE.value = True
    time.sleep(0.5)
