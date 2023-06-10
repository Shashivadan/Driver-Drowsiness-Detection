import cv2
import dlib
import numpy as np
from flask import Flask, render_template, Response
from pygame import mixer

app = Flask(__name__)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

mixer.init()
mixer.music.load("warning.mp3")


def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


def detect_drowsiness(frame):
    '''this function will verify the person drowsy or not'''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray, 0)

    # Loop through each face
    for face in faces:
        # Detect facial landmarks for the face
        (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
        # Draw face detection square on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        landmarks = predictor(gray, face)
        # Extract the coordinates for the left and right eyes
        left_eye = [(landmarks.part(36).x, landmarks.part(36).y),
                    (landmarks.part(37).x, landmarks.part(37).y),
                    (landmarks.part(38).x, landmarks.part(38).y),
                    (landmarks.part(39).x, landmarks.part(39).y),
                    (landmarks.part(40).x, landmarks.part(40).y),
                    (landmarks.part(41).x, landmarks.part(41).y)]
        right_eye = [(landmarks.part(42).x, landmarks.part(42).y),
                     (landmarks.part(43).x, landmarks.part(43).y),
                     (landmarks.part(44).x, landmarks.part(44).y),
                     (landmarks.part(45).x, landmarks.part(45).y),
                     (landmarks.part(46).x, landmarks.part(46).y),
                     (landmarks.part(47).x, landmarks.part(47).y)]

        # Calculate the eye aspect ratio (EAR) for each eye
        left_ear = eye_aspect_ratio(np.array(left_eye))
        right_ear = eye_aspect_ratio(np.array(right_eye))
        avg_ear = (left_ear + right_ear) / 2.0

        # Check if the eye aspect ratio is below the threshold for eye closure
        if avg_ear < 0.26:
            return True
    return False


def generate_frames():
    cap = cv2.VideoCapture(0)
    drowsy = False
    ear_counter = 0
    ear_thresh = 20
    while True:
        success, frame = cap.read()
        if not success:
            break
        if detect_drowsiness(frame=frame):
            ear_counter += 1
            if ear_counter >= ear_thresh:
                if not drowsy:
                    mixer.music.play()
                drowsy = True
                cv2.putText(frame, "WARNING: Drowsiness Detected", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1,
                            (0, 0, 255), 2)
        else:
            ear_counter = 0
            if drowsy:
                mixer.music.stop()
            drowsy = False

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/about')
def about():
    return render_template('About.html')


if __name__ == "__main__":
    app.run(debug=True)
