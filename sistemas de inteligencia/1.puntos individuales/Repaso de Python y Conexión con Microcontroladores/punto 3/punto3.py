import serial
import time

# Configura el puerto serial (ajusta el puerto COM según tu sistema)
arduino = serial.Serial('COM2', 9600, timeout=1)
time.sleep(2)  # Espera a que se establezca la conexión

try:
    while True:
        print(" 1) para andar\n 2) para ir atras\n 3) para frenar\n 4) para ajustar velocidad\n")
        
        ea = input("Ingrese el valor indicado: ")
        if ea == '1':
            arduino.write(b'F')
            print("Adelante")
        elif ea == '2':
            arduino.write(b'B')
            print("Atrás")
        elif ea == '3':
            arduino.write(b'S')
            print("Frenar")
        elif ea == '4':
            speed = input("Ingrese la velocidad (0-255): ")
            arduino.write(f'V{speed}'.encode())
            print(f"Velocidad ajustada a {speed}")
        else:
            print("Escriba un valor válido")
except Exception as e:
    print(f"Error: {e}")
finally:
    arduino.close()