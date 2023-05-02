import cv2

img = cv2.resize(cv2.imread("practica1-4/img2.jpeg"), (200,200), interpolation=cv2.INTER_AREA)
cv2.imshow("img", img)
R,G,B = cv2.split(img)
# cv2.namedWindow("Rojo", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Verde", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Azul", cv2.WINDOW_NORMAL)
# cv2.imshow("Rojo", R)
# cv2.imshow("Verde", G)
# cv2.imshow("Azul", B)

while True:
    key = cv2.waitKey()
    if key == ord("r"):
        cv2.imshow("ventana", B)
    elif key == ord("g"):
        cv2.imshow("ventana", G)
    elif key == ord("b"):
        cv2.imshow("ventana", B)
    else:
        break

# cv2.waitKey()
cv2.destroyAllWindows()