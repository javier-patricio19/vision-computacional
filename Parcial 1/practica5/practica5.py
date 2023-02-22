import cv2
import numpy as np

# img = cv2.imread("img.jpg")
image = np.zeros((100,100,3), np.uint8)

height, width, channels = image.shape
# height, width, channels = img.shape

print(height, width, channels)

for x in range (width):
    for y in range (height):
        # print(image[x][y])
        pixel = image[x][y]
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            image[x][y] = [224, 51, 255]
            
            

cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.imshow("win", image)
# cv2.imshow("win", img)
cv2.waitKey()
cv2.destroyAllWindows()