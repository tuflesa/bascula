import serial

bascula = serial.Serial('/dev/ttyUSB0')
peso = bascula.readline()
print(str(peso))

bascula.close()
