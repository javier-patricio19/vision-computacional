import cv2
import numpy as np

img = cv2.imread("img.jpg")
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,valor = cv2.threshold(gris, 228, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
contorno, jerarquia = cv2.findContours(
    figura,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

for index in range(len(contorno)):
    cv2.drawContours(img, contorno, index, (0, 230, 0), 5)
    cantidad = contorno[index]
    moments = cv2.moments(cantidad)
    pos_x = int(moments['m10']/moments['m00'])
    pos_y = int(moments['m01']/moments['m00'])
    img = cv2.circle(img, (pos_x, pos_y), radius=2, color=(0,230,0), thickness=20)

img = cv2.putText(img, ("Son: "+str(len(contorno))+ " objetos"),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),10,cv2.LINE_AA)
    
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("morfo", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)
cv2.imshow("morfo", figura)
cv2.waitKey()
cv2.destroyAllWindows()