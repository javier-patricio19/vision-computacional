import sys
from ventana import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage
import cv2
import time

class aplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
    
        self.ventana.setupUi(self)
        self.ventana.btnCargarImg.clicked.connect(self.cargar)
        self.ventana.btnGuardar.clicked.connect(self.guardar)
        self.ventana.btnSalir.clicked.connect(self.cerrar)
        
    def cargar(self):
        # print("cargar")
        self.nombre_archivo = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        # print(self.nombre_archivo)
        self.img = cv2.imread(self.nombre_archivo)
        frame = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img2 = QImage(
            frame, 
            frame.shape[1], 
            frame.shape[0], 
            frame.strides[0], 
            QImage.Format_RGB888)
        img2 = img2.scaled(500,400, Qt.KeepAspectRatio)
        imagen = self.ventana.lblImg.setPixmap(QtGui.QPixmap.fromImage(img2))
        
    def guardar(self):
        # print("guardar")
        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
        cv2.imwrite(f"img{tiempo}.jpg", self.img)
        print("Imagen guardada")
        
    def cerrar(self):
        self.close()
        
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = aplicationWindow()
    ventana.show()
    sys.exit(app.exec_())
