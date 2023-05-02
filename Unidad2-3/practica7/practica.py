#-----Rango de colores Rojo, Amarillo y Verde----
#Verde claro: 25,20,20
#Verde obscuro: 100,255,255

#Azul claro: 100,100,20
#Azul obscuro: 125,255,255

#Rojo claro: 0,100,20
#Rojo obscuro: 5,255,255

#Rojo claro2: 175,100,20
#Rojo obscuro2: 179,255,255

import cv2
import numpy as np

img = cv2.imread("imgs/verde.jpg")

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

verde_claro = np.array([25,20,20], np.uint8)
verde_obscuro = np.array([100,255,255], np.uint8)

mascara = cv2.inRange(imghsv, verde_claro, verde_obscuro)
kernel = np.ones((7,7),np.uint8)

mascara = cv2.morphologyEx(
    mascara,
    cv2.MORPH_CLOSE,
    kernel
)
mascara = cv2.morphologyEx(
    mascara,
    cv2.MORPH_OPEN,
    kernel
)

seccion_img = cv2.bitwise_and(img, img, mask=mascara)

contorno, valor = cv2.findContours(
    mascara.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

resultado = cv2.drawContours(seccion_img, contorno, -1, (255,0,0), 3)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
