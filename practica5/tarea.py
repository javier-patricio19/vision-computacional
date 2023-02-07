import cv2
import numpy as np

imgs_names = ("img1.png", "img2.png", "img3.png", "img4.png", "img5.png")
imgs = []

for i in range(len(imgs_names)):
    imgs.append(cv2.imread(imgs_names[i]))



# print(height, width, channels)

for img in imgs:
    for x in range (img.shape[0]):
        for y in range (img.shape[1]):
            # print(image[x][y])
            pixel = img[x][y]
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                img[x][y] = [224, 51, 255]
    cv2.namedWindow("win"+str(), cv2.WINDOW_NORMAL)
    cv2.imshow("win", img)
            
            



# cv2.imshow("win", img)
cv2.waitKey()
cv2.destroyAllWindows()