import RPi.GPIO as GPIO
import time

SLEEP_TIME = 0.0001
STEP_ANGLE = 1.8


GPIO.setmode(GPIO.BCM) # use BCM pin numbering
GPIO.setup(16, GPIO.OUT) # set GPIO 16 as output

steps = 8 * 360/1.8 # 1.8 is angle per step, uses 1/8 microsteps as default
print(steps)

try:
    for ii in range(int(100*steps)):
        GPIO.output(16, GPIO.HIGH)
        time.sleep(SLEEP_TIME)

        GPIO.output(16, GPIO.LOW)
        time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
    print("Exiting program")

finally:
    GPIO.cleanup()