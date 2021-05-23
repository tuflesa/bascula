import serial

bascula = serial.Serial('/dev/ttyUSB0', timeout=1)
peso = bascula.readline()
print(str(peso))

bascula.close()
