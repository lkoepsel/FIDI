import time
import board
from analogio import AnalogIn

with AnalogIn(board.A2) as analog_in:

    while True:
        normalized = analog_in.value * 100 // 65535
        print(analog_in.value, normalized)
        time.sleep(0.5)
