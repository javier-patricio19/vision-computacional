import sys
from ventana import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage
import cv2
import time


app = QtWidgets.QApplication([])

ventana = uic.loadUi("ventana.ui")

def cargar():
    global img
    # print("cargar")
    nombre_archivo = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
    # print(nombre_archivo)
    img = cv2.imread(nombre_archivo)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img2 = QImage(
        frame, 
        frame.shape[1], 
        frame.shape[0], 
        frame.strides[0], 
        QImage.Format_RGB888)
    img2 = img2.scaled(500,400, Qt.KeepAspectRatio)
    imagen = ventana.lblImg.setPixmap(QtGui.QPixmap.fromImage(img2))
    
def guardar():
    global img
    # print("guardar")
    tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
    cv2.imwrite(f"img{tiempo}.jpg", img)
    print("Imagen guardada")
    
def cerrar():
    ventana.close()
    
ventana.btnCargarImg.clicked.connect(cargar)
ventana.btnGuardar.clicked.connect(guardar)
ventana.btnSalir.clicked.connect(cerrar)

ventana.show()
app.exec()