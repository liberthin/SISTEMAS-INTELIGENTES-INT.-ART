import serial
import pandas as pd
from datetime import datetime
import time

# Configuración del puerto serial
try:
    ser = serial.Serial('COM2', 9600)  # Reemplaza 'COM3' con el puerto correcto
    ser.flushInput()
    print("Conexión serial establecida correctamente.")
except Exception as e:
    print(f"Error al abrir el puerto serial: {e}")
    exit()

# Lista para almacenar los datos
data = []

# Intervalo de tiempo para guardar los datos (en segundos)
save_interval = 10  # Guardar cada 10 segundos
last_save_time = time.time()

try:
    print("Leyendo datos del sensor. Los datos se guardarán automáticamente...")
    while True:
        # Lee una línea del puerto serial
        line = ser.readline().decode('utf-8').strip()
        
        # Obtiene el valor del sensor y la marca de tiempo
        sensor_value = int(line)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Almacena los datos en la lista
        data.append([timestamp, sensor_value])
        
        # Imprime los datos en la consola
        print(f"Timestamp: {timestamp}, Sensor Value: {sensor_value}")

        # Guardar automáticamente después de un intervalo de tiempo
        if time.time() - last_save_time >= save_interval:
            # Guarda los datos en un DataFrame
            df = pd.DataFrame(data, columns=['Timestamp', 'Sensor Value'])
            
            try:
                # Guarda los datos en un archivo de Excel
                df.to_excel('C:/Users/liber/OneDrive/Escritorio/arduino/puntos grupales/punto1/ldr_sensor_data.xlsx', index=False, engine='openpyxl')
                print(f"Datos guardados en 'C:/Users/liber/OneDrive/Escritorio/arduino/puntos grupales/punto1/ldr_sensor_data.xlsx' a las {timestamp}")
            except Exception as e:
                print(f"Error al guardar el archivo de Excel: {e}")
            
            # Reinicia el tiempo del último guardado
            last_save_time = time.time()

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cierra el puerto serial
    ser.close()
    print("Puerto serial cerrado.")