""" show_ticks: demonstrate ticks
"""
from time import sleep
from adafruit_ticks import ticks_ms, ticks_add, ticks_less
import sys


on_delay = 10000
start_time = ticks_ms()
off_time = ticks_add(start_time, on_delay)
print(f"When {start_time=:,} > {off_time=:,}")

while True:
    # check button, if pressed respond appropriately
    if ticks_less(ticks_ms(), off_time):
        print(f"{ticks_ms()=:,} < {off_time=:,}")
    else:
        print(f"{ticks_ms()=:,} > {off_time=:,}")
        sys.exit()
    sleep(4)
