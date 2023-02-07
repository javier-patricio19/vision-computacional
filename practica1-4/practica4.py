import cv2

img = cv2.imread("img2.jpeg")
cv2.namedWindow("ventana", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty("ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("ventana", img)


cv2.waitKey()
cv2.destroyAllWindows()