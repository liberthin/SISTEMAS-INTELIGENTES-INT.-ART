import cv2

image = cv2.imread(r'C:\Users\liber\OneDrive\Escritorio\sistemas de inteligencia\2.puntos grupales\12.jpg')

cv2.imshow("Imagen Original", image)

b, g, r = cv2.split(image)
cv2.imshow("Componente R", r)
cv2.imshow("Componente G", g)
cv2.imshow("Componente B", b)

cv2.waitKey(0)
cv2.destroyAllWindows()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
cv2.imshow("Componente H", h)
cv2.imshow("Componente S", s)
cv2.imshow("Componente V", v)
cv2.imshow("Imagen Original", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l, a, b_lab = cv2.split(lab_image)
cv2.imshow("Componente L", l)
cv2.imshow("Componente A", a)
cv2.imshow("Componente B (LAB)", b_lab)
cv2.imshow("Imagen Original",lab_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(ycrcb_image)
cv2.imshow("Componente Y", y)
cv2.imshow("Componente Cr", cr)
cv2.imshow("Componente Cb", cb)
cv2.imshow("Imagen Original", ycrcb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

xyz_image = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
x, y_xyz, z = cv2.split(xyz_image)
cv2.imshow("Componente X", x)
cv2.imshow("Componente Y (XYZ)", y_xyz)
cv2.imshow("Componente Z", z)
cv2.imshow("Imagen Original", xyz_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

altura, ancho, canales = image.shape
print(f"Ancho de la imagen: {ancho}")
print(f"Alto de la imagen: {altura}")
print(f"Canales de la imagen: {canales}")

cv2.waitKey(0)
cv2.destroyAllWindows()
