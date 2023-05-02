# Del video para el examen capturar una imagen dentro del tiempo de 0 al 4 segundo.

# Una ves realizado esto, debes de contabilizar los objetos aplicando la técnica que mas te parezca.
# Crear dos imágenes de la imagen anterior por mitad y guardarlas con tu nombre y un numero que diferencie la imagen, junto con la extensión .jpg
# por ejemplo: osvaldo1.jpg y osvaldo2.jpg
# calcular el área de las figuras de la imagen 1 y el perímetro de las figuras de la imagen 2.
# Texto de la respuesta

import cv2
import numpy as np

video = cv2.VideoCapture("ExamenOpenCV.mp4")

captura_realizada = False
while video.isOpened():
    a, frame = video.read()
    
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.imshow("Frame", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('s') and not captura_realizada:
        captura_realizada = True
        img = frame.copy()
        cv2.imwrite("captura.jpg", img)
        
        copia1 = frame.copy()
        cv2.rectangle(copia1, (0,0), (copia1.shape[1], copia1.shape[0]), (0, 255,0), 5)
        cv2.imshow("Frame", copia1)
        cv2.waitKey(500)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()

img = cv2.imread("captura.jpg")

alto, ancho, canales = img.shape
mitades = []
mitades.append(img[0:alto, 0:int(ancho/2)])
mitades.append(img[0:alto, int(ancho/2):int(ancho)])

cv2.imwrite("francisco1.jpg", mitades[0])
cv2.imwrite("francisco2.jpg", mitades[1])


for index_mitad, mitad in enumerate(mitades):
    copia = cv2.GaussianBlur(mitad, (11,11), 8, (0,0))
    gris = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)

    _,valor = cv2.threshold(gris, 10, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3,3), np.uint8)
    # figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
    contorno, jerarquia = cv2.findContours(
        valor,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

    cantidad_obj = 0

    for index in range(len(contorno)):
        area = int(cv2.contourArea(contorno[index]))
        perimetro = int(cv2.arcLength(contorno[index], True))
        
        print(area)
        if area > 10000:
            cantidad_obj = cantidad_obj + 1
            cv2.drawContours(mitad, contorno, index, (0, 230, 0), 5)
            cantidad = contorno[index]
            
            moments = cv2.moments(cantidad)
            pos_x = int(moments['m10']/moments['m00'])
            pos_y = int(moments['m01']/moments['m00'])
            
            if(index_mitad == 0):
                mitad = cv2.putText(mitad, ("Area: "+str(area)),(pos_x-200, pos_y+100), cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),4,cv2.LINE_AA)
                cv2.imwrite("areas.jpg", mitad)

            if(index_mitad == 1):
                mitad = cv2.putText(mitad, ("Per: "+str(perimetro)),(pos_x-20, pos_y+120), cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),4,cv2.LINE_AA)
                cv2.imwrite("perimetros.jpg", mitad)
        
        cv2.namedWindow(("mitad"+str(index_mitad)) , cv2.WINDOW_NORMAL)
        cv2.imshow(("mitad"+str(index_mitad)), mitad)

    mitad = cv2.putText(mitad, ("Son: "+str(cantidad_obj)+ " objetos"),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),10,cv2.LINE_AA)
    
    cv2.namedWindow(("mitad"+str(index_mitad)), cv2.WINDOW_NORMAL)
    cv2.imshow(("mitad"+str(index_mitad)), mitad)

cv2.waitKey(0)
cv2.destroyAllWindows()