import cv2
import numpy as np
import imutils

video = cv2.VideoCapture(0)

while True:
    a, frame = video.read()
    
    if a == False:
        break
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    rojo_claro = np.array([0,170,20], np.uint8)
    rojo_obscuro = np.array([10,255,255], np.uint8)

    rojo_claro2 = np.array([175,170,20], np.uint8)
    rojo_obscuro2 = np.array([179,255,255], np.uint8)

    mascara1 = cv2.inRange(hsv, rojo_claro, rojo_obscuro)
    mascara2 = cv2.inRange(hsv, rojo_claro2, rojo_obscuro2)

    mascara = cv2.add(mascara1, mascara2)

    rojo = cv2.bitwise_and(frame, frame, mask=mascara)
    rojo[mascara>0] = (255,0,0)
    no_rojo = cv2.bitwise_not(mascara)
    color_gris = cv2.bitwise_and(gris, gris, mask=no_rojo)
    img_final = cv2.add(color_gris, rojo)

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow("img", frame)


    cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
    cv2.imshow("img2", img_final)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()