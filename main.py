from flask import Flask, render_template, Response
from module2 import generate_frames

app = Flask(__name__)


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


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)
