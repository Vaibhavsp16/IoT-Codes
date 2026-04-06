# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO
from time import sleep

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led_pin = 8
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

# Run forever
while True:
    # Turn ON LED
    GPIO.output(led_pin, GPIO.HIGH)
    print("LED ON")
    sleep(1)

    # Turn OFF LED
    GPIO.output(led_pin, GPIO.LOW)
    print("LED OFF")
    sleep(1)