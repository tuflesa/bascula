from flask import Flask
from flask import jsonify
from flask_cors import CORS
from threading import Thread
import serial

app = Flask(__name__)
CORS(app)

thread = None

def serialThread():
    global peso
    
    peso = 0
    serialOK = True

    try:
        bascula = serial.Serial('/dev/ttyUSB0', timeout=1)
    except:
        serialOK = False

    while (True):
        if serialOK:
            lectura = bascula.readline()
            lectura = lectura.decode("utf-8")
            peso = int(lectura[2:9])
            
        else:
            peso = 'Error de puerto serie'

@app.route('/')
def index():
    global thread
    global peso

    if thread is None:
        thread = Thread(target=serialThread)
        thread.daemon = True
        thread.start()

    return jsonify({'peso':peso })
