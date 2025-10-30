from picamera2 import Picamera2
import cv2
import time

class Camera:
    def __init__(self):
        self.image = None

        self.face_cascade_front = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt_tree.xml')

        self.camera = Picamera2()
        self.camera.configure(self.camera.create_still_configuration(main={"format": "RGB888"}))
        self.camera.start()

    def close_camera(self):
        self.camera.close()

    def capture_image(self):
        self.image = self.camera.capture_array()
        self.image = cv2.resize(self.image, (640, 360))
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def display_image(self, display_time):
        cv2.imshow("Captured Image", self.image)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

    def detect_face(self):
        
        # tuning:
        # - scaleFactor: how much is a region of the image enlarged between checks (higher -> faster, but more likely to miss faces)
        # - minNeighbours: how many filters need to hit in a region to confirm a face (higher -> fewer FPs, more FNs)
        # - minSize: min size of face (pixels) (lower detects faces farther away, more FPs)
        front_faces = self.face_cascade_front.detectMultiScale(self.image, scaleFactor=1.01, minNeighbors=3, minSize=(10, 10))
        print("faces:", len(front_faces))
        
        # draw rectangle on face
        for (x, y, w, h) in front_faces:
            print("yo a face!")
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)



if __name__ == "__main__":
    camera = Camera()
    while (1):
        camera.capture_image()
        camera.detect_face()
        camera.display_image(2000)
    
    camera.close_camera()



