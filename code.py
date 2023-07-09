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
        if pressed == "ENTER":
            pressed = None
            print(pressed)
            count_UP += 1
            print(f"STEP count = {count_UP}")
            rgb('gb')

        elif pressed == "STEP":
            pressed = None
            print(pressed)
            count_ENTER += 1
            print(f"Enter count = {count_ENTER}")
            rgb('b')

        else:
            print(f"{pressed =}")
            rgb('gr')
