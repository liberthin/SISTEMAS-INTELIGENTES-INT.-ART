import cv2

# Inicializar la captura de video desde la cámara (0 = cámara por defecto)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()
    
    if not ret:
        print("Error: No se pudo capturar el frame.")
        break

    # Mostrar el frame en una ventana
    cv2.imshow("Captura en tiempo real", frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()

