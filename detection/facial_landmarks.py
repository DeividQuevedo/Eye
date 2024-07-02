import cv2
import dlib

# Carregar o detector de faces e o preditor de landmarks do dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def detect_landmarks(frame):
    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar faces na imagem em escala de cinza
    faces = detector(gray)
    
    # Iterar sobre as faces detectadas
    for face in faces:
        # Detectar landmarks para a face atual
        landmarks = predictor(gray, face)
        
        # Desenhar cada landmark na imagem
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
    
    return frame

# Função principal para capturar vídeo da câmera e aplicar detecção de landmarks
def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Aplicar detecção de landmarks
        result_frame = detect_landmarks(frame)
        
        cv2.imshow('Detecção de Landmarks', result_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
