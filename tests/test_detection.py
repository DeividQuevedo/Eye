import cv2

def capture_camera_image():
    cap = cv2.VideoCapture(0)  # Abrir a câmera padrão (0 para a primeira câmera disponível)

    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return None

    ret, frame = cap.read()  # Capturar um quadro da câmera
    cap.release()  # Liberar a câmera após captura

    if not ret:
        print("Não foi possível capturar um quadro da câmera.")
        return None

    return frame

def detect_faces(frame):
    # Carregar o classificador Haar Cascade para detecção de faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return frame

def main():
    print("Capturando imagem da câmera...")
    frame = capture_camera_image()

    if frame is not None:
        print("Detectando faces na imagem...")
        result_frame = detect_faces(frame)

        # Salvar a imagem resultante com as faces detectadas
        cv2.imwrite('detected_faces.jpg', result_frame)
        print("Imagem com faces detectadas salva como 'detected_faces.jpg'.")
    else:
        print("Não foi possível capturar a imagem da câmera.")

if __name__ == "__main__":
    main()
