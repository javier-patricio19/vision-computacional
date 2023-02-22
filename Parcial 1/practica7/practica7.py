
import cv2
import numpy as np

img = cv2.imread("imagen.jpg")

alto, largo, canales = img.shape

if alto==largo:
    print("Es cuadrada")
    
    imgcopiada = img.copy()
    roi1 = cv2.selectROI("ROI",img)
    cv2.namedWindow("ROI",cv2.WINDOW_NORMAL)
    print(roi1)
    imagenueva = img[int(roi1[1]) : int(roi1[1]+roi1[3]), int(roi1[0]) : int(roi1[0]+roi1[2])]
    altoROI, largoROI, canalesROI = imagenueva.shape

    #segunda imagen
    roi2 = cv2.selectROI("ROI", img)
    #cv2.namedWindow("ROI2", cv2.WINDOW_NORMAL)
    print(roi2)
    imagenueva2 = img[int(roi2[1]) : int(roi2[1]+roi2[3]), int(roi2[0]) : int(roi2[0]+roi2[2])]
    altoROI2, largoROI2, canalesROI2 = imagenueva2.shape
    
    nueva1 = cv2.resize(imagenueva,(largoROI2,altoROI2))
    nueva2 = cv2.resize(imagenueva2,(largoROI,altoROI))
    
    imgcopiada[int(roi1[1]) : int(roi1[1]+ roi1[3]), int(roi1[0]) : int(roi1[0]+ roi1[2])] = nueva2
    imgcopiada[int(roi2[1]) : int(roi2[1]+ roi2[3]), int(roi2[0]) : int(roi2[0]+ roi2[2])] = nueva1
    
    cv2.namedWindow("imgCompuesta", cv2.WINDOW_NORMAL)
    cv2.imshow("imgCompuesta", imgcopiada)
    print("Imagnen nueva ",altoROI, largoROI)   
    cv2.namedWindow("NUEVA",cv2.WINDOW_NORMAL)
    cv2.imshow("NUEVA",imagenueva)
    print("imagenueva2",altoROI2, largoROI2)
    cv2.namedWindow("ROI3", cv2.WINDOW_NORMAL)
    cv2.imshow("ROI3",imagenueva)
    
    
    
    
else:
    print("No es cuadrada")
    parte1 = img[0 : alto, 0 : int(largo/2)]
    cv2.namedWindow("parte1",cv2.WINDOW_NORMAL)
    cv2.imshow("parte1",parte1)
    alto1, largo1, canales1 = parte1.shape
    print(alto1,largo1)
    parte2 = img[0 : alto, int(largo/2):]
    cv2.namedWindow("parte2",cv2.WINDOW_NORMAL)
    cv2.imshow("parte2",parte2)
    alto2, largo2, canales2 = parte2.shape
    print(alto2,largo2)
    imagenCompuesta = np.concatenate((parte2,parte1),axis=1)
    cv2.namedWindow("imagenCompuesta", cv2.WINDOW_NORMAL)
    cv2.imshow("imagenCompuesta", imagenCompuesta)

cv2.namedWindow("original",cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()