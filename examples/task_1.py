# simple single task program to test overhead
# Runs at 5kHz or 200ms
# uses 8 tasks to make it even to compare to other boards/languages
import board
from digitalio import DigitalInOut, Direction


PIN5 = DigitalInOut(board.D5)
PIN5.direction = Direction.OUTPUT
PIN5.value = True


def p5():
    PIN5.value = not PIN5.value


tasks = (p5,)


while True:
    for task in tasks:
        task()
