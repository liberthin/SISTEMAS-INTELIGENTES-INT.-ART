import serial
import time

# Configura el puerto serial
ser = serial.Serial('COM2', 9600, timeout=1)
time.sleep(2)  # Espera a que se establezca la conexión


temperatura = 25.5
humedad = 60.0
luz = 75.0


# Envía los datos al microcontrolador
datos = f"{temperatura},{humedad},{luz}\n"
ser.write(datos.encode())

# Cierra la conexión
ser.close()