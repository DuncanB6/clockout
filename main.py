import RPi.GPIO as GPIO
import time

from camera import Camera
from motion_detector import check_motion
from led import led_on, led_off
from stepper import spin_minute_degrees


MOTION_PIN = 23
MOTION_LED_PIN = 24
CAMERA_LED_PIN = 25
STEP_PIN = 16


def setup():

    camera = Camera()

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(MOTION_LED_PIN, GPIO.OUT)
    GPIO.setup(CAMERA_LED_PIN, GPIO.OUT)
    GPIO.setup(STEP_PIN, GPIO.OUT)

    return camera



def main_loop():

    camera = setup()

    try:
        while True:
            led_on(MOTION_LED_PIN)
            led_on(CAMERA_LED_PIN)

            camera.capture_image()
            face = camera.detect_face()
            print("Face detected?", face)

            motion = check_motion(MOTION_PIN)
            print("Motion detected?", motion)

            spin_minute_degrees(90)

            led_off(MOTION_LED_PIN)
            led_off(CAMERA_LED_PIN)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nLoop interrupted by user. Exiting gracefully...")

    finally:
        cleanup(camera)

    return


def cleanup(camera):
    led_off(MOTION_LED_PIN)
    led_off(CAMERA_LED_PIN)

    camera.close_camera()

    GPIO.cleanup()

    return


if __name__ == "__main__":
    main_loop()
    


