import cv2
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,800)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

while(True):
    v,frame = video.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    alto, ancho, canales = frame.shape
    cx = int(ancho / 2)
    cy = int(alto / 2)
    centro = hsv_frame[cy,cx]
    canal_H= centro[0]
    print(canal_H)
    color = ""
    if canal_H < 5:
        color = "Rojo"
    elif canal_H <22:
        color = "Naranja"
    elif canal_H < 33:
        color = "Amarillo"
    elif canal_H < 78:
        color = "Verde"
    elif canal_H < 131:
        color = "Azul"
    elif canal_H < 167:
        color = "Violeta"
    else:
        color = "Rojo"
    b,g,r = int(centro[0]), int(centro[1]), int(centro[2]) 
    cv2.putText(frame,color+" : "+str(canal_H),(10,50),0, 1, (b,g,r),2)
    cv2.circle(frame,(cx,cy),5,(255,0,0),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
video.release()
cv2.waitKey()
cv2.destroyAllWindows()