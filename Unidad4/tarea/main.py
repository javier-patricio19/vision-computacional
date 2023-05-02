import sys
from calculadora import Ui_Calculadora
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class aplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculadora = Ui_Calculadora()
        self.calculadora.setupUi(self)
        
        self.calculadora.btnCalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        op = self.calculadora.dropOperacion.currentIndex()
        
        try:
            num1 = float(self.calculadora.txtNum1.text())
            num2 = float(self.calculadora.txtNum2.text())
        except:
            self.calculadora.lblMsg.setText("*Ingresa solo numeros")
        else:
            self.calculadora.lblMsg.setText("")
            match op:
                case 0: #Suma
                    resultado = num1 + num2
                case 1: #Resta
                    resultado = num1 - num2
                case 2: #Mult
                    resultado = num1 * num2
                case 3: #Div
                    resultado = num1 / num2
            self.calculadora.lblResultado.setText(str(round(resultado, 2)))
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = aplicationWindow()
    calculadora.show()
    sys.exit(app.exec_())
