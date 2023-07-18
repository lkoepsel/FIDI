<<<<<<< Updated upstream
=======
<<<<<<< HEAD
# simple single task program to test overhead
# as the FIDI board only has nine pins available
# uses 8 tasks to make it even to compare to other boards/languages
=======
>>>>>>> Stashed changes
""" ultra_random: provides two fixed frequencies (500, 40kHz) and a random
frequency for a random amount of time.

Uses namedtuple instances to identify states, parameters are:
state: current state
onSTEP: state to move to based on press of STEP button
onENTER: state to move to based on press of ENTER button

Example:
state_1 = states(1, 2, 4)

Requires:
    ultra.py -> code.py
    lib:
        adafruit_ticks.mpy
        adafruit_debouncer.mpy
        proto_buttons.mpy
        RGB_LED.mpy
"""
>>>>>>> origin/main
import board
from digitalio import DigitalInOut, Direction
from random import randrange
from adafruit_ticks import ticks_ms


PIN5 = DigitalInOut(board.D5)
PIN5.direction = Direction.OUTPUT
PIN5.value = True


<<<<<<< Updated upstream
=======
<<<<<<< HEAD
def p5():
    PIN5.value = not PIN5.value


tasks = (p5,)


while True:
    for task in tasks:
        task()
=======
>>>>>>> Stashed changes
def s_0():
    print(f"state 0")
    audible_off()
    leds(0)
    status.value = 0
    return (state_0)


def s_1():
    print(f"state 1")
    audible_off()
    leds(1)
    status.value = 0
    return (state_1)


def s_2():
    print(f"state 2")
    audible_off()
    leds(2)
    status.value = 0
    return (state_2)


def s_3():
    print(f"state 3")
    audible_off()
    leds(3)
    status.value = 0
    return (state_3)


def s_4():
    print(f"state 4")
    audible_on()
    leds(1)
    status.value = 1
    return (state_4)


def s_5():
    print(f"state 5")
    ultra_random()
    leds(2)
    status.value = 1
    return (state_5)


def s_6():
    print(f"state 6")
    ultra_2()
    leds(3)
    status.value = 1
    return (state_6)


def leds(n):
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
        error(1)


def error(e):
    print(f"{e=}")
    rgb('r')


def audible_off():
    speaker.duty_cycle = 0
    return(0)


def audible_on():
    speaker.frequency = 500
    speaker.duty_cycle = dutycycle()
    return(0)


def ultra_random():
    rand_freq = randrange(20000, 50000, 1000)
    print(f"{rand_freq=} {rand_delay=}")
    speaker.frequency = rand_freq
    speaker.duty_cycle = dutycycle()
    return(0)


def ultra_2():
    speaker.frequency = 40000
    speaker.duty_cycle = dutycycle()
    return(0)


def dutycycle():
    pos_duty = 65535 // 2
    print(f"Positive Duty {pos_duty}")
    return(pos_duty)


states = namedtuple('states', ['state', 'onSTEP', 'onENTER'])
state_0 = states(0, s_1, s_0)
state_1 = states(1, s_2, s_4)
state_2 = states(2, s_3, s_5)
state_3 = states(3, s_0, s_6)
state_4 = states(4, s_2, s_4)
state_5 = states(5, s_3, s_5)
state_6 = states(6, s_0, s_6)

STATE = state_0
rand_delay = 0
current_time = ticks_ms()
while True:
    # check button, if pressed respond appropriately
    pressed = buttons()
    if STATE.state == 5:
        if ticks_ms() >= current_time + rand_delay:
            current_time = ticks_ms()
            rand_delay = randrange(500, 10000, 50)
            ultra_random()
    if (pressed is not None):
        if pressed == "STEP":
            STATE = STATE.onSTEP()

        elif pressed == "ENTER":
            STATE = STATE.onENTER()

        else:
            error(0)
    pressed = None
>>>>>>> origin/main
