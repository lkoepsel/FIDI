# simple round-robin scheduler to test speed
# uses 8 tasks to make it even to compare to other boards/languages
import board
from digitalio import DigitalInOut, Direction


PIN8 = DigitalInOut(board.GP8)
PIN8.direction = Direction.OUTPUT
PIN8.value = False
PIN9 = DigitalInOut(board.GP9)
PIN9.direction = Direction.OUTPUT
PIN9.value = True
PIN2 = DigitalInOut(board.GP2)
PIN2.direction = Direction.OUTPUT
PIN2.value = True
PIN3 = DigitalInOut(board.GP3)
PIN3.direction = Direction.OUTPUT
PIN3.value = True
PIN4 = DigitalInOut(board.GP4)
PIN4.direction = Direction.OUTPUT
PIN4.value = True
PIN5 = DigitalInOut(board.GP5)
PIN5.direction = Direction.OUTPUT
PIN5.value = True
PIN6 = DigitalInOut(board.GP6)
PIN6.direction = Direction.OUTPUT
PIN6.value = True
PIN7 = DigitalInOut(board.GP7)
PIN7.direction = Direction.OUTPUT
PIN7.value = True


def p8():
    PIN8.value = not PIN8.value


def p9():
    PIN9.value = not PIN9.value


def p2():
    PIN2.value = not PIN2.value


def p3():
    PIN3.value = not PIN3.value


def p4():
    PIN4.value = not PIN4.value


def p5():
    PIN5.value = not PIN5.value


def p6():
    PIN6.value = not PIN6.value


def p7():
    PIN7.value = not PIN7.value


task_list = (p8, p9, p2, p3, p4, p5, p6, p7)


def tasks():
    while True:
        for task in task_list:
            task()
