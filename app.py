from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

camera = None  # Variável global para armazenar o objeto de captura de vídeo

def get_camera():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)  # Inicializa a câmera apenas uma vez

def gen_frames():
    get_camera()  # Garante que a câmera seja inicializada antes de gerar os frames
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
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
