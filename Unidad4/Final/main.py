
import sys
from ventana import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import cv2
import imutils
from datetime import datetime



class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    mostrar_captura = pyqtSignal(np.ndarray)
    flag_capturar_img = False

    def run(self):
        # capture from web cam
        path = QFileDialog.getOpenFileName()[0]
        cap = cv2.VideoCapture(path)
        while True:
            ret, frame = cap.read()
            if ret:
                if(self.flag_capturar_img):
                    tiempo = datetime.now()
                    self.nombre_captura = (
                        str(tiempo.hour) + "-" 
                        + str(tiempo.minute) + "-" 
                        + str(tiempo.second) + ".jpg"
                        )
                    cv2.imwrite(self.nombre_captura, frame)
                    self.mostrar_captura.emit(frame)
                    self.flag_capturar_img = False
                    
                self.change_pixmap_signal.emit(frame)
                
        
        
class aplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
    
        self.ventana.setupUi(self)
        
        self.ventana.menuBuscarVideo.triggered.connect(self.buscarVideo)
        self.ventana.menuGuardarCaptura.triggered.connect(self.guardarCaptura)
        self.ventana.menuSalir.triggered.connect(self.close)
        
        self.ventana.btnCapturar.clicked.connect(self.tomarCaptura)
        
        self.ventana.sliderH.valueChanged['int'].connect(self.sliderH)
        self.ventana.sliderS.valueChanged['int'].connect(self.sliderS)
        self.ventana.sliderV.valueChanged['int'].connect(self.sliderV)
    
    def buscarVideo(self):
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()
        
        
    def tomarCaptura(self):
        self.thread.flag_capturar_img = True
        self.thread.mostrar_captura.connect(self.mostrarCaptura)
    
    @pyqtSlot(np.ndarray)
    def convert_cv_qt(self, cv_img, escala):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(escala[0],escala[1], Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img, (471,300))
        self.ventana.lblVideo.setPixmap(qt_img)
    
    def mostrarCaptura(self, cv_img):
        self.hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
        qt_img = self.convert_cv_qt(cv_img, (281,200))
        self.ventana.lblCaptura.setPixmap(qt_img)
        
    
    def guardarCaptura(self):
        cv2.imwrite("HSV"+self.thread.nombre_captura, self.captura_modificada)
    
    def sliderH(self):
        valor = self.ventana.sliderH.value()
        self.ventana.lblValorH.setText(str(valor))
        
        self.modificarHSV(0, valor, 180)
    
    
    def sliderS(self):
        valor = self.ventana.sliderS.value()
        self.ventana.lblValorS.setText(str(valor))
        
        self.modificarHSV(1, valor, 255)
        
    def sliderV(self):
        valor = self.ventana.sliderV.value()
        self.ventana.lblValorV.setText(str(valor))
        
        self.modificarHSV(2, valor, 255)
        
    def modificarHSV(self, pos, valor, limite):
        img = self.hsv.copy()
        if (img[:,:,pos].all() < limite):
            img[:,:,pos]= (img[:,:,pos]+valor)%limite
                
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        self.captura_modificada = img.copy()
        img = self.convert_cv_qt(img, (281,200))
        self.ventana.lblCaptura.setPixmap(img)
        
    
        
    
    def unirHSV(self):
        pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = aplicationWindow()
    ventana.show()
    sys.exit(app.exec_())