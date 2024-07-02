import cv2
import dlib
import numpy as np

# Importar funções de detecção de face e landmarks
from detection.facial_landmarks import detector, predictor

class EARCalculator:
    @staticmethod
    def eye_aspect_ratio(eye):
        # Calcular as distâncias entre os pontos do olho para o cálculo do EAR
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def calculate_ear(self, landmarks):
        # Extrair os pontos dos olhos para o cálculo do EAR
        left_eye = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                             (landmarks.part(37).x, landmarks.part(37).y),
                             (landmarks.part(38).x, landmarks.part(38).y),
                             (landmarks.part(39).x, landmarks.part(39).y),
                             (landmarks.part(40).x, landmarks.part(40).y),
                             (landmarks.part(41).x, landmarks.part(41).y)])
        
        right_eye = np.array([(landmarks.part(42).x, landmarks.part(42).y),
                              (landmarks.part(43).x, landmarks.part(43).y),
                              (landmarks.part(44).x, landmarks.part(44).y),
                              (landmarks.part(45).x, landmarks.part(45).y),
                              (landmarks.part(46).x, landmarks.part(46).y),
                              (landmarks.part(47).x, landmarks.part(47).y)])
        
        # Calcular EAR para cada olho
        left_ear = self.eye_aspect_ratio(left_eye)
        right_ear = self.eye_aspect_ratio(right_eye)
        
        # Calcular EAR médio
        return (left_ear + right_ear) / 2.0

def detect_eyes_and_calculate_ear(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    ear_calculator = EARCalculator()

    for face in faces:
        landmarks = predictor(gray, face)
        ear = ear_calculator.calculate_ear(landmarks)

        # Alterar a cor dos pontos para vermelho se os olhos estiverem fechados (EAR < 0.2, por exemplo)
        if ear < 0.2:
            color = (0, 0, 255)  # Vermelho
        else:
            color = (0, 255, 0)  # Verde
        
        # Desenhar landmarks dos olhos
        for n in range(36, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, color, -1)

        # Mostrar EAR no frame
        cv2.putText(frame, f'EAR: {ear:.2f}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    return frame
