import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM mode)
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number
led_pin = 17

# Set the GPIO pin as output
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Toggle the LED on and off
    while True:
        print("Toggling LED")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
