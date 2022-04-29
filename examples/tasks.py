# simple round-robin scheduler to test speed 
# as the FIDI board only has nine pins available
# uses 8 tasks to make it even to compare to other boards/languages
import time
import board
from digitalio import DigitalInOut, Direction


PIN0 = DigitalInOut(board.D0)
PIN0.direction = Direction.OUTPUT
PIN0.value = False
PIN1 = DigitalInOut(board.D1)
PIN1.direction = Direction.OUTPUT
PIN1.value = True
PIN2 = DigitalInOut(board.D2)
PIN2.direction = Direction.OUTPUT
PIN2.value = True
PIN3 = DigitalInOut(board.D3)
PIN3.direction = Direction.OUTPUT
PIN3.value = True
PIN4 = DigitalInOut(board.D4)
PIN4.direction = Direction.OUTPUT
PIN4.value = True
# PIN5 = DigitalInOut(board.D5)
# PIN5.direction = Direction.OUTPUT
# PIN5.value = True

RED = DigitalInOut(board.LED_R)
RED.direction = Direction.OUTPUT
RED.value = True
GREEN = DigitalInOut(board.LED_G)
GREEN.direction = Direction.OUTPUT
GREEN.value = True
BLUE = DigitalInOut(board.LED_B)
BLUE.direction = Direction.OUTPUT
BLUE.value = True


def p0():
    PIN0.value = not PIN0.value


def p1():
    PIN1.value = not PIN1.value


def p2():
    PIN2.value = not PIN2.value


def p3():
    PIN3.value = not PIN3.value


def p4():
    PIN4.value = not PIN4.value


def p5():
    PIN4.value = not PIN5.value


def r():
    RED.value = not RED.value


def g():
    GREEN.value = not GREEN.value


def b():
    BLUE.value = not BLUE.value


tasks = (p0, p1, p2, p3, p4, p5, r, g, b,)


while True:
    for task in tasks:
        task()
