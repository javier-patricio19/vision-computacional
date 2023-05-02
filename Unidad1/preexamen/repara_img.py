import cv2
import numpy as np

img = cv2.imread("practica9/img.jpg")
alto, ancho, canales = img.shape

if(alto > ancho):
    img2 = cv2.resize(img, (,500), interpolation=cv2.INTER_AREA)