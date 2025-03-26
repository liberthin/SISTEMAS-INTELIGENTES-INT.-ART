import serial
import time
import random

# Configuración del puerto serial
ser = serial.Serial('COM2', 9600)  # Cambia 'COM3' al puerto correcto
time.sleep(2)  # Esperar a que se establezca la conexión

if ser.is_open:
    print("Puerto serial abierto correctamente.")
else:
    print("Error: No se pudo abrir el puerto serial.")

def generar_datos_sensor():
    # Simular datos de sensores
    temperatura = random.uniform(20.0, 30.0)  # Temperatura entre 20 y 30 grados
    humedad = random.uniform(40.0, 60.0)      # Humedad entre 40% y 60%
    luz = random.uniform(0.0, 100.0)          # Intensidad de luz entre 0 y 100
    return temperatura, humedad, luz

def enviar_datos_arduino():
    while True:
        temperatura, humedad, luz = generar_datos_sensor()
        
        # Formatear los datos como una cadena separada por comas
        datos = f"{temperatura:.2f},{humedad:.2f},{luz:.2f}\n"
        
        # Enviar los datos al Arduino
        ser.write(datos.encode('utf-8'))
        
        print(f"Enviado: {datos.strip()}")
        
        # Esperar un momento antes de enviar el siguiente conjunto de datos
        time.sleep(2)

if __name__ == "__main__":
    try:
        enviar_datos_arduino()
    except KeyboardInterrupt:
        print("Programa terminado")
    finally:
        ser.close()