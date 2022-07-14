import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Viste.Accesso.Login.Signup import Signup


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi("Viste/Accesso/Login/Login.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        id = self.id.text()
        password = self.password.text()
        print("Accesso effettuato con id: ", id, "e password:", password)

    def gotocreate(self):
        self.signup = Signup()
        self.signup.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.close()



