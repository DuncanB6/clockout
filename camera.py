from picamera2 import Picamera2
import cv2
import time

class Camera:
    def __init__(self):
        self.image = None

        self.camera = Picamera2()
        self.camera.configure(self.camera.create_still_configuration(main={"format": "RGB888"}))

    def capture_image(self):
        self.camera.start()
        self.image = self.camera.capture_array()
        self.camera.close()

    def display_image(self, display_time):
        resized_image = cv2.resize(self.image, (640, 360))
        cv2.imshow("Captured Image", resized_image)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()





if __name__ == "__main__":
    camera = Camera()
    camera.capture_image()
    camera.display_image(2000)



