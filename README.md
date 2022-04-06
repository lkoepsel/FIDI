# CircuitPython on the Omzlo FIDI Board
## Introduction
The [Omzlo: FIDI](https://www.omzlo.com/articles/fidi-a-tiny-board-for-super-fast-prototyping-with-circuitpython) is quite attractive for prototyping due to its size, cost and relative power. It is based on the ATSAMD21 microcontroller which is an ARM M0+-based chip. Due to its specs (48Mhz/4MB Flash/32K RAM), you can easily and quickly program it using CircuitPython (or MicroPython). In my case, I'll be using CircuitPython to take advantage of a number of Adafruit boards. You will want to install the latest  using the  [CircuitPython Serpente](https://circuitpython.org/board/serpente/) and also get the latest [CircuitPython Library Bundle](https://circuitpython.org/libraries).

## Additional Library files
**RGB_serial**: *from RGB_serial import rgb*
Provides function rgb('r|g|b') to turn RGB led on or off. Any combination of rgb may be provided and for each letter, the appropriate led will turn on. If not provided, the appropriate led will be off. Uses the RX of the QWIC connector, not USB.