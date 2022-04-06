# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio

# LED setup for most CircuitPython boards:
ledG = pwmio.PWMOut(board.LED_G, frequency=5000, duty_cycle=0)
ledR = pwmio.PWMOut(board.LED_R, frequency=5000, duty_cycle=0)


while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            ledG.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            ledR.duty_cycle = int(i * 2 * 65535 / 100)  # Down
        else:
            ledG.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            ledR.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100) # Up
        time.sleep(0.05)
