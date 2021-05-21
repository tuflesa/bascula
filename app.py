from flask import Flask
from flask import jsonify
import serial

app = Flask(__name__)

def leer_bascula():
    try:
        bascula = serial.Serial('COM3')
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