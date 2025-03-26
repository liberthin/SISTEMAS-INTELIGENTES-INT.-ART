import serial
import time

# Configurar el puerto serial (ajusta el puerto según tu sistema)
ser = serial.Serial('COM2', 9600, timeout=1)  # En Windows, usa 'COMX'. En Linux/Mac, usa '/dev/ttyUSBX' o similar.

try:
    while True:
        if ser.in_waiting > 0:  # Verificar si hay datos disponibles en el puerto serial
            line = ser.readline().decode('utf-8').strip()  # Leer la línea y decodificarla
            if line == "Button pressed!":
                print("El botón fue presionado!")  # Reaccionar al evento
        time.sleep(0.1)  # Pequeña pausa para evitar sobrecargar la CPU

except KeyboardInterrupt:
    print("Programa terminado por el usuario.")

finally:
    ser.close()  # Cerrar el puerto serial