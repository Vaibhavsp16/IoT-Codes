import RPi.GPIO as GPIO
import time

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)

while True:
    if GPIO.input(sensor) == 0:
        print("Soil is dry")
    else:
        print("Soil is wet")
    time.sleep(1)