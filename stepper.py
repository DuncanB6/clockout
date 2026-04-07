import RPi.GPIO as GPIO
import time


def spin_minute_degrees(degrees, direction, speed, step_pin, dir_pin):
    if direction == "clockwise":
        GPIO.output(dir_pin, GPIO.HIGH)
    elif direction == "counter_clockwise":
        GPIO.output(dir_pin, GPIO.LOW)

    if speed == "fast":
        sleep_time = 0.0001
    elif speed == "medium":
        sleep_time = 0.001
    elif speed == "slow":
        sleep_time = 0.005


    steps = 8 * 360/1.8 # 1.8 is angle per step, uses 1/8 microsteps as default
    steps =  (degrees/360) * steps # rotate a few times

    for ii in range(int(steps)):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(sleep_time)

        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(sleep_time)

    return

if __name__ == "__main__":
    SLEEP_TIME = 0.001
    STEP_ANGLE = 1.8

    GPIO.setmode(GPIO.BCM) # use BCM pin numbering
    GPIO.setup(16, GPIO.OUT) # set GPIO 16 as output
    GPIO.setup(12, GPIO.OUT)

    try:
        spin_minute_degrees(4320, "clockwise", "medium", 16, 12)

    except KeyboardInterrupt:
        print("Exiting program")

    finally:
        GPIO.cleanup()