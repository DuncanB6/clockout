import RPi.GPIO as GPIO
import time

PIN = 23  # BCM numbering

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Use PUD_UP instead if your button/signal pulls to ground

def check_motion():
    return GPIO.input(PIN)

if __name__ == "__main__":

    try:
        while True:
            state = check_motion()
            if state:
                print("HIGH")
            else:
                print("LOW")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nExiting...")

    finally:
        GPIO.cleanup()