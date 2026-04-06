import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led1_pin = 8
led2_pin = 16

GPIO.setup(led1_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led2_pin, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(led1_pin, GPIO.HIGH)
    GPIO.output(led2_pin, GPIO.LOW)
    sleep(1)

    GPIO.output(led1_pin, GPIO.LOW)
    GPIO.output(led2_pin, GPIO.HIGH)
    sleep(1)