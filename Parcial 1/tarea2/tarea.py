
import cv2
import numpy as np

  
# leer la imagen
img = cv2.imread("img.jpg")

# obtener dimenciones
alto, ancho, canales = img.shape

# generar la imagen partida a la mitad
img_mitad = img[
    0:int(ancho/2), 
    0:int(alto)]
cv2.namedWindow("mitad", cv2.WINDOW_NORMAL)
cv2.imshow("mitad", img_mitad)
cv2.imwrite("mitad.jpg", img_mitad)

# abrir una ventana para seleccionar multiples rois
rois = cv2.selectROIs("Original", img)

# extraer las cordenadas de los rois seleccionados
for index, roi in enumerate(rois):
    x1 = roi[0]
    y1 = roi[1]
    x2 = roi[2]
    y2 = roi[3]
    
# generar las imagenes de los recortes
    img_corte = img[y1:y1+y2,x1:x1+x2]
    cv2.namedWindow("img"+str(index), cv2.WINDOW_NORMAL)
    cv2.imshow("img"+str(index), img_corte)
    cv2.imwrite("img"+str(index)+".jpg", img_corte)

cv2.waitKey()
cv2.destroyAllWindows()
