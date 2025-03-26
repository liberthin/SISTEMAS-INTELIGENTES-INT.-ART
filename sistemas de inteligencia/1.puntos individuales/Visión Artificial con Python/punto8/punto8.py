import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread(r"C:\Users\liber\OneDrive\Escritorio\sistemas de inteligencia\1.puntos individuales\arcoiris.jpg", cv2.IMREAD_GRAYSCALE)

# Redimensionar la imagen para una mejor visualización
#imagen = cv2.resize(imagen, (500, 500))

# Aplicar detección de bordes con Canny
bordes = cv2.Canny(imagen, 50, 150)

# Encontrar contornos en la imagen con bordes detectados
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una imagen en color para visualizar los resultados
imagen_color = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

for contorno in contornos:
    # Calcular el área del objeto
    area = cv2.contourArea(contorno)
    
    # Calcular el perímetro del objeto
    perimetro = cv2.arcLength(contorno, True)
    
    # Aproximar la forma del contorno
    epsilon = 0.02 * perimetro
    approx = cv2.approxPolyDP(contorno, epsilon, True)
    
    # Dibujar el contorno y mostrar información en la imagen
    cv2.drawContours(imagen_color, [approx], -1, (0, 255, 0), 2)
    x, y, w, h = cv2.boundingRect(approx)
    cv2.putText(imagen_color, f"A:{int(area)} P:{int(perimetro)}", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# Mostrar la imagen con contornos y características
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Bordes Detectados', bordes)
cv2.imshow('Objetos detectados', imagen_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
