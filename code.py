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
import board
import pwmio
from proto_buttons import buttons
from collections import namedtuple
from digitalio import DigitalInOut, Direction
from random import randrange
from adafruit_ticks import ticks_ms, ticks_add, ticks_less


bit_1 = DigitalInOut(board.D0)
bit_1.direction = Direction.OUTPUT

bit_0 = DigitalInOut(board.D1)
bit_0.direction = Direction.OUTPUT

error_led = DigitalInOut(board.LED_R)
error_led.direction = Direction.OUTPUT
error_led.value = 1

ON = 0
MED = 32767
DIM = 62000
OFF = 65535
status_led = pwmio.PWMOut(board.LED_B, frequency=1000, duty_cycle=OFF)

speaker = pwmio.PWMOut(board.D4, frequency=500, duty_cycle=0,
                       variable_frequency=True)


def s_0():
    print(f"state 0")
    audible_off()
    state_leds(0)
    status_off()
    return (state_0)


def s_1():
    print(f"state 1")
    audible_off()
    state_leds(1)
    status_off()
    return (state_1)


def s_2():
    print(f"state 2")
    audible_off()
    state_leds(2)
    status_off()
    return (state_2)


def s_3():
    print(f"state 3")
    audible_off()
    state_leds(3)
    status_off()
    return (state_3)


def s_4():
    print(f"state 4")
    audible_on()
    state_leds(1)
    status_on(ON)
    return (state_4)


def s_5():
    print(f"state 5")
    ultra_random()
    state_leds(2)
    status_on(ON)
    return (state_5)


def s_6():
    print(f"state 6")
    ultra_2()
    state_leds(3)
    status_on(ON)
    return (state_6)


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
    if e == 0:
        error_led = 1
    else:
        print(f"{e=}")
        error_led.value = 0


def status_off():
    status_led.duty_cycle = OFF
    return(0)


def status_on(s):
    status_led.duty_cycle = s
    return(0)


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
    return(pos_duty)


states = namedtuple('states', ['state', 'onSTEP', 'onENTER'])
state_0 = states(0, s_1, s_0)
state_1 = states(1, s_2, s_4)
state_2 = states(2, s_3, s_5)
state_3 = states(3, s_0, s_6)
state_4 = states(4, s_2, s_4)
state_5 = states(5, s_3, s_5)
state_6 = states(6, s_0, s_0)

init = True
STATE = state_0
error(0)
while True:
    if init:
        rand_delay = 0
        on_delay = 10000
        current_time = ticks_ms()
        start_time = ticks_ms()
        off_time = ticks_add(start_time, on_delay)
        startup = False
        init = False
        STATE.onENTER()

    # check button, if pressed respond appropriately
    pressed = buttons()
    if ticks_less(ticks_ms(), off_time):
        startup = True
    else:
        startup = False
        state_leds(0)
        status_on(DIM)
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
            error(1)
    pressed = None
