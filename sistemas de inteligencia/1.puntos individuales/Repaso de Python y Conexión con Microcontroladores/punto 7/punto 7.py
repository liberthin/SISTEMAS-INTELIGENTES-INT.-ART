import serial
import time
import threading

# Variable para almacenar los datos del sensor
sensor_data = ""

# Función para leer datos del puerto serial en segundo plano
def read_serial(arduino):
    global sensor_data
    while True:
        if arduino.in_waiting > 0:
            sensor_data = arduino.readline().decode('utf-8').rstrip()

try:
    # Conectar con el Arduino
    arduino = serial.Serial('COM2', 9600)
    time.sleep(2)  # Esperar a que el Arduino se inicialice
    print("Conexión establecida con el Arduino")

    # Iniciar un hilo para leer datos del puerto serial
    threading.Thread(target=read_serial, args=(arduino,), daemon=True).start()

    while True:
        print("\n1) Ver valores de temperatura y humedad")
        print("2) Controlar el motor")
        print("3) Prender y apagar el LED")
        print("4) Salir")
        comand = input("Indique la opción: ")

        if comand == '1':
            while True:
                print("\n1) Ver dato de temperatura y humedad")
                print("2) Salir")
                rem = input("Indique la opción: ")
                if rem == '1':
                    print(sensor_data)  # Mostrar los datos del sensor
                elif rem == '2':
                    break
                else:
                    print("Opción inválida")

        elif comand == '2':
            while True:
                print("\n1) Para andar")
                print("2) Para ir atrás")
                print("3) Para frenar")
                print("4) Salir")
                ea = input("Ingrese el valor indicado: ")
                if ea == '1':
                    arduino.write(b'F')
                    print("Motor hacia adelante")
                elif ea == '2':
                    arduino.write(b'B')
                    print("Motor hacia atrás")
                elif ea == '3':
                    arduino.write(b'S')
                    print("Motor detenido")
                elif ea == '4':
                    break
                else:
                    print("Escriba un valor válido")

        elif comand == '3':
            while True:
                print("\nIndique la función")
                print("1: Encendido")
                print("2: Apagado")
                print("3: Salir")
                ea2 = input("Ingrese el valor indicado: ")
                if ea2 == '1':
                    arduino.write(b'e')
                    print("Se encendió el LED")
                elif ea2 == '2':
                    arduino.write(b'a')
                    print("Se apagó el LED")
                elif ea2 == '3':
                    break
                else:
                    print("Escriba un valor válido")

        elif comand == '4':
            print("Hasta luego")
            break

        else:
            print("Comando inválido")

except serial.SerialException as e:
    print(f"Error al conectar con el Arduino: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Puerto serial cerrado")