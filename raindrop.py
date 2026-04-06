from time import sleep
from gpiozero import InputDevice

rain_sensor = InputDevice(18)

while True:
    if not rain_sensor.is_active:
        print("No Rain")
    else:
        print("Raining")

    sleep(1)