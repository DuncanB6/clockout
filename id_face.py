import cv2

def capture_and_detect_faces():
    # Initialize the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    # Check if webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    # Load the face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    print("Press SPACE to capture and detect faces, or 'q' to quit")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture frame")
            break
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in real-time (optional - shows detection while live)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangles around detected faces in live view
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display the frame
        cv2.imshow('Webcam - Press SPACE to capture, Q to quit', frame)
        
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord(' '):  # Space bar to capture
            # Take the current frame for analysis
            captured_frame = frame.copy()
            captured_gray = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the captured frame
            captured_faces = face_cascade.detectMultiScale(captured_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            # Check if faces were found
            if len(captured_faces) > 0:
                print(f"Captured image: Found {len(captured_faces)} face(s)")
                
                # Draw rectangles around faces in captured image
                for (x, y, w, h) in captured_faces:
                    cv2.rectangle(captured_frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                
                # Save the captured image with detection
                cv2.imwrite('captured_with_faces.jpg', captured_frame)
                print("Saved captured image as 'captured_with_faces.jpg'")
                
                # Show the captured result
                cv2.imshow('Captured Image with Face Detection', captured_frame)
                
            else:
                print("Captured image: No faces found")
                cv2.imwrite('captured_no_faces.jpg', captured_frame)
                print("Saved captured image as 'captured_no_faces.jpg'")
        
        elif key == ord('q'):  # 'q' to quit
            break
    
    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_detect_faces()