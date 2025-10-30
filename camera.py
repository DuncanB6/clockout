from picamera2 import Picamera2
import cv2
import time

def main():
    camera = Picamera2()
    camera.configure(camera.create_preview_configuration())
    
    camera.start()
    time.sleep(2)
    
    image = camera.capture_array()
    
    cv2.imshow("Captured Image", image)
    print("Press any key to close the window...")
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    camera.close()

if __name__ == "__main__":
    main()
