from pygame import mixer
import cv2
from module1 import detect_drowsiness



mixer.init()
mixer.music.load("warning.mp3")


def generate_frames():
    cap = cv2.VideoCapture(0)
    drowsy = False
    ear_counter = 0
    ear_thresh = 15

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
