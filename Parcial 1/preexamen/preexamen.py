# elegir una imagen cuadrada y validar que no sea mayor a 500px dicha imagen se mostrara en escala de grises
# a continuacion dicha imagen se partira en cuatro partes representando un cuarto cada una de ellas
# posteriormente una de las cuatro imagenes se rotara a 45° y otra a 135°
#por ultimo una de las imagenes escalarla de 1/5

import cv2
import numpy as np
import imutils

#Leer la imagen y recabar el alto, ancho y sus canales
img0 = cv2.imread("practica9/img.jpg")
alto0, ancho0, canales0 = img0.shape

#Redimencionar la imagen a 400x400 pixeles
img =  cv2.resize(img0[0:ancho0, 0:ancho0], (400,400), interpolation=cv2.INTER_AREA)
alto, ancho, canales = img.shape

#Comprobar que la imagen no sea mayor a 500px y que sea cuadrada
if((alto > 500 or ancho > 500) or (alto - ancho != 0)):
    print("La imagen no es cuadrada o es demasiado grande!!!")
    cv2.destroyAllWindows()
else:
    #Convertir la imagen a escala de grises y mostrarla en una ventana
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img gris", img_gris)
    
    #Crear una lista con los recortes de la imagen original
    recortes = [
        img_gris[0:int(alto/2), 0:int(ancho/2)],
        img_gris[0:int(alto/2), int(ancho/2):int(ancho)],
        img_gris[int(alto/2):alto, 0:int(ancho/2)],
        img_gris[int(alto/2):alto, int(ancho/2):ancho]
    ]
    
    #Recorrer la lista de recortes y mostrarlos en ventanas
    for i, x in enumerate(range(len(recortes))):
        cv2.imshow("img"+str(x), recortes[i])
    
    #Crear y mostrar una imagen con rotacion de 45°
    img_rotada1 = imutils.rotate_bound(recortes[0], 45)
    cv2.imshow("45 grad", img_rotada1)
    
    #Crear y mostrar una imagen con rotacion de 135°
    img_rotada2 = imutils.rotate_bound(recortes[1], 135)
    cv2.imshow("135 grad", img_rotada2)
    
    #Redimencionar un recorte para que sea 5 veces mas grande y mostrarlo en una ventana
    dim_nuevas = (int(recortes[2].shape[0]*5),int(recortes[2].shape[1]*5))
    img_grande = cv2.resize(recortes[2],(dim_nuevas),interpolation=cv2.INTER_LINEAR)
    cv2.imshow("grande", img_grande)



cv2.waitKey()
cv2.destroyAllWindows()