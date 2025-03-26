import serial
import time

# Configuración del puerto serie (ajusta según tu sistema operativo)
ser = serial.Serial('COM3', 9600, timeout=1)  # En Linux/Mac usa '/dev/ttyUSB0' o '/dev/ttyACM0'
time.sleep(2)  # Esperar a que Arduino inicie

try:
    while True:
        data = ser.readline().decode().strip()  # Leer datos del puerto serie
        if data:
            print(data)  # Imprimir temperatura y velocidad del ventilador en la terminal

except KeyboardInterrupt:
    print("Finalizando...")
    ser.close()