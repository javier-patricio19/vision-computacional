import cv2

img = cv2.resize(cv2.imread("practica1-4/img2.jpeg"), (200,200), interpolation=cv2.INTER_AREA)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("img", img2)
H,S,V = cv2.split(img)
# cv2.namedWindow("H", cv2.WINDOW_NORMAL)
# cv2.namedWindow("S", cv2.WINDOW_NORMAL)
# cv2.namedWindow("V", cv2.WINDOW_NORMAL)
# cv2.imshow("H", H)
# cv2.imshow("S", S)
# cv2.imshow("V", V)

while True:
    key = cv2.waitKey()
    if key == ord("h"):
        cv2.imshow("ventana", H)
    elif key == ord("s"):
        cv2.imshow("ventana", S)
    elif key == ord("v"):
        cv2.imshow("ventana", V)


cv2.waitKey()
cv2.destroyAllWindows()