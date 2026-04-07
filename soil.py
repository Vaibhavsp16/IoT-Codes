import RPi.GPIO as GPIO

# Setup
GPIO.setmode(GPIO.BOARD)

input_pin = 8
led1_pin = 36
led2_pin = 32

GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(led1_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led2_pin, GPIO.OUT, initial=GPIO.LOW)

# Run forever
try:
    while True:
        state = GPIO.input(input_pin)

        print(not state)

        GPIO.output(led1_pin, state)
        GPIO.output(led2_pin, not state)

except KeyboardInterrupt:
    GPIO.cleanup()