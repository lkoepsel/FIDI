# CircuitPython on the Omzlo FIDI Board
## Introduction
The [Omzlo: FIDI](https://www.omzlo.com/articles/fidi-a-tiny-board-for-super-fast-prototyping-with-circuitpython) is quite attractive for prototyping due to its size, cost and relative power. It is based on the ATSAMD21 microcontroller which is an ARM M0+-based chip. Due to its specs (48Mhz/4MB Flash/32K RAM), you can easily and quickly program it using CircuitPython (or MicroPython). In my case, I'll be using CircuitPython to take advantage of a number of Adafruit boards. You will want to install the latest  using [CircuitPython Serpente](https://circuitpython.org/board/serpente/) and also get the latest [CircuitPython Library Bundle](https://circuitpython.org/libraries).

## Library Files
**RGB_led:** 
```python
from RGB_led import rgb

rgb('b') 	# lights only blue led
rgb('gb') 	# lights both green and blue led
rgb('rgbn')	# does nothing, too many letters
rgb('')		# turns all leds off
```
**proto_buttons:**
```python
from proto_buttons import buttons

pressed = buttons()
if pressed != None:
    if pressed == "D0":
        count_UP += 1
        print(f"{count_UP =}")
        rgb('gb')
    elif pressed == "D1":
        count_ENTER += 1
        print(f"{count_ENTER =}")
        rgb('b')

    else:
        rgb('r')

```

## Using Library Files (lib/)
It's best to load the Library files using the mpy versions as they are smaller and faster to load. To do so, do the following:
```bash
mpy lib/filename.py
cp -X lib/filename.mpy /Volumes/CircuitPython/lib
```
## Example files
**analog_in:**
Demonstrates how to use analog input using a context manager. Not required for a small program, however, useful to use as it will release the pin per CircuitPython requirements.

**button_counter:**
Demonstrates how to use *proto_buttons buttons()*, sets up two buttons using the protoboard and counts each press, printing values over USB

**fsm:**
Simple, four state, finite state machine (fsm), implemented using a namedtuple. I used a namedtuple to identify the required parameters for the fsm. See file for more details.

**pwm:**
Example for pwm from Adafruit.

**rgb_blink:**
Shows how to blink any one of the three color leds.

**rgb_input:**
Handy example to enter *"r|g|b"* to see what color the combinations make. Uses USB port. Provides function rgb('r|g|b') to turn RGB led on or off. Any combination of *'rgb'* may be provided and for each letter, the appropriate led will turn on. If not provided, the appropriate led will be off.

**UART_read:**
Demonstrates how to use the QWIC RX/TX pins as a UART. Very slow to respond, has automatic reading of characters (reads w/o Enter).

