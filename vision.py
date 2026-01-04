import cv2
import datetime
import os



def start_face_detection():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    print("Press 'q' to quit face detection...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("JARVIS Vision - Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
def take_screenshot():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if ret:
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(folder, f"screenshot_{timestamp}.png")
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved as {filename}")
    else:
        print("Failed to take screenshot.")
    
    cap.release()
    cv2.destroyAllWindows()
    
# x= start_face_detection()
# y=take_screenshot()