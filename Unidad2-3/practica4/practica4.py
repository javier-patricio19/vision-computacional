import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def resize_image(e):
   global image, resized, image2
   image = im
   resized = image.resize((e.width, e.height))
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

win = tk.Tk()
win.geometry("700x500")
img = cv2.imread("img.jpg")

canvas = tk.Canvas(win, width=700, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,valor = cv2.threshold(gris, 50, 255, cv2.THRESH_BINARY)


kernel = np.ones((3,3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
contorno, jerarquia = cv2.findContours(
    figura,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

for index in range(len(contorno)):
    cv2.drawContours(img, contorno, index, (0, 230, 0), 5)
    cantidad = contorno[index]
    moments = cv2.moments(cantidad)
    pos_x = int(moments['m10']/moments['m00'])
    pos_y = int(moments['m01']/moments['m00'])
    img = cv2.circle(img, (pos_x, pos_y), radius=2, color=(0,230,0), thickness=20)
    
    area = cv2.contourArea(contorno[index])
    print("Area: ", area)
    
    img = cv2.putText(img, str(area),(pos_x, pos_y+100), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),9,cv2.LINE_AA)

img = cv2.putText(img, ("Son: "+str(len(contorno))+ " objetos"),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),10,cv2.LINE_AA)


im = Image.fromarray(img)
im = im.resize((400,400))
imgtk = ImageTk.PhotoImage(image=im)

canvas.create_image(0, 0, image=imgtk, anchor='nw')

win.bind("<Configure>", resize_image)
win.mainloop()

# # cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# # cv2.namedWindow("morfo", cv2.WINDOW_NORMAL)
# # cv2.imshow("img", img)
# # cv2.imshow("morfo", figura)
# # cv2.waitKey()
# # cv2.destroyAllWindows()