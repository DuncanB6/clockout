from picamera2 import Picamera2
import cv2
import time

def main():
    camera = Picamera2()

    camera.configure(camera.create_still_configuration(main={"format": "RGB888"}))

    camera.start()
    time.sleep(2)
    
    print("Annnnnnnd...")
    image = camera.capture_array()
    print("CLICK!")

    image = cv2.resize(image, (640, 360))
    cv2.imshow("Captured Image", image)
    cv2.waitKey(2000)
    
    cv2.destroyAllWindows()
    camera.close()

if __name__ == "__main__":
    main()


