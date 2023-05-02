import sys
from login import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class aplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Ui_MainWindow()
        self.login.setupUi(self)
        
        self.login.btnAceptar.clicked.connect(self.validar)
        self.login.btnCancelar.clicked.connect(self.cerrar)
        
    def validar(self):
        print("ola")
        usuario = self.login.txtUsuario.text()
        password = self.login.txtPassword.text()
        
        if usuario == 'admin' and password == '123':
            self.login.lblMsj.setText("Correcto")
        else:
            self.login.lblMsj.setText("Incorrecto")
        
    def cerrar(self):
        print("cerrar")
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = aplicationWindow()
    login.show()
    sys.exit(app.exec_())
