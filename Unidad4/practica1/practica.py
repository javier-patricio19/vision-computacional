'''Rojo Claro: 0,100,20
Rojo Oscuro: 5,255,255
Rojo Claro2: 175,100,20
Rojo Oscuro2: 179,255,255'''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

bg = None
rojoBajo1 = np.array([0,100,20], np.uint8)
rojoAlto1 = np.array([5,255,255], np.uint8)
rojoBajo2 = np.array([ 175,100,20], np.uint8)
rojoAlto2 = np.array([179,255,255], np.uint8)

while True:
    ret, frame = cap.read()
  
    if ret == False: break

    if bg is None:
        bg = frame

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
    mask = cv2.add(maskRojo1,maskRojo2)
    mask = cv2.medianBlur(mask, 13)

    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2) #Dilatamos los pixeles o expandimos
    areaColor = cv2.bitwise_and(bg, bg, mask=mask)
    maskInv = cv2.bitwise_not(mask)
    sinAreaColor = cv2.bitwise_and(frame,frame,mask=maskInv)
    finalFrame = cv2.addWeighted(areaColor,1,sinAreaColor,1,0) #aplicamos la transparencia

    #cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
    #cv2.imshow('Frame',frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('areaColor', areaColor)
    #cv2.imshow('maskInv',maskInv)
    #cv2.imshow('sinAreaColor',sinAreaColor)
    cv2.namedWindow("finalFrame",cv2.WINDOW_NORMAL)
    cv2.imshow('finalFrame',finalFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()