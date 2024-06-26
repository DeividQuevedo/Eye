from flask import Flask, render_template, Response
import cv2
import dlib

app = Flask(__name__)

camera = None  # Variável global para armazenar o objeto de captura de vídeo
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # Arquivo com o modelo de predição de pontos faciais

def get_camera():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)  # Inicializa a câmera apenas uma vez

def detect_landmarks(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    
    for rect in rects:
        landmarks = predictor(gray, rect)
        for i in range(68):  # Número de pontos faciais no modelo usado
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
    
    return frame

def gen_frames():
    get_camera()  # Garante que a câmera seja inicializada antes de gerar os frames
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = detect_landmarks(frame)  # Chama a função para detectar pontos faciais no frame
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
