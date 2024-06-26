import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CASCADE_PATH = os.path.join(BASE_DIR, 'haarcascade_frontalface_default.xml')
LANDMARKS_PATH = os.path.join(BASE_DIR, 'shape_predictor_68_face_landmarks.dat')
