import serial

bascula = serial.Serial('COM3')
peso = bascula.readline()
print(str(peso))

bascula.close()