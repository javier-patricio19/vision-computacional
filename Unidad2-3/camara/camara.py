#Activar la camara

import cv2
captura = cv2.VideoCapture(0)
while (captura.isOpened()):
  ret, imagen = captura.read() #ret, es un bool que nos indica si esta leyedo el video
  if ret == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()

#Grabar video con camara
#el valor 20.0 son los fotogramas del video x segundo (640,480) la resolución
captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter('videoSalida.avi',
                         cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    salida.write(imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
salida.release()
cv2.destroyAllWindows()

#visualizar video 
captura = cv2.VideoCapture('videoSalida.avi')
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(30) == ord('s'):  #el valor 30 en esta instrucción refleja los frames que se mostraran por segundo
      break
  else: break #termina el video cuando se acaba
captura.release()
cv2.destroyAllWindows()