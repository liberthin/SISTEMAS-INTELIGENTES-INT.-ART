import cv2 
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Copia del frame original para conservarlo sin modificaciones
    original = frame.copy()  # <-- Imagen original
    # Procesamiento para detección de contornos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)  # Frame modificado con contornos
    # Mostrar ambas imágenes: original y con contornos
    cv2.imshow('Original', original)          # Ventana con imagen original
    cv2.imshow('Con contornos', frame)         # Ventana con imagen procesada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
