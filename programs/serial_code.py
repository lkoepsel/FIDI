import board
import busio
import digitalio


uart = busio.UART(board.TX, board.RX, baudrate=115200)


while True:
    data = uart.read(8)  # read up to 32 bytes
    print(len(data), data)  # this is a bytearray type

    if data is not None:
        led.value = False

        # convert bytearray to string
        # data_string = ''.join([chr(b) for b in data])
        # print(data_string, end="")

        led.value = True
