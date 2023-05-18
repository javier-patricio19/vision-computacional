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
        
        self.ventana.menuGuardarGrises.setEnabled(False)
        self.ventana.menuGuardarRGB.setEnabled(False)
        self.ventana.menuGuardarHSV.setEnabled(False)
        
        self.ventana.menuAbrirImg.triggered.connect(self.abrir)
        self.ventana.menuSalir.triggered.connect(self.salir)
        self.ventana.menuGuardarGrises.triggered.connect(self.guardarGris)
        self.ventana.menuGuardarHSV.triggered.connect(self.guardarHSV)
        self.ventana.menuGuardarRGB.triggered.connect(self.guardarRGB)
        
        self.ventana.btnGrises.clicked.connect(self.crearGrises)
        self.ventana.btnRGB.clicked.connect(self.crearRGB)
        self.ventana.btnHSV.clicked.connect(self.crearHSV)
        
        
        
    def abrir(self):
        self.nombre_archivo = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        # print(self.nombre_archivo)
        self.img = cv2.imread(self.nombre_archivo)
        frame = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img = QImage(
            frame, 
            frame.shape[1], 
            frame.shape[0], 
            frame.strides[0], 
            QImage.Format_RGB888)
        img = img.scaled(200,250, Qt.KeepAspectRatio)
        self.ventana.lblImg1.setPixmap(QtGui.QPixmap.fromImage(img))
        
        self.ventana.menuEdicion.setEnabled(True)
        self.ventana.btnGrises.setEnabled(True)
        self.ventana.btnRGB.setEnabled(True)
        self.ventana.btnHSV.setEnabled(True)
        
        self.ventana.sliderR.valueChanged['int'].connect(self.rgbR)
        self.ventana.sliderR.setMaximum(255)
        self.ventana.sliderG.valueChanged['int'].connect(self.rgbG)
        self.ventana.sliderB.valueChanged['int'].connect(self.rgbB)
        
        self.ventana.sliderH.valueChanged['int'].connect(self.canalH)
        self.ventana.sliderS.valueChanged['int'].connect(self.canalS)
        self.ventana.sliderV.valueChanged['int'].connect(self.canalV)
    
    def canalH(self, valor):
        va = 180 - valor
        self.h[self.h > va] = 180
        self.h[self.h <= va] += valor
        self.modHSV()
        
        
    def canalS(self, valor):
        va = 180 - valor
        self.s[self.s > va] = 180
        self.s[self.s <= va] += valor
        self.modHSV()
    
    def canalV(self, valor):
        va = 180 - valor
        self.v[self.v > va] = 180
        self.v[self.v <= va] += valor
        self.modHSV()
    
    def modHSV(self):
        img2 = cv2.merge((self.h,self.s,self.v))
        self.h,self.s,self.v = cv2.split(self.img)
        self.framehsv = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img = QImage(
            self.framehsv, 
            self.framehsv.shape[1], 
            self.framehsv.shape[0], 
            self.framehsv.strides[0], 
            QImage.Format_RGB888)
        img = img.scaled(200,250, Qt.KeepAspectRatio)
        self.ventana.lblImg4.setPixmap(QtGui.QPixmap.fromImage(img))
        
    def guardarHSV(self):
        archivo = QFileDialog.getSaveFileName(filter = "JPG(*.jpg);;PNG(*.png)")[0]
        cv2.imwrite(archivo, self.framehsv) 
        
    def guardarRGB(self):
        archivo = QFileDialog.getSaveFileName(filter = "JPG(*.jpg);;PNG(*.png)")[0]
        cv2.imwrite(archivo, self.framergb) 
        
    def rgbR(self, valor):
        limite = 255
        self.r[self.g > limite] += 255
        self.r[self.r <= limite] += valor
        self.modRgb()
    
    def rgbG(self, valor):
        limite = 255
        self.g[self.g > limite] += 255
        self.g[self.r <= limite] += valor
        self.modRgb()
    
    def rgbB(self, valor):
        limite = 255
        self.b[self.g > limite] += 255
        self.b[self.r <= limite] += valor
        self.modRgb()
        
    def modRgb(self):
        rgb_final = cv2.merge((self.r,self.g,self.b))
        self.framergb = cv2.cvtColor(rgb_final, cv2.COLOR_BGR2RGB)
        img = QImage(
            self.framergb, 
            self.framergb.shape[1], 
            self.framergb.shape[0], 
            self.framergb.strides[0], 
            QImage.Format_RGB888)
        img = img.scaled(200,250, Qt.KeepAspectRatio)
        self.ventana.lblImg3.setPixmap(QtGui.QPixmap.fromImage(img))
        
    def crearGrises(self):
        # img = cv2.imread(self.nombre_archivo)
        self.img_gris = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        img = QImage(
            self.img_gris, 
            self.img_gris.shape[1], 
            self.img_gris.shape[0], 
            self.img_gris.strides[0], 
            QImage.Format_Grayscale8)
        img = img.scaled(200,250, Qt.KeepAspectRatio)
        self.ventana.lblImg2.setPixmap(QtGui.QPixmap.fromImage(img))
        
        self.ventana.menuGuardarGrises.setEnabled(True)
        
    def crearRGB(self):
        frame = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img = QImage(
            frame, 
            frame.shape[1], 
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888)
        img = img.scaled(200,250, Qt.KeepAspectRatio)
        self.ventana.lblImg3.setPixmap(QtGui.QPixmap.fromImage(img))
        
        self.ventana.sliderR.setEnabled(True)
        self.ventana.sliderG.setEnabled(True)
        self.ventana.sliderB.setEnabled(True)
        
        self.ventana.menuGuardarRGB.setEnabled(True)
        
        self.r,self.g,self.b = cv2.split(self.img)
    
    def crearHSV(self):
        self.h,self.s,self.v = cv2.split(self.img)
        frame = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        img = QImage(
            frame, 
            frame.shape[1], 
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888)
        img = img.scaled(200,250, Qt.KeepAspectRatio)
        self.ventana.lblImg4.setPixmap(QtGui.QPixmap.fromImage(img))
        
        self.ventana.sliderH.setEnabled(True)
        self.ventana.sliderS.setEnabled(True)
        self.ventana.sliderV.setEnabled(True)
        
        self.ventana.menuGuardarHSV.setEnabled(True)
        
    def guardarGris(self):
        archivo = QFileDialog.getSaveFileName(filter = "JPG(*.jpg);;PNG(*.png)")[0]
        cv2.imwrite(archivo, self.img_gris) 
        
    def salir(self):
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = aplicationWindow()
    ventana.show()
    sys.exit(app.exec_())