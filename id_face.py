import cv2

def capture_and_detect_faces():

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    face_cascade_front = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    print("Press SPACE to capture and detect faces, or 'q' to quit")
    
    while True:

        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture frame")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # tuning:
        # scaleFactor: how much is a region of the image enlarged between checks (higher -> faster, but more likely to miss faces)
        # minNeighbours: how many filters need to hit in a region to confirm a face (higher -> fewer FPs, more FNs)
        # minSize: min size of face (pixels) (lower detects faces farther away, more FPs)
        faces = face_cascade_front.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(30, 30))
        
        # draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow("Face ID", frame)
        
        # wait for key
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_detect_faces()