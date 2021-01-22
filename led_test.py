import gpiozero
from gpiozero import LED
from time import sleep

ziarovka = LED(18)

while True:
    ziarovka.on()
    sleep(1)
    ziarovka.off()
    sleep(1)
