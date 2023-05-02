import cv2
import numpy as np

img = cv2.imread("practica8\img.jpg")
img2 = cv2.resize(img, (200,200))

alto, ancho, canales = img2.shape


angulo = 30
centro = (ancho // 2, alto // 2)
escala = 1

rotacion = cv2.getRotationMatrix2D(centro, angulo, escala)
print(rotacion)
img_rotacion = cv2.warpAffine(img2, rotacion, (ancho, alto))

cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
cv2.imshow("Imagen", img)

cv2.namedWindow("Imagen2", cv2.WINDOW_NORMAL)
cv2.imshow("Imagen2", img2)

cv2.namedWindow("Rotada", cv2.WINDOW_NORMAL)
cv2.imshow("Rotada", img_rotacion)

cv2.waitKey()
cv2.destroyAllWindows()