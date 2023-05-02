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

video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    color_bajo = np.array([0,100,20])
    color_alto = np.array([5,255,255])
    
    mascara = cv2.inRange(hsv_frame, color_bajo, color_alto)
    color = cv2.bitwise_and(frame, frame, mask=mascara)
    
    contorno, valor = cv2.findContours(
        mascara.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
        )
    
    frame = cv2.drawContours(frame, contorno, -1, (0,255,0), 3)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Rojo", color)
    
    if(cv2.waitKey(25) & 0xFF == ord('q')):
        break
    
video.release()
# cv2.waitKey()
cv2.destroyAllWindows()