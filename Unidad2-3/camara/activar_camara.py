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
