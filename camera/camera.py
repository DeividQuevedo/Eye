import cv2
from detection.facial_landmarks import detect_landmarks
from detection.eye_detection import detect_eyes_and_calculate_ear

class Camera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            raise Exception("Could not open video device")

    def __del__(self):
        if self.video.isOpened():
            self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if success:
            # Aplicar detecção de landmarks e cálculo de EAR
            frame = detect_eyes_and_calculate_ear(frame)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        else:
            return None
