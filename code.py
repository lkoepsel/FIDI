# rgb_input - use to demonstrate rgb function
# enter r|g|b at terminal and appropriate led will light
import board
from RGB_led import rgb


while True:
    print(f"Enter r|g|b, one, two or all:")
    command = input()

    if command is not None:
        rgb(command)
