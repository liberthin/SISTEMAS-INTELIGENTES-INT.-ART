import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread(r"C:\Users\liber\OneDrive\Escritorio\sistemas de inteligencia\1.puntos individuales\imagen.jpg")

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización (Thresholding)
_, umbralizada = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos
contornos, _ = cv2.findContours(umbralizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos sobre la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

# Mostrar imágenes
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Umbralización", umbralizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
