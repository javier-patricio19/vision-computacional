# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        Calculadora.setObjectName("Calculadora")
        Calculadora.resize(428, 383)
        Calculadora.setMinimumSize(QtCore.QSize(428, 383))
        Calculadora.setMaximumSize(QtCore.QSize(428, 383))
        self.centralwidget = QtWidgets.QWidget(Calculadora)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_2.setObjectName("label_2")
        self.txtNum1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNum1.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.txtNum1.setObjectName("txtNum1")
        self.txtNum2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNum2.setGeometry(QtCore.QRect(130, 100, 113, 20))
        self.txtNum2.setObjectName("txtNum2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(270, 100, 82, 25))
        self.btnCalcular.setObjectName("btnCalcular")
        self.dropOperacion = QtWidgets.QComboBox(self.centralwidget)
        self.dropOperacion.setGeometry(QtCore.QRect(270, 60, 81, 21))
        self.dropOperacion.setObjectName("dropOperacion")
        self.dropOperacion.addItem("")
        self.dropOperacion.addItem("")
        self.dropOperacion.addItem("")
        self.dropOperacion.addItem("")
        self.lblResultado = QtWidgets.QLabel(self.centralwidget)
        self.lblResultado.setGeometry(QtCore.QRect(150, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblResultado.setFont(font)
        self.lblResultado.setObjectName("lblResultado")
        self.lblMsg = QtWidgets.QLabel(self.centralwidget)
        self.lblMsg.setGeometry(QtCore.QRect(60, 230, 291, 41))
        self.lblMsg.setText("")
        self.lblMsg.setObjectName("lblMsg")
        Calculadora.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculadora)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 23))
        self.menubar.setObjectName("menubar")
        Calculadora.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculadora)
        self.statusbar.setObjectName("statusbar")
        Calculadora.setStatusBar(self.statusbar)

        self.retranslateUi(Calculadora)
        QtCore.QMetaObject.connectSlotsByName(Calculadora)

    def retranslateUi(self, Calculadora):
        _translate = QtCore.QCoreApplication.translate
        Calculadora.setWindowTitle(_translate("Calculadora", "Calculadora"))
        self.label.setText(_translate("Calculadora", "Número 1"))
        self.label_2.setText(_translate("Calculadora", "Número 2"))
        self.label_3.setText(_translate("Calculadora", "Resultado: "))
        self.btnCalcular.setText(_translate("Calculadora", "Calcular"))
        self.dropOperacion.setCurrentText(_translate("Calculadora", "Suma"))
        self.dropOperacion.setItemText(0, _translate("Calculadora", "Suma"))
        self.dropOperacion.setItemText(1, _translate("Calculadora", "Resta"))
        self.dropOperacion.setItemText(2, _translate("Calculadora", "Multiplicación"))
        self.dropOperacion.setItemText(3, _translate("Calculadora", "División"))
        self.lblResultado.setText(_translate("Calculadora", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculadora = QtWidgets.QMainWindow()
    ui = Ui_Calculadora()
    ui.setupUi(Calculadora)
    Calculadora.show()
    sys.exit(app.exec_())
