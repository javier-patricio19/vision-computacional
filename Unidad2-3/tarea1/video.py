import cv2
import os
video = cv2.VideoCapture("video.mp4")

capturas = []
while video.isOpened():
    _, frame = video.read()
    
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.imshow("Frame", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('s') and len(capturas) < 2:
        copia = frame.copy()
        capturas.append(copia)
        nombre_archivo = "copia"+str(len(capturas))+".jpg"
        print(nombre_archivo)
        cv2.imwrite(nombre_archivo, copia)
        copia1 = frame.copy()
        cv2.rectangle(copia1, (0,0), (copia1.shape[1], copia1.shape[0]), (0, 255,0), 5)
        cv2.imshow("Frame", copia1)
        cv2.waitKey(500)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()

if len(capturas) > 0:
    if not os.path.exists("rgb"):
        os.makedirs("rgb")
        
    b,g,r = cv2.split(capturas[0])
    cv2.imwrite("rgb/azul.jpg", b)
    cv2.imwrite("rgb/verde.jpg", g)
    cv2.imwrite("rgb/rojo.jpg", r)

if len(capturas) > 1:
    if not os.path.exists("hsv"):
        os.makedirs("hsv")
    hsv = cv2.cvtColor(capturas[1], cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    cv2.imwrite("hsv/matiz.jpg", h)
    cv2.imwrite("hsv/saturacion.jpg", s)
    cv2.imwrite("hsv/brillo.jpg", v)

cv2.waitKey(1)
cv2.destroyAllWindows()