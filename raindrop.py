import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
sensor = 18

GPIO.setup(sensor, GPIO.IN)

while True:
    if GPIO.input(sensor) == 0:
        print("No Rain")
    else:
        print("Raining")
    time.sleep(1)