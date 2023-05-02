
#Grabar video con camara
import cv2

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
