# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblUsr = QtWidgets.QLabel(self.centralwidget)
        self.lblUsr.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.lblUsr.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.lblUsr.setObjectName("lblUsr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(96, 80, 61, 20))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.lblMsj = QtWidgets.QLabel(self.centralwidget)
        self.lblMsj.setGeometry(QtCore.QRect(110, 130, 47, 16))
        self.lblMsj.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.lblMsj.setText("")
        self.lblMsj.setObjectName("lblMsj")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(170, 30, 113, 20))
        self.txtUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(170, 70, 113, 20))
        self.txtPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPassword.setObjectName("txtPassword")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(90, 190, 75, 23))
        self.btnAceptar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(190, 190, 75, 23))
        self.btnCancelar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 90, 111, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("rr.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblUsr.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Contraseña"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
