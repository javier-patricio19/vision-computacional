from PyQt5.QtWidgets import QApplication, QWidget
import sys

class VentanaVacia(QWidget):
    def _init_(self):
        super(VentanaVacia,self)._init_()
        self.initializeUi()
        
    def initializeUi(self):
        self.setGeometry(100,100,400,600)
        self.setWindowTitle("Ventana")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaVacia()
    window.show()
    sys.exit(app.exec_())