import serial
import tkinter as tk

# Configura el puerto serial
try:
    ser = serial.Serial('COM2', 9600, timeout=1)
    print("Conexión serial establecida correctamente.")
except Exception as e:
    print(f"Error al abrir el puerto serial: {e}")
    exit()

# Función para encender el LED
def encender_led():
    ser.write(b'1')
    label_status.config(text="LED encendido", fg="green")

# Función para apagar el LED
def apagar_led():
    ser.write(b'0')
    label_status.config(text="LED apagado", fg="red")

# Crear la ventana principal
root = tk.Tk()
root.title("Control de LED y LDR")

# Botones para controlar el LED
btn_encender = tk.Button(root, text="Encender LED", command=encender_led)
btn_encender.pack(pady=10)

btn_apagar = tk.Button(root, text="Apagar LED", command=apagar_led)
btn_apagar.pack(pady=10)

# Etiqueta para mostrar el estado del LED
label_status = tk.Label(root, text="LED apagado", fg="red")
label_status.pack(pady=10)

# Etiqueta para mostrar el valor del LDR
label_ldr = tk.Label(root, text="Valor del LDR: -")
label_ldr.pack(pady=10)

# Función para actualizar el valor del LDR
def actualizar_ldr():
    if ser.in_waiting > 0:
        ldr_value = ser.readline().decode('utf-8').strip()
        label_ldr.config(text=f"Valor del LDR: {ldr_value}")
    root.after(100, actualizar_ldr)  # Actualiza cada 100 ms

# Iniciar la actualización del LDR
actualizar_ldr()

# Ejecutar la interfaz gráfica
root.mainloop()

# Cerrar el puerto serial al salir
ser.close()