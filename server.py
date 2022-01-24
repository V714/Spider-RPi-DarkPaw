from flask import Flask, render_template, url_for, jsonify, request, redirect, Response
from flask.wrappers import Request
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
from getkey import getkey, keys
from calibrate import calibrate as clb
import step_functions
import threading
import Adafruit_PCA9685
from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import random as rnd
from camera import Camera
from test import get_data, eyelight, servo, make_a_step, change_direction, change_action, start_walking

app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app,cors_allowed_origins="*")

cors = CORS(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

accel = mpu6050(0x68)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
buzzer = GPIO.PWM(12,440)

file_found = False
servo_min = [300] * 12
servo_max = [300] * 12
data = ""
eyelight_bool=False



@app.route('/')
def index():
    return render_template("index.html")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/stream')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@socketio.on('data')
def handleData(data):
    global action
    global eyelight_bool
    key = data['key']

    if key == 'W':
        change_action("forward")
    elif key == 'S':
        change_action("backward")
    elif key == 'Q':
        change_action("forward_left")
    elif key == 'E':
        change_action("forward_right")
    elif key == 'Z':
        change_action("backward_left")
    elif key == 'C':
        change_action("backward_right")
    elif key == "SPACE":
        change_action("stay")
    elif key == "I":
        change_action("standup_front")
    elif key == "B":
        if eyelight_bool:
            eyelight(False)
        else:
            eyelight(True)
    key = ''


if __name__ == "__main__":
    get_data()
    change_direction(True)
    stop_moving = False
    moving = threading.Thread(target=start_walking, args= (lambda:stop_moving,))
    moving.start()
    socketio.run(app, host='0.0.0.0',port=777, debug=True)
