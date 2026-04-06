import RPi.GPIO as GPIO
from datetime import datetime

from camera import Camera
from motion_detector import check_motion
from led import led_on, led_off
from stepper import spin_minute_degrees


MOTION_PIN = 23
MOTION_LED_PIN = 24
CAMERA_LED_PIN = 25
STEP_PIN = 16
DIR_PIN = 12


def setup():

    camera = Camera()

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(MOTION_LED_PIN, GPIO.OUT)
    GPIO.setup(CAMERA_LED_PIN, GPIO.OUT)
    GPIO.setup(STEP_PIN, GPIO.OUT)
    GPIO.setup(DIR_PIN, GPIO.OUT)
    GPIO.setup(STEP_PIN, GPIO.OUT)

    return camera


def cleanup(camera):
    led_off(MOTION_LED_PIN)
    led_off(CAMERA_LED_PIN)

    camera.close_camera()

    GPIO.cleanup()

    return


def calibrate_hands():
    print("Use a/d for large moves, w/s for small moves, enter time (4 digit number) to quit")

    current_hands = 0000

    while True:
        key = input("Command: ").lower()

        if key == "a":
            spin_minute_degrees(5, "counter_clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key == "d":
            spin_minute_degrees(5, "clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key == "w":
            spin_minute_degrees(1, "counter_clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key == "s":
            spin_minute_degrees(1, "clockwise", "medium", STEP_PIN, DIR_PIN)
        elif key.isnumeric():
            current_hands = int(key)
            break

    return current_hands


def set_to_current_time(current_hands):
    # parse input time (e.g., 0430 → 4:30)
    current_hands = f"{current_hands:04d}"
    current_h = int(current_hands[:2]) % 12
    current_m = int(current_hands[2:])
    
    now = datetime.now()
    print(now)
    real_h = now.hour % 12
    real_m = now.minute

    current_angle = (current_h * 360) + (current_m * 6)
    target_angle = (real_h * 360) + (real_m * 6)
    print(current_angle, target_angle)

    min_value = 360
    max_value = 7860

    current_angle = current_angle - min_value
    target_angle = target_angle - min_value
    max_value = max_value - min_value

    diff = (current_angle - target_angle) % max_value  # Wrap between 0 and 360
    if diff > (max_value / 2):
        diff -= max_value

    print(diff)

    if diff < 0:
        spin_minute_degrees(abs(diff), "clockwise", "medium", STEP_PIN, DIR_PIN)
    elif diff > 0:
        spin_minute_degrees(abs(diff), "counter_clockwise", "medium", STEP_PIN, DIR_PIN)
    else:
        pass

    current_hands = int(f"{real_h}{real_m}")

    return current_hands


def main_loop():

    camera = setup()

    current_hands = calibrate_hands()

    try:
        while True:
            led_off(MOTION_LED_PIN)
            led_off(CAMERA_LED_PIN)

            while check_motion(MOTION_PIN):
                
                led_on(MOTION_LED_PIN)

                camera.capture_image()
                face = camera.detect_face()

                led_off(CAMERA_LED_PIN)

                while face:

                    led_on(CAMERA_LED_PIN)

                    current_hands = set_to_current_time(current_hands)

                    camera.capture_image()
                    face = camera.detect_face()


    except KeyboardInterrupt:
        print("\nLoop interrupted by user. Exiting gracefully...")

    finally:
        cleanup(camera)

    return


if __name__ == "__main__":
    main_loop()
    


