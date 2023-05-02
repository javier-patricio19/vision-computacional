import cv2
import numpy as np
from datetime import datetime

video = cv2.VideoCapture("video.mp4")
contador = 0
while video.isOpened():
    contador = contador + 1
    _, frame = video.read()
    cv2.rectangle(frame, (0,0), (frame.shape[1], frame.shape[0]), (0, 255,0), 5)
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.imshow("Frame", frame)

    
    if cv2.waitKey(1) == ord('s'):
        copia = frame.copy()
        
        tiempo = datetime.now()
        nombre_archivo = "copia"+str(tiempo.hour)+str(tiempo.minute)+str(tiempo.second)+".jpg"
        print(nombre_archivo)
        cv2.imwrite(nombre_archivo, copia)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
video.release()

img = cv2.imread("frame.jpg")
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.imshow("frame", img)

cv2.waitKey()
cv2.destroyAllWindows()