import time
from gpiozero import InputDevice, OutputDevice

relay = OutputDevice(14)


def water_for_x_seconds(duration):
    relay.on()
    time.sleep(5)
    relay.off()


time.sleep(5)
water_for_x_seconds(5)
time.sleep(5)
water_for_x_seconds(5)
