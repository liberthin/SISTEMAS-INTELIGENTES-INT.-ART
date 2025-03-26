import cv2
import numpy as np

# Inicializar la captura de video desde la cámara (0 = cámara por defecto)
cap = cv2.VideoCapture(0)

# Definir el rango de color a detectar (en formato HSV)
# Ejemplo: Rojo
lower_color = np.array([0, 120, 70], np.uint8)
upper_color = np.array([10, 255, 255], np.uint8)

#verde
#lower_color = np.array([36, 100, 100], np.uint8)
#upper_color = np.array([86, 255, 255], np.uint8)

#azul
#lower_color = np.array([100, 150, 0], np.uint8)
#upper_color = np.array([140, 255, 255], np.uint8)



while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: No se pudo capturar el frame.")
        break

    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear una máscara para detectar el color dentro del rango
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Aplicar la máscara sobre la imagen original
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar los resultados
    cv2.imshow("Video Original", frame)
    cv2.imshow("Detección de Color", result)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
