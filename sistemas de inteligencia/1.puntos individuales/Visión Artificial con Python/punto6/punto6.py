import cv2
import numpy as np

# Capturar el video desde la cámara o un archivo
cap = cv2.VideoCapture(0)  # Cambia "0" por el nombre del archivo si deseas procesar un video guardado

# Leer el primer frame y convertirlo a escala de grises
ret, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(prev_frame, (5, 5), 0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir frame a escala de grises y suavizar
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Calcular la diferencia absoluta entre frames consecutivos
    diff = cv2.absdiff(prev_frame, gray)
    
    # Aplicar un umbral para detectar regiones con movimiento
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    # Encontrar contornos en la imagen umbralizada
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filtrar ruido y pequeñas detecciones
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Mostrar los resultados
    cv2.imshow("Detección de Movimiento", frame)
    cv2.imshow("Diferencia", thresh)
    
    # Actualizar el frame previo
    prev_frame = gray
    
    # Salir con la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
