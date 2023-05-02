# dibujar el contorno de la imagen y escribir que color es

import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    a, frame = video.read()
    
    if a == False:
        break
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_claro = np.array([100,100,20],np.uint8)
    color_obscuro= np.array([125,255,255],np.uint8)
    
    mascara = cv2.inRange(hsv,color_claro, color_obscuro)
    kernel = np.ones((7,7),np.uint8)

    mascara = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE, kernel)
    mascara = cv2.morphologyEx(mascara,cv2.MORPH_OPEN, kernel)

    seccionIMG = cv2.bitwise_and(frame, frame ,mask=mascara)
    
    contorno, valor=cv2.findContours(mascara.copy(),
                                 cv2.RETR_EXTERNAL, 
                                 cv2.CHAIN_APPROX_SIMPLE)

    resultado = cv2.drawContours(frame, contorno,-1,(0,255,0),3)
    
    alto, ancho, canales = frame.shape
    cx = int(ancho / 2)
    cy = int(alto / 2)
    centro = hsv[cy,cx]
    canal_H= centro[0]
    print(canal_H)
    color = ""
    if canal_H < 5:
        color = "Rojo"
    elif canal_H <22:
        color = "Naranja"
    elif canal_H < 33:
        color = "Amarillo"
    elif canal_H < 78:
        color = "Verde"
    elif canal_H < 131:
        color = "Azul"
    elif canal_H < 167:
        color = "Violeta"
    else:
        color = "Rojo"
    b,g,r = int(centro[0]), int(centro[1]), int(centro[2]) 
    cv2.putText(frame,color,(10,50),0, 1, (0,0,255),2)
    cv2.circle(frame,(cx,cy),5,(0,0,255),2)
    
    cv2.namedWindow("video", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("mascara", cv2.WINDOW_NORMAL)
    
    cv2.imshow("video", frame)
    # cv2.imshow("mascara", resultado)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()