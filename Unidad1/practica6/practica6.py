# Practica 6 - 03/02/23

import cv2
import numpy as np

# img1 = cv2.imread("img1.png")
img1 = cv2.imread("img2.jpg")
h, w, ch = img1.shape

if h - w < 2 or w - h < 2:
    print("Es cuadrada")
    img_copia = img1.copy
    roi1 = cv2.selectROI("roi", img1)
    cv2.namedWindow("roi1", cv2.WINDOW_NORMAL)
    # print(roi1)
    img_nueva = img1[
        int(roi1[1]):int(roi1[1]+roi1[3]), 
        int(roi1[0]):int(roi1[0]+roi1[2])
        ]
    h_roi, w_roi, ch_roi = img_nueva.shape
    print("imagen nueva", h_roi, w_roi)
    
    cv2.imshow("roi1", img_nueva)
else:
    print("No es cuadrada")
    parte1 = img1[0:h, 0:int(w/2)]
    cv2.namedWindow("parte1", cv2.WINDOW_NORMAL)
    cv2.imshow("parte1", parte1)
    h_part1, w_part1, ch_part1 = parte1.shape
    
    parte2 = img1[0:h, int(w/2):]
    
    cv2.namedWindow("parte2", cv2.WINDOW_NORMAL)
    cv2.imshow("parte2", parte2)

# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.imshow("original", img1)

cv2.waitKey()
cv2.destroyAllWindows()