import board
import busio
from RGB_serial import rgb


uart = busio.UART(board.TX, board.RX, baudrate=115200)

while True:
    data = uart.read(4)  # read up to 4 bytes

    if data is not None:
        print(len(data), data)

        rgb(data)