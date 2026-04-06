import RPi.GPIO as GPIO
import time


def led_on(led_pin):
    GPIO.output(led_pin, GPIO.HIGH)

    return

def led_off(led_pin):
    GPIO.output(led_pin, GPIO.LOW)

    return

if __name__ == "__main__":

    # Use BCM pin numbering
    GPIO.setmode(GPIO.BCM)

    # Set GPIO 24 as an output
    LED_PIN_1 = 24
    GPIO.setup(LED_PIN_1, GPIO.OUT)
    LED_PIN_2 = 25
    GPIO.setup(LED_PIN_2, GPIO.OUT)

    try:
        while(1):
            #led_on(LED_PIN_1)
            led_off(LED_PIN_2)
            time.sleep(1)
            #led_off(LED_PIN_1)
            led_on(LED_PIN_2)
            time.sleep(1)


    finally:
        print("Cleaning up GPIO...")
        led_off(LED_PIN_1)
        led_off(LED_PIN_2)
        GPIO.cleanup()