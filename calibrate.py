

from stepper import spin_minute_degrees
from main import setup, cleanup


MOTION_PIN = 23
MOTION_LED_PIN = 24
CAMERA_LED_PIN = 25
STEP_PIN = 16
DIR_PIN = 12

def calibrate_hands():
    print("Use a/d for large moves, w/s for small moves, enter time (4 digit number) to complete calibration")

    current_hands = 0000

    while True:
        key = input("Command: ").lower()

        if key == "a":
            spin_minute_degrees(30, "counter_clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key == "d":
            spin_minute_degrees(30, "clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key == "w":
            spin_minute_degrees(5, "counter_clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key == "s":
            spin_minute_degrees(5, "clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key.isnumeric():
            current_hands = int(key)
            break

    print("Calibration complete!")

    return current_hands


if __name__ == "__main__":
    camera = setup()

    calibrate_hands()

    cleanup(camera)