# button_counter - count button presses, indicate an error with RED led
from RGB_led import rgb
from proto_buttons import buttons


count_UP = 0
count_ENTER = 0
print(f"Begin ")
while True:
    # check button, if pressed respond appropriately
    pressed = buttons()
    if (pressed is not None):
        if pressed == "STEP":
            count_UP += 1
            print(f"STEP count = {count_UP}")
            rgb('g')

        elif pressed == "ENTER":
            count_ENTER += 1
            print(f"ENTER count = {count_ENTER}")
            rgb('b')

        else:
            rgb('r')
        pressed = None
