import gpiozero
from gpiozero import LED
from time import sleep

ziarovka = LED(18)

while True:
    print("Starting")
    ziarovka.on()
    print("Bulb on")
    sleep(1)
    ziarovka.off()
    print("Bulb off")
    sleep(1)
