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
        MainWindow.resize(1000, 466)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 466))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 466))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 420))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 420))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblImg1 = QtWidgets.QLabel(self.frame)
        self.lblImg1.setMinimumSize(QtCore.QSize(200, 250))
        self.lblImg1.setMaximumSize(QtCore.QSize(200, 250))
        self.lblImg1.setText("")
        self.lblImg1.setObjectName("lblImg1")
        self.horizontalLayout.addWidget(self.lblImg1)
        self.lblImg2 = QtWidgets.QLabel(self.frame)
        self.lblImg2.setMinimumSize(QtCore.QSize(200, 250))
        self.lblImg2.setMaximumSize(QtCore.QSize(200, 250))
        self.lblImg2.setText("")
        self.lblImg2.setObjectName("lblImg2")
        self.horizontalLayout.addWidget(self.lblImg2)
        self.lblImg3 = QtWidgets.QLabel(self.frame)
        self.lblImg3.setMinimumSize(QtCore.QSize(200, 250))
        self.lblImg3.setMaximumSize(QtCore.QSize(200, 250))
        self.lblImg3.setText("")
        self.lblImg3.setObjectName("lblImg3")
        self.horizontalLayout.addWidget(self.lblImg3)
        self.lblImg4 = QtWidgets.QLabel(self.frame)
        self.lblImg4.setMinimumSize(QtCore.QSize(200, 250))
        self.lblImg4.setMaximumSize(QtCore.QSize(200, 250))
        self.lblImg4.setText("")
        self.lblImg4.setObjectName("lblImg4")
        self.horizontalLayout.addWidget(self.lblImg4)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnGrises = QtWidgets.QPushButton(self.centralwidget)
        self.btnGrises.setEnabled(False)
        self.btnGrises.setMinimumSize(QtCore.QSize(0, 36))
        self.btnGrises.setObjectName("btnGrises")
        self.verticalLayout_4.addWidget(self.btnGrises)
        self.btnRGB = QtWidgets.QPushButton(self.centralwidget)
        self.btnRGB.setEnabled(False)
        self.btnRGB.setMinimumSize(QtCore.QSize(0, 36))
        self.btnRGB.setObjectName("btnRGB")
        self.verticalLayout_4.addWidget(self.btnRGB)
        self.btnHSV = QtWidgets.QPushButton(self.centralwidget)
        self.btnHSV.setEnabled(False)
        self.btnHSV.setMinimumSize(QtCore.QSize(0, 36))
        self.btnHSV.setObjectName("btnHSV")
        self.verticalLayout_4.addWidget(self.btnHSV)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sliderR = QtWidgets.QSlider(self.centralwidget)
        self.sliderR.setEnabled(False)
        self.sliderR.setMinimumSize(QtCore.QSize(200, 0))
        self.sliderR.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderR.setMaximum(255)
        self.sliderR.setOrientation(QtCore.Qt.Horizontal)
        self.sliderR.setObjectName("sliderR")
        self.verticalLayout_5.addWidget(self.sliderR, 0, QtCore.Qt.AlignHCenter)
        self.sliderG = QtWidgets.QSlider(self.centralwidget)
        self.sliderG.setEnabled(False)
        self.sliderG.setMinimumSize(QtCore.QSize(200, 0))
        self.sliderG.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderG.setMaximum(255)
        self.sliderG.setOrientation(QtCore.Qt.Horizontal)
        self.sliderG.setObjectName("sliderG")
        self.verticalLayout_5.addWidget(self.sliderG, 0, QtCore.Qt.AlignHCenter)
        self.sliderB = QtWidgets.QSlider(self.centralwidget)
        self.sliderB.setEnabled(False)
        self.sliderB.setMinimumSize(QtCore.QSize(200, 0))
        self.sliderB.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderB.setMaximum(255)
        self.sliderB.setOrientation(QtCore.Qt.Horizontal)
        self.sliderB.setObjectName("sliderB")
        self.verticalLayout_5.addWidget(self.sliderB, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sliderH = QtWidgets.QSlider(self.centralwidget)
        self.sliderH.setEnabled(False)
        self.sliderH.setMinimumSize(QtCore.QSize(200, 0))
        self.sliderH.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderH.setMaximum(255)
        self.sliderH.setOrientation(QtCore.Qt.Horizontal)
        self.sliderH.setObjectName("sliderH")
        self.verticalLayout.addWidget(self.sliderH, 0, QtCore.Qt.AlignHCenter)
        self.sliderS = QtWidgets.QSlider(self.centralwidget)
        self.sliderS.setEnabled(False)
        self.sliderS.setMinimumSize(QtCore.QSize(200, 0))
        self.sliderS.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderS.setMaximum(255)
        self.sliderS.setOrientation(QtCore.Qt.Horizontal)
        self.sliderS.setObjectName("sliderS")
        self.verticalLayout.addWidget(self.sliderS, 0, QtCore.Qt.AlignHCenter)
        self.sliderV = QtWidgets.QSlider(self.centralwidget)
        self.sliderV.setEnabled(False)
        self.sliderV.setMinimumSize(QtCore.QSize(200, 0))
        self.sliderV.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderV.setMaximum(255)
        self.sliderV.setOrientation(QtCore.Qt.Horizontal)
        self.sliderV.setObjectName("sliderV")
        self.verticalLayout.addWidget(self.sliderV, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEdicion = QtWidgets.QMenu(self.menuBar)
        self.menuEdicion.setEnabled(False)
        self.menuEdicion.setObjectName("menuEdicion")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuAbrirImg = QtWidgets.QAction(MainWindow)
        self.menuAbrirImg.setObjectName("menuAbrirImg")
        self.menuSalir = QtWidgets.QAction(MainWindow)
        self.menuSalir.setObjectName("menuSalir")
        self.menuGuardarGrises = QtWidgets.QAction(MainWindow)
        self.menuGuardarGrises.setEnabled(True)
        self.menuGuardarGrises.setObjectName("menuGuardarGrises")
        self.menuGuardarRGB = QtWidgets.QAction(MainWindow)
        self.menuGuardarRGB.setObjectName("menuGuardarRGB")
        self.menuGuardarHSV = QtWidgets.QAction(MainWindow)
        self.menuGuardarHSV.setObjectName("menuGuardarHSV")
        self.menuArchivo.addAction(self.menuAbrirImg)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.menuSalir)
        self.menuEdicion.addAction(self.menuGuardarGrises)
        self.menuEdicion.addAction(self.menuGuardarRGB)
        self.menuEdicion.addAction(self.menuGuardarHSV)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuEdicion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edicion de Imagen"))
        self.btnGrises.setText(_translate("MainWindow", "Escala de Grises"))
        self.btnRGB.setText(_translate("MainWindow", "RGB"))
        self.btnHSV.setText(_translate("MainWindow", "HSV"))
        self.label.setText(_translate("MainWindow", "R"))
        self.label_3.setText(_translate("MainWindow", "B"))
        self.label_2.setText(_translate("MainWindow", "G"))
        self.label_4.setText(_translate("MainWindow", "H"))
        self.label_5.setText(_translate("MainWindow", "S"))
        self.label_6.setText(_translate("MainWindow", "V"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEdicion.setTitle(_translate("MainWindow", "Edición"))
        self.menuAbrirImg.setText(_translate("MainWindow", "Abrir Imagen"))
        self.menuSalir.setText(_translate("MainWindow", "Salir"))
        self.menuGuardarGrises.setText(_translate("MainWindow", "Guardar Escala de Grises"))
        self.menuGuardarRGB.setText(_translate("MainWindow", "Guardar RGB"))
        self.menuGuardarHSV.setText(_translate("MainWindow", "Guardar HSV"))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())