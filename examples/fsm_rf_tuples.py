""" fsm: finite state machine

Uses namedtuple instances to identify states, parameters are:
state: current state
onD0: state to move to based on press of button on D0
onD1: state to move to based on press of button on D1
ledD0: led color based on rgb() to light based on D0
ledD1: led color based on rgb() to light based on D1
funcD0: function to execute based on D0
funcD1: function to execute based on D1
Example:
state_1 = states(1, 2, 1, 'g', 'rb', audible_off, audible_1)

"""
import board
import pwmio
from analogio import AnalogIn
from RGB_bin import bin_leds, blink_bin
from proto_buttons import buttons
from collections import namedtuple
import supervisor


supervisor.disable_autoreload()

state = 0
change = False
speaker = pwmio.PWMOut(board.D3, frequency=500, duty_cycle=0,
                       variable_frequency=True)
analog_in = AnalogIn(board.A2)
MAGENTA = 99
YELLOW = 98


def null_stub():
    print('null')
    return()


def audible_off():
    speaker.duty_cycle = 0
    return(0)


def audible_1():
    speaker.frequency = 500
    speaker.duty_cycle = dutycycle()
    return(0)


def ultra_1():
    speaker.frequency = 22000
    speaker.duty_cycle = dutycycle()
    return(0)


def ultra_2():
    speaker.frequency = 40000
    speaker.duty_cycle = dutycycle()
    return(0)


def dutycycle():
    pos_duty = analog_in.value * 100 // 65535
    print(f"POT: {analog_in.value} {pos_duty=}")
    return(analog_in.value)


states = namedtuple('states', ['state', 'onD0', 'onD1', 'funcD0', 'funcD1'])
state_0 = states(0, 1, 0, audible_off, null_stub)
state_1 = states(1, 2, 1, audible_off, audible_1)
state_2 = states(2, 3, 2, audible_off, ultra_1)
state_3 = states(3, 0, 3, audible_off, ultra_2)


def states(STATE):
    if pressed == "D0":
        state = STATE.onD0
        bin_leds(STATE.state)
        STATE.funcD0()
        print(f"state {STATE.state} UP {state=}")

    elif pressed == "D1":
        state = STATE.onD1
        blink_bin(MAGENTA, STATE.state)
        STATE.funcD1()
        print(f"state {STATE.state} ENTER {state=}")

    else:
        bin_leds(5)

    return(state)


while True:
    # check button, if pressed respond appropriately
    pressed = buttons()

    if (pressed is not None):
        change = True
        while (change and state == 0):
            change = False
            state = states(state_0)

        while (change and state == 1):
            change = False
            state = states(state_1)

        while (change and state == 2):
            change = False
            state = states(state_2)

        while (change and state == 3):
            change = False
            state = states(state_3)
