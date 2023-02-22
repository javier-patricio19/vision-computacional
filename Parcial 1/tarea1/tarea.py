import cv2
import numpy as np

#Crear una arreglo con los nombres de los archivos
imgs_names = ("img1.png", "img2.png", "img3.png", "img4.png", "img5.png")

#Crear una lista para almacenar las imagenes cargadas
imgs = []

#Leer las imagenes y guardarlas en la lista creada anteriormete
for i in range(len(imgs_names)):
    imgs.append(cv2.imread(imgs_names[i]))

#Recorrer la lista de imagenes y los pixeles de cada una, si los pixeles estan vacion, pintarlos de un color
#y mostrar las imagenes modificadas
for index, img in enumerate(imgs):
    for x in range (img.shape[0]):
        for y in range (img.shape[1]):
            # print(image[x][y])
            pixel = img[x][y]
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                img[x][y] = [224, 51, 255]
    cv2.imshow("win"+str(index), img)

cv2.waitKey()
cv2.destroyAllWindows()