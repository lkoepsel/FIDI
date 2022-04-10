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
        button_D0.update()
        button_D1.update()
        if button_D0.rose:
            return "D0"
        if button_D1.rose:
            return "D1"
        else:
            return None


button_D0 = attach_Button(board.D0)
button_D1 = attach_Button(board.D1)
