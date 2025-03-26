import serial

# Configura el puerto serial (reemplaza 'COM3' con el puerto correcto)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    print("Conexión serial establecida correctamente.")
except Exception as e:
    print(f"Error al abrir el puerto serial: {e}")
    exit()

try:
    while True:
        # Solicita al usuario que ingrese un texto
        texto = input("Ingresa el texto para mostrar en la LCD: ")
        
        # Envía el texto a Arduino a través del puerto serial
        ser.write(f"{texto}\n".encode('utf-8'))  # Añade un salto de línea al final
        print(f"Texto enviado: {texto}")

except KeyboardInterrupt:
    # Cierra el puerto serial al interrumpir el programa
    ser.close()
    print("\nPuerto serial cerrado.")