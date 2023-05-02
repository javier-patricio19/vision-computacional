import cv2
import numpy as np
import imutils

img = cv2.imread("img.jpg")

img = imutils.resize(img, width=640)


gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gris = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rojo_claro = np.array([0,100,20], np.uint8)
rojo_obscuro = np.array([5,255,255], np.uint8)

rojo_claro2 = np.array([175,100,20], np.uint8)
rojo_obscuro2 = np.array([179,255,255], np.uint8)

mascara1 = cv2.inRange(hsv, rojo_claro, rojo_obscuro)
mascara2 = cv2.inRange(hsv, rojo_claro2, rojo_obscuro2)

mascara = cv2.add(mascara1, mascara2)

rojo = cv2.bitwise_and(img, img, mask=mascara)
no_rojo = cv2.bitwise_not(mascara)
color_gris = cv2.bitwise_and(gris, gris, mask=no_rojo)
img_final = cv2.add(color_gris, rojo)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)


cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
cv2.imshow("img2", img_final)


cv2.waitKey(0)
cv2.destroyAllWindows()