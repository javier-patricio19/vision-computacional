#visualizar video 
import cv2
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