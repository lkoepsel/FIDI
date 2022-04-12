""" fsm: finite state machine

Uses namedtuple instances to identify states, parameters are:
state: current state
on_D0: state to move to based on press of button on D0
on_D1: state to move to based on press of button on D1
led_D0: led color based on rgb() to light based on D0
led_D1: led color based on rgb() to light based on D1
func_D0: function to execute based on D0
func_D1: function to execute based on D1
Example:
state_1 = states(1, 2, 1, 'g', 'rb', audible_off, audible_1)

"""
import board
import pwmio
from analogio import AnalogIn
from RGB_led import rgb
from proto_buttons import buttons
from collections import namedtuple
import supervisor


supervisor.disable_autoreload()

state = 0
change = False
speaker = pwmio.PWMOut(board.D3, frequency=500, duty_cycle=0,
                       variable_frequency=True)
analog_in = AnalogIn(board.A2)


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


states = namedtuple('states', ['state', 'on_D0', 'on_D1', 'led_D0', 'led_D1',
                               'func_D0', 'func_D1'])
state_0 = states(0, 1, 0, 'g', 'b', audible_off, null_stub)
state_1 = states(1, 2, 1, 'g', 'rb', audible_off, audible_1)
state_2 = states(2, 3, 2, 'g', 'gb', audible_off, ultra_1)
state_3 = states(3, 0, 3, 'g', 'rgb', audible_off, ultra_2)


def states(STATE):
    if pressed == "D0":
        state = STATE.on_D0
        rgb(STATE.led_D0)
        STATE.func_D0()
        print(f"state {STATE.state} UP {state=}")

    elif pressed == "D1":
        state = STATE.on_D1
        rgb(STATE.led_D1)
        STATE.func_D1()
        print(f"state {STATE.state} ENTER {state=}")

    else:
        rgb('r')

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
