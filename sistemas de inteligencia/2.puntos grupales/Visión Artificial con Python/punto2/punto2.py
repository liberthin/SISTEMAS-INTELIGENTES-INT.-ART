import cv2
import numpy as np


def Dibujo_casa_sol(image):
    # Dibujar la casa
    cv2.rectangle(image, (150, 250), (350, 400), (255, 255, 0), -1)  # Cuerpo de la casa
    cv2.line(image, (150, 250), (250, 150), (20,42 , 255), 5)  # Techo
    cv2.line(image, (350, 250), (250, 150), (20, 42, 255), 5)
    cv2.rectangle(image, (230, 320), (270, 400), (0, 255, 0), -1)  # Puerta
   
    # Dibujar el sol
    cv2.circle(image, (400, 100), 40, (0, 255, 255), -1)  # Sol
    return image




image = np.ones((500, 500, 3), dtype=np.uint8) * 255
image = Dibujo_casa_sol(image)
cv2.imshow('Original', image)


# Rotar la imagen 90 grados en sentido horario


rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotada 90°', rotated)


# Escalar la imagen al 50% del tamaño original


scaled = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)
cv2.imshow('Escalada 50%', scaled)


# Trasladar la imagen 50 píxeles a la derecha y 30 hacia abajo


M = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(image, M, (500, 500))
cv2.imshow('Trasladada', translated)


cv2.waitKey(0)
cv2.destroyAllWindows()
