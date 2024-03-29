# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(600, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(202, 255, 196);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnCargarImg = QtWidgets.QPushButton(self.frame)
        self.btnCargarImg.setGeometry(QtCore.QRect(20, 20, 91, 23))
        self.btnCargarImg.setStyleSheet("background-color: white;\n"
"border-radius: 3px;\n"
"border: 1px solid black;")
        self.btnCargarImg.setObjectName("btnCargarImg")
        self.btnSalir = QtWidgets.QPushButton(self.frame)
        self.btnSalir.setGeometry(QtCore.QRect(20, 100, 91, 23))
        self.btnSalir.setStyleSheet("background-color: white;\n"
"border-radius: 3px;\n"
"border: 1px solid black;")
        self.btnSalir.setObjectName("btnSalir")
        self.lblImg = QtWidgets.QLabel(self.frame)
        self.lblImg.setGeometry(QtCore.QRect(130, 20, 441, 381))
        self.lblImg.setText("")
        self.lblImg.setObjectName("lblImg")
        self.btnGuardar = QtWidgets.QPushButton(self.frame)
        self.btnGuardar.setGeometry(QtCore.QRect(20, 60, 91, 23))
        self.btnGuardar.setStyleSheet("background-color: white;\n"
"border-radius: 3px;\n"
"border: 1px solid black;")
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
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
        self.btnCargarImg.setText(_translate("MainWindow", "Cargar imagen"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
