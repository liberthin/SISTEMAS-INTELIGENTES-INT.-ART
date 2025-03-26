import serial
import matplotlib.pyplot as plt
import time

# Configuración del puerto serie (ajusta el nombre del puerto)
ser = serial.Serial('COM2', 9600)  # En Linux/Mac usa '/dev/ttyUSB0' o '/dev/ttyACM0'
time.sleep(2)  # Espera a que Arduino inicie

distances = []

plt.ion()  # Modo interactivo
fig, ax = plt.subplots()
line, = ax.plot(distances, label="Distancia (cm)")
ax.set_ylim(0, 200)  # Ajusta el rango según el sensor
ax.set_title("Medición en tiempo real")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Distancia (cm)")
ax.legend()

while True:
    try:
        data = ser.readline().decode().strip()  # Leer datos del puerto serie
        if data:
            distance = float(data)
            distances.append(distance)

            print(f"Distancia medida: {distance:.2f} cm")  # Imprimir en la terminal

            if len(distances) > 50:  # Mantener últimas 50 mediciones
                distances.pop(0)

            line.set_ydata(distances)
            line.set_xdata(range(len(distances)))
            ax.relim()
            ax.autoscale_view()
            plt.draw()
            plt.pause(0.1)  # Pequeña pausa para actualizar la gráfica

    except KeyboardInterrupt:
        print("Finalizando...")
        ser.close()
        break
