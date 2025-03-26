import cv2
import cv2.data

imagen = cv2.imread(r"C:\Users\liber\OneDrive\Escritorio\sistemas de inteligencia\1.puntos individuales\moto.jpg", cv2.IMREAD_GRAYSCALE)
imagen2 = cv2.imread(r"C:\Users\liber\OneDrive\Escritorio\sistemas de inteligencia\1.puntos individuales\moto.jpg")

imagen = cv2.resize(imagen, (500, 500))
imagen2 = cv2.resize(imagen2, (500, 500))

suavizado = cv2.GaussianBlur(imagen,(5,5),1)
suavizado2 = cv2.GaussianBlur(imagen2,(5,5),1)

bordes = cv2.Canny(suavizado, 50,100)
bordes2 = cv2.Canny(suavizado2, 50,100)

bordes_suave = cv2.Canny(imagen, 50,150)
bordes_fuerte = cv2.Canny(imagen, 150,250)

contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contornos, -1,(0,255,0),2)

contornos, _ = cv2.findContours(bordes2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen2, contornos, -1,(255,255,0),2)

# Aplicar umbralización (thresholding)
_, umbral = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
_, umbral2 = cv2.threshold(imagen2, 127, 255, cv2.THRESH_BINARY)

#mostrar resultados
cv2.imshow('imagen original', imagen)
cv2.imshow('bordes con Canny', bordes)
cv2.imshow('bordes suaves', bordes_suave)
cv2.imshow('bordes fuertes', bordes_fuerte)
cv2.imshow('imagen color', imagen2)
#mostrar imagen con contornos
cv2.imshow('objetos detectados', imagen)

#mostrar imagen con umbral
cv2.imshow('Umbralización imagen 1', umbral)
cv2.imshow('Umbralización imagen 2', umbral2)

cv2.waitKey(0)
cv2.destroyAllWindows()
