import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer_pin = 23
GPIO.setup(buzzer_pin, GPIO.OUT)

while True:
    GPIO.output(buzzer_pin, GPIO.HIGH)
    print("Beep")
    sleep(0.5)

    GPIO.output(buzzer_pin, GPIO.LOW)
    print("No Beep")
    sleep(0.5)

