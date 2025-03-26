import cv2
import numpy as np

# Capturar video desde la cámara (0 para la cámara predeterminada)
cap = cv2.VideoCapture(0)

# Crear un objeto para restar el fondo (detección de movimiento)
fmov = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar el sustractor de fondo
    fgmask = fmov.apply(gray)

    # Filtrar ruido con una operación morfológica
    fgmask = cv2.medianBlur(fgmask, 5)

    # Encontrar contornos de los objetos en movimiento
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignorar objetos muy pequeños
        if cv2.contourArea(contour) < 500:
            continue

        # Obtener el rectángulo delimitador del objeto detectado
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Dibujar un punto central para rastreo
        center = (x + w // 2, y + h // 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

    # Mostrar los resultados
    cv2.imshow("Detección de Movimiento", frame)
    cv2.imshow("Máscara de Movimiento", fgmask)

    # Salir con la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
