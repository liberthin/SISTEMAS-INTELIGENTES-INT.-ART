import serial
import time

# Configura la conexión serial
arduino = serial.Serial('COM2', 9600, timeout=1)  # Reemplaza 'COM3' con el puerto correcto
time.sleep(2)  # Espera a que se establezca la conexión

def move_servo(angle):
    if 0 <= angle <= 180:
        arduino.write(f"{angle}\n".encode())  # Envía el ángulo al Arduino
        response = arduino.readline().decode().strip()  # Lee la respuesta del Arduino
        print(response)
    else:
        print("Ángulo fuera de rango (0-180)")

# Bucle para control manual
while True:
    try:
        angle = int(input("Ingresa el ángulo (0-180): "))  # Solicita el ángulo al usuario
        move_servo(angle)  # Mueve el servomotor al ángulo especificado
    except ValueError:
        print("Entrada inválida. Ingresa un número entre 0 y 180.")
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
        break

# Cierra la conexión serial
arduino.close()