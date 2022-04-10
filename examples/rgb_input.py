# rgb_input - use to demonstrate rgb function
# enter r|g|b at terminal and appropriate led will light
import board
from RGB_led import rgb


while True:
    command = input()

    if command is not None:
        rgb(command)
