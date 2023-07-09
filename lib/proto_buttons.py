# lib/proto_buttons - provides debounce and press for buttons on proto board
import board
from adafruit_debouncer import Debouncer
import digitalio
from time import sleep


def attach_Button(pin):
    def_pin = digitalio.DigitalInOut(pin)
    def_pin.direction = digitalio.Direction.INPUT
    def_pin.pull = digitalio.Pull.UP
    return Debouncer(def_pin)


def buttons():
    while True:
        button_STEP.update()
        button_ENTER.update()

        if button_STEP.rose:
            print(f"STEP")
            return "STEP"
        if button_ENTER.rose:
            print(f"ENTER")
            return "ENTER"
        else:
            sleep(1)
            return None


button_STEP = attach_Button(board.D3)
button_ENTER = attach_Button(board.D2)
