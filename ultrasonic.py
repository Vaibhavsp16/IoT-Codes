import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trig_pin = 16
echo_pin = 18

GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

while True:
    GPIO.output(trig_pin, False)
    sleep(0.000002)

    GPIO.output(trig_pin, True)
    sleep(0.00001)
    GPIO.output(trig_pin, False)

    while GPIO.input(echo_pin) == 0:
        pulse_start = time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150

    print("Distance:", distance, "cm")

    sleep(1)