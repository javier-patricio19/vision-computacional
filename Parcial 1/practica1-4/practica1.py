# -*- coding: utf-8 -*-

import cv2

img1 = cv2.imread("img1.jpg")
cv2.imshow("imagen", img1)
img2 = cv2.resize(img1, (500,500), interpolation=cv2.INTER_AREA)
cv2.imshow("imagen", img2)
cv2.imwrite("imagen.jpg", img2)
cv2.waitKey()
cv2.destroyAllWindows()