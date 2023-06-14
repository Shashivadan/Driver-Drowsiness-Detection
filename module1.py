import cv2
import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def eye_aspect_ratio(eye):

    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


def detect_drowsiness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)

    for face in faces:
        (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        landmarks = predictor(gray, face)

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

        left_ear = eye_aspect_ratio(np.array(left_eye))
        right_ear = eye_aspect_ratio(np.array(right_eye))
        avg_ear = (left_ear + right_ear) / 2.0

        if avg_ear < 0.25:
            return True
    return False
