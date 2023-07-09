# button_counter - count button presses, indicate an error with RED led
from RGB_led import rgb
from proto_buttons import buttons


count_UP = 0
count_ENTER = 0
print(f"Begin ")
while True:
    print(f"Loop:")
    # check button, if pressed respond appropriately
    pressed = buttons()
    print(f"{pressed=}")
    if (pressed is not None):
        if pressed == "STEP":
            pressed = None
            count_UP += 1
            print(f"STEP count = {count_UP}")
            rgb('g')

        elif pressed == "ENTER":
            pressed = None
            count_ENTER += 1
            print(f"ENTER count = {count_ENTER}")
            rgb('b')

        else:
            rgb('r')
