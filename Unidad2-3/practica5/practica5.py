import cv2
import numpy as np

img = cv2.imread("img.png")

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,valor = cv2.threshold(gris, 50, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
contorno, _ = cv2.findContours(
    figura,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

lista_contornos = []

for index in range(len(contorno)):
    area = cv2.contourArea(contorno[index])
    if area > 500:
        objecto = contorno[index]
        lista_contornos.append(objecto)
        
cv2.drawContours(img, contorno[index], -1, (0,255,0), 5)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)

cv2.waitKey()
cv2.destroyAllWindows()