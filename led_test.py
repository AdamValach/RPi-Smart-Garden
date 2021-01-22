import time
from gpiozero import InputDevice

moisture = InputDevice(14)

while True:
    if not moisture.is_active:
        print("Moisture detected!")
    else:
        print("Moisture not detected!")
    time.sleep(1)
