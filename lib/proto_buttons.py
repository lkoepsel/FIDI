# lib/proto_buttons - provides debounce and press for buttons on proto board
import board
from adafruit_debouncer import Debouncer
import digitalio


def attach_Button(pin):
    def_pin = digitalio.DigitalInOut(pin)
    def_pin.direction = digitalio.Direction.INPUT
    def_pin.pull = digitalio.Pull.UP
    return Debouncer(def_pin)


def buttons():
    while True:
        button_D2.update()
        button_D3.update()
        if button_D2.rose:
            return "D2"
        if button_D3.rose:
            return "D3"
        else:
            return None


button_D2 = attach_Button(board.D2)
button_D3 = attach_Button(board.D3)
