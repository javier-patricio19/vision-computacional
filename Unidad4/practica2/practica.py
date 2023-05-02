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

video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
  
    if ret == False: break
    # img = cv2.imread("img.jpg")

    imagenhsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    rojoBajo1 = np.array([0,150,20], np.uint8)
    rojoAlto1 = np.array([10,255,255], np.uint8)
    rojoBajo2 = np.array([175,150,20], np.uint8)
    rojoAlto2 = np.array([179,255,255], np.uint8)


    mascaraRojo1 = cv2.inRange(imagenhsv, rojoBajo1, rojoAlto1)
    mascaraRojo2 = cv2.inRange(imagenhsv, rojoBajo2, rojoAlto2)
    mascara = cv2.add(mascaraRojo1,mascaraRojo2)
        
    kernel = np.ones((7,7),np.uint8)

    mascara = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE, kernel)
    mascara = cv2.morphologyEx(mascara,cv2.MORPH_OPEN, kernel)

    seccionIMG = cv2.bitwise_and(img,img,mask=mascara)
    
    seccionIMG[mascara>0] = (255,0,0)

    contorno, valor=cv2.findContours(
        mascara.copy(),
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)

    final = cv2.add(img, seccionIMG)
    
    cv2.namedWindow("Final",cv2.WINDOW_NORMAL)
    cv2.imshow("Final",final)
    cv2.namedWindow("Restultado",cv2.WINDOW_NORMAL)
    cv2.imshow("Restultado",seccionIMG)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
    
# cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
# cv2.imshow("Imagen",img)
# cv2.waitKey()
# cv2.destroyAllWindows()