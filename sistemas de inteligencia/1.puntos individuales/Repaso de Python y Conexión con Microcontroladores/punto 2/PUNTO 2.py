import serial
import time

# Configurar el puerto serial
try:
    arduino = serial.Serial('COM2', 9600)
    time.sleep(2)
    print("Conexión establecida con el Arduino")
except serial.SerialException as e:
    print(f"Error al conectar con el Arduino: {e}")
    exit()

def leer_datos():
    while True:
        if arduino.in_waiting > 0:  # Verificar si hay datos disponibles
            linea = arduino.readline().decode('utf-8').rstrip()  # Leer y decodificar la línea
            print(linea)  # Mostrar la línea en la terminal de Python

try:
    leer_datos()
except KeyboardInterrupt:
    print("Programa terminado")