# escalado de imagenes

import cv2
import numpy as np

img0 = cv2.imread("practica9/img.jpg")
alto0, ancho0, canales0 = img0.shape
img = img0[0:ancho0, 0:ancho0]
alto, ancho, canales = img.shape
print(alto, ancho)

escala = 2

matriz = np.array([
    [escala,0,0],
    [0,escala,0],
    [0,0,1]
    ])

# img_nueva = np.zeros((alto*escala, ancho*escala, canales), np.uint8)

# ancho2, alto2, canales2 = img_nueva.shape
# for y in range(ancho):
#     for x in range(alto):
#         pixel = img[y,x]
#         pos_pixel = np.array([y,x,1])
#         res_pixel = np.dot(matriz, pos_pixel)
#         pos_x = res_pixel[0]
#         pos_y = res_pixel[1]
#         img_nueva[pos_x,pos_y] = pixel
        


img_nueva = cv2.resize(img,(33,33),interpolation=cv2.INTER_LINEAR)

cv2.namedWindow("nueva", cv2.WINDOW_NORMAL)
cv2.imshow("nueva", img_nueva)

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()