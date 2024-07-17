import boto3
import base64
from datetime import datetime
import cv2

# Inicializar cliente DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

# Referência à tabela
table = dynamodb.Table('EyesMining')

def store_detection_data(face_id, image_data, eyes_open, drowsiness_level):
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    timestamp = datetime.utcnow().isoformat()
    
    item = {
        '3y3sm1n1ngk3y': face_id,
        'timestamp': timestamp,
        'image_data': encoded_image,
        'detection_results': {
            'eyes_open': eyes_open,
            'drowsiness_level': drowsiness_level
        }
    }
    
    table.put_item(Item=item)

def capture_image():
    # Captura da imagem usando OpenCV
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        ret, buffer = cv2.imencode('.jpg', frame)
        image_data = buffer.tobytes()
        cap.release()
        return image_data
    else:
        cap.release()
        raise RuntimeError("Failed to capture image")

# Exemplo de uso
if __name__ == "__main__":
    face_id = 'unique_face_id'
    try:
        image_data = capture_image()
        eyes_open = True
        drowsiness_level = 0.2
        
        store_detection_data(face_id, image_data, eyes_open, drowsiness_level)
        print("Dados armazenados com sucesso!")
    except Exception as e:
        print(f"Erro ao capturar ou armazenar dados: {e}")
