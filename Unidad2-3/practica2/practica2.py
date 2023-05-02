import cv2
import numpy as np

img = cv2.imread("monedas.jpg")
img2 = img.copy()
gris = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_,valor = cv2.threshold(gris, 228, 300, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
# bordes = cv2.Canny(gris, 220, 300, apertureSize=3)
contorno, jerarquia = cv2.findContours(
    figura,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contorno, -1, (0,50,150), 12)
print("Hay ", len(contorno), " monedas")

img = cv2.putText(img2, ("Son: "+str(len(contorno))+ " monedas"),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),10,cv2.LINE_AA)

cv2.namedWindow("monedas", cv2.WINDOW_NORMAL)
cv2.namedWindow("morfo", cv2.WINDOW_NORMAL)
cv2.imshow("monedas", img)
cv2.imshow("morfo", figura)

cv2.waitKey()
cv2.destroyAllWindows()