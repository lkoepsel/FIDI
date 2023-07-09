""" fsm: finite state machine

Uses namedtuple instances to identify states, parameters are:
state: current state
onSTEP: state to move to based on press of STEP button
onENTER: state to move to based on press of ENTER button

Example:
state_1 = states(1, 2, 1)

"""
import board
import pwmio
from RGB_led import rgb
from proto_buttons import buttons
from collections import namedtuple
# import supervisor
from digitalio import DigitalInOut, Direction


# STEP = DigitalInOut(board.D0)
# STEP.direction = Direction.INPUT
# STEP.pull = Pull.UP

# ENTER = DigitalInOut(board.D1)
# ENTER.direction = Direction.INPUT
# ENTER.pull = Pull.UP

bit_1 = DigitalInOut(board.D0)
bit_1.direction = Direction.OUTPUT

bit_0 = DigitalInOut(board.D1)
bit_0.direction = Direction.OUTPUT

status = DigitalInOut(board.D4)
status.direction = Direction.OUTPUT

speaker = pwmio.PWMOut(board.D5, frequency=500, duty_cycle=0,
                       variable_frequency=True)

# supervisor.disable_autoreload()

state = 0
change = False


def s_0():
    print(f"state 0")
    audible_off()
    leds(0)
    return (state_0)


def s_1():
    print(f"state 1")
    audible_off()
    leds(1)
    return (state_1)


def s_2():
    print(f"state 2")
    audible_off()
    leds(2)
    return (state_2)


def s_3():
    print(f"state 3")
    audible_off()
    leds(3)
    return (state_3)


def s_4():
    print(f"state 4")
    audible_off()
    leds(1)
    return (state_4)


def s_5():
    print(f"state 5")
    audible_off()
    leds(2)
    return (state_5)


def s_6():
    print(f"state 6")
    audible_off()
    leds(3)
    return (state_6)


def leds(n):
    if n == 0:
        bit_0.value = 0
        bit_1.value = 1
    if n == 0:
        bit_0.value = 0
        bit_1.value = 1
    if n == 0:
        bit_0.value = 0
        bit_1.value = 1
    if n == 0:
        bit_0.value = 0
        bit_1.value = 1
    else:
        error()


def error():
    rgb('r')


def null_stub():
    print('null')
    return()


def audible_off():
    speaker.duty_cycle = 0
    return(0)


def audible_on():
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
    pos_duty = 0x7fff
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
print(f"start: {STATE.state}")
while True:
    print(f"loop: {STATE.state}")
    # check button, if pressed respond appropriately
    pressed = buttons()
    print(f"{pressed=}")

    if (pressed is not None):
        print(f"not None: {pressed=}")
        if pressed == "STEP":
            STATE = STATE.onSTEP()

        elif pressed == "ENTER":
            STATE = STATE.onENTER()

        else:
            error()
    pressed = None
