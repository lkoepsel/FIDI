# analog_in - read an ADC pin and print the voltage
import time
import board
from analogio import AnalogIn

with AnalogIn(board.A0) as analog_in:

    while True:
        voltage = analog_in.value * 3.3 / 65535
        print(f'{analog_in.value}, {voltage: .2f}')
        time.sleep(2.0)
