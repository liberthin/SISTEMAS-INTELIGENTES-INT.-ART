import cv2
# Inicializar la captura desde la cámara web
cap = cv2.VideoCapture(0)
while True:
    # Leer un frame del video
    ret, frame = cap.read()
    if not ret:
        break
    # 1. Aplicar filtro Gaussiano 
    Suavisado = cv2.GaussianBlur(frame, (3, 3), 0)
    # 2. Convertir a escala de grises
    gray = cv2.cvtColor(Suavisado, cv2.COLOR_BGR2GRAY)
     # 3. Detección de bordes con Canny
    Bordes = cv2.Canny(gray, 50, 150)
    # Mostrar cada etapa en ventanas separadas
    cv2.imshow('Imagen Original', frame)
    cv2.imshow('Suavizado Gaussiano', Suavisado)
    cv2.imshow('Bordes Canny', Bordes)
    # Salir del bucle con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar recursos
cap.release()
cv2.destroyAllWindows()
