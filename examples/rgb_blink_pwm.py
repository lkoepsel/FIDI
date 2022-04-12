import time
import board
import pwmio


ON = 0
DIM = 60000
MED = 32768
OFF = 65535

# LED setup for most CircuitPython boards:
RED = pwmio.PWMOut(board.LED_R, frequency=1000, duty_cycle=OFF)
GREEN = pwmio.PWMOut(board.LED_G, frequency=1000, duty_cycle=OFF)
BLUE = pwmio.PWMOut(board.LED_B, frequency=1000, duty_cycle=OFF)


def bin_leds(value):
    if value == 0:
        RED.duty_cycle = OFF
        GREEN.duty_cycle = DIM
        BLUE.duty_cycle = OFF
    elif value == 1:
        RED.duty_cycle = OFF
        GREEN.duty_cycle = OFF
        BLUE.duty_cycle = ON
    elif value == 2:
        RED.duty_cycle = OFF
        GREEN.duty_cycle = MED
        BLUE.duty_cycle = OFF
    elif value == 3:
        RED.duty_cycle = OFF
        GREEN.duty_cycle = MED
        BLUE.duty_cycle = ON
    else:
        RED.duty_cycle = ON
        GREEN.duty_cycle = OFF
        BLUE.duty_cycle = OFF

while True:
    for i in range(5):
        bin_leds(i)
        print(f"{i=}")
        time.sleep(1)
