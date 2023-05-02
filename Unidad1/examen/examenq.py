# Si la imagen es cuadrada, dejarla así, de lo contrario cambiar su tamaño a que su ancho y alto sean iguales.
# Partir la imagen en 3 tercios de forma vertical de los cuales las imágenes resultantes se guardarán con los nombres de tercio1, tercio2 y tercio3.
# La imagen tercio1, se convertirá en RGB y se mostrará los resultados en ventanas.
# La imagen tercio2, se convertirá en HSV y se mostrará los resultados en ventanas.
# La imagen tercio3, se cambiará su tamaño igual a la imagen original y se mostrará en escala de grises.

import cv2
import numpy as np

img = cv2.imread("mario.jpeg")
# cv2.imshow("original", img)

alto, ancho, canales = img.shape

if(alto != ancho):
    img = cv2.resize(img, (700,700), interpolation=cv2.INTER_AREA)
    cv2.imwrite("cuadrada.jpg", img)


alto1, ancho1, canales1 = img.shape

medida_tercio = int(ancho1/3)
tercio1 = img[0:alto1, 0:medida_tercio]
tercio2 = img[0:alto1, medida_tercio:medida_tercio*2]
tercio3 = img[0:alto1, medida_tercio*2:ancho1]
cv2.imwrite("tercio1.jpg", tercio1)
cv2.imwrite("tercio2.jpg", tercio2)
cv2.imwrite("tercio3.jpg", tercio3)

B,G,R = cv2.split(tercio1)
cv2.imshow("Rojo", R)
cv2.imshow("Verde", G)
cv2.imshow("Azul", B)

H,S,V = cv2.split(cv2.cvtColor(tercio2, cv2.COLOR_BGR2HSV))
cv2.imshow("H", H)
cv2.imshow("S", S)
cv2.imshow("V", V)

tercio3 = cv2.resize(tercio3, (ancho, alto), interpolation=cv2.INTER_AREA)
tercio3 = cv2.cvtColor(tercio3, cv2.COLOR_BGR2GRAY)
cv2.imshow("tercio3", tercio3)

cv2.waitKey()
cv2.destroyAllWindows()