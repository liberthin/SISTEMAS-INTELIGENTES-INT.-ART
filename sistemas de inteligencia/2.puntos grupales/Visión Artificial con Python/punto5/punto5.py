import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread(r"C:\Users\liber\OneDrive\Escritorio\sistemas de inteligencia\2.puntos grupales\pina.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar el operador de Sobel en la dirección X e Y
sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)  # Bordes verticales
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)  # Bordes horizontales

# Convertir los gradientes absolutos para mejor visualización
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combinar ambas direcciones
sobel_combinado = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Mostrar las imágenes
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(sobel_x, cmap='gray')
plt.title('Bordes Verticales')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel_y, cmap='gray')
plt.title('Bordes Horizontales')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sobel_combinado, cmap='gray')
plt.title('Bordes Combinados')
plt.axis('off')

plt.show()
