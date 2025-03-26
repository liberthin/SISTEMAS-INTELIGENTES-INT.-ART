import serial
import time
from datetime import datetime

# Configuración
UMBRAL_TEMP = 30.0  # °C
UMBRAL_HUM = 70.0   # %
PUERTO = 'COM2'      # Cambiar por tu puerto

def log_alerta(mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {mensaje}")
    with open("alertas.log", "a") as f:
        f.write(f"[{timestamp}] {mensaje}\n")

def monitor_serial():
    try:
        ser = serial.Serial(PUERTO, 9600, timeout=1)
        print("Monitor de Temperatura/Humedad iniciado...")
        print(f"Umbrales: Temp > {UMBRAL_TEMP}°C | Hum > {UMBRAL_HUM}%")
        
        while True:
            if ser.in_waiting > 0:
                linea = ser.readline().decode('utf-8').strip()
                
                # Procesar datos normales (temperatura,humedad)
                if "," in linea and "ALERTA" not in linea:
                    try:
                        temp, hum = map(float, linea.split(","))
                        print(f"Temperatura: {temp:.1f}°C | Humedad: {hum:.1f}%")
                        
                        # Verificar umbrales
                        if temp > UMBRAL_TEMP:
                            log_alerta(f"Temperatura ALTA: {temp:.1f}°C")
                        if hum > UMBRAL_HUM:
                            log_alerta(f"Humedad ALTA: {hum:.1f}%")
                            
                    except ValueError:
                        print(f"Dato inválido: {linea}")
                
                # Procesar alertas directas desde Arduino
                elif "ALERTA_TEMP" in linea:
                    log_alerta("Alerta de temperatura desde Arduino!")
                elif "ALERTA_HUM" in linea:
                    log_alerta("Alerta de humedad desde Arduino!")
                    
    except serial.SerialException as e:
        print(f"Error de conexión: {e}")
    except KeyboardInterrupt:
        print("Monitor detenido por el usuario")

if __name__ == "__main__":
    monitor_serial()