#Rango de colores Rojo, Amarillo y Verde
'''
Verde Claro: 25,20,20
Verde Oscuro: 100,255,255

Azul Claro: 100,100,20
Azul Oscuro: 125,255,255

Rojo Claro: 0,100,20
Rojo Oscuro: 5,255,255

Rojo Claro2: 175,100,20
Rojo Oscuro2: 179,255,255

Amarillo Claro: 15,100,20
Amarillo Oscuro: 45,255,255
'''

import cv2
import numpy as np

img = cv2.imread("hoja.jpeg")

imagenhsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
VerdeClaro = np.array([25,20,20],np.uint8)
VerdeOscuro= np.array([100,255,255],np.uint8)

mascara = cv2.inRange(imagenhsv,VerdeClaro,VerdeOscuro)
kernel = np.ones((7,7),np.uint8)

mascara = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara,cv2.MORPH_OPEN, kernel)

seccionIMG = cv2.bitwise_and(img,img,mask=mascara)

contorno, valor=cv2.findContours(mascara.copy(),
                                 cv2.RETR_EXTERNAL, 
                                 cv2.CHAIN_APPROX_SIMPLE)

resultado = cv2.drawContours(seccionIMG, contorno,-1,(0,255,0),3)

cv2.namedWindow("Restultado",cv2.WINDOW_NORMAL)
cv2.imshow("Restultado",resultado)
cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow("Imagen",img)
cv2.waitKey()
cv2.destroyAllWindows()