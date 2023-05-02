import cv2
import numpy as np
import imutils

img = cv2.imread("practica8\img.jpg")
img2 = cv2.resize(img, (200,200))

alto, ancho, canales = img2.shape
angulo = 45

img_rotada = imutils.rotate_bound(img2, angulo)

cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
cv2.imshow("Imagen", img)

cv2.namedWindow("Imagen2", cv2.WINDOW_NORMAL)
cv2.imshow("Imagen2", img2)

cv2.namedWindow("Rotada", cv2.WINDOW_NORMAL)
cv2.imshow("Rotada", img_rotada)


cv2.waitKey()
cv2.destroyAllWindows()