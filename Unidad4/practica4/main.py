from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

login = uic.loadUi("login.ui")

#Ejecucion de los botones

def validar():
    # print("Hola mundo")
    usuario = login.txtUsuario.text()
    password = login.txtPassword.text()
    
    if usuario == 'admin' and password == '123':
        login.lblMsj.setText("Correcto")
    else:
        login.lblMsj.setText("Incorrecto")
        

def cerrar():
    # print("cerrar")
    login.destroy()

login.btnAceptar.clicked.connect(validar)
login.btnCancelar.clicked.connect(cerrar)


login.show()

app.exec()