import RPi.GPIO as GPIO
import time

SLEEP_TIME = 0.001
STEP_ANGLE = 1.8


GPIO.setmode(GPIO.BCM) # use BCM pin numbering
GPIO.setup(16, GPIO.OUT) # set GPIO 16 as output

def spin_minute_degrees(degrees):
    steps = 8 * 360/1.8 # 1.8 is angle per step, uses 1/8 microsteps as default
    steps =  (degrees/360) * steps # rotate a few times

    for ii in range(int(steps)):
        GPIO.output(16, GPIO.HIGH)
        time.sleep(SLEEP_TIME)

        GPIO.output(16, GPIO.LOW)
        time.sleep(SLEEP_TIME)

    return

if __name__ == "__main__":
    try:
        spin_minute_degrees(360)

    except KeyboardInterrupt:
        print("Exiting program")

    finally:
        GPIO.cleanup()