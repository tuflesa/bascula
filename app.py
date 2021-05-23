from flask import Flask
from flask import jsonify
from flask_cors import CORS
import serial

app = Flask(__name__)
CORS(app)

def leer_bascula():
    try:
        bascula = serial.Serial('/dev/ttyUSB0', timeout=1)
        peso = bascula.readline()
        bascula.close()
        peso = peso.decode("utf-8")
        peso = int(peso[2:9])
    except:
        peso = 'Error de lectura de bascula'
    return peso

@app.route("/")
def bascula():
    return jsonify({'peso': leer_bascula()})
