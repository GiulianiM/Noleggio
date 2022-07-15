from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Cliente import Cliente
from Viste.Cliente.HomepageCliente import HomepageCliente


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi("Viste/Accesso/GUI/Login.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        id = self.id.text()
        password = self.password.text()
        cliente = Cliente().ricerca_cliente_codice(id)
        if cliente is None:
            QMessageBox.warning(self, "Attenzione!", "Cliente con questo codice non trovato")
        elif cliente.password != password:
            QMessageBox.warning(self, "Attenzione!", "Password errata")
        else:
            self.homepage = HomepageCliente(cliente)
            self.homepage.show()
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            self.close()

    def gotocreate(self):
        self.signup = Signup()
        self.signup.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.close()


class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("Viste/Accesso/GUI/createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        # if self.check_campi():
        cliente = Cliente()
        nome = self.nome.text().capitalize()
        cognome = self.cognome.text().capitalize()
        cf = self.cf.text().upper()
        telefono = self.telefono.text()
        password = self.password.text()
        if Signup.check_campi(self):
            cliente, message = cliente.crea_cliente(nome=nome, cognome=cognome, telefono=telefono, codicefiscale=cf,
                                                    password=password)
            if cliente is not None:
                QMessageBox.information(self, "Attenzione!", message + "codice: " + str(cliente.codice) + " password: " + str(cliente.password))
                self.homepage_cliente = HomepageCliente(cliente)
                self.homepage_cliente.show()
                self.close()
            else:
                QMessageBox.warning(self, "Attenzione!", message)

    def check_campi(self):
        regex = r"[a-zA-Z0-9]"
        # il nome deve avere minimo 3 caratteri
        if len(self.nome.text()) > 2:
            # il cognome deve avere minimo 3 caratteri
            if len(self.cognome.text()) > 2:
                # il codice fiscale deve essere esattamente di 16 caratteri
                if len(self.cf.text()) == 16 and self.cf.text().isalnum():
                    # il numero di telefono puo avere solo 10 cifre
                    if len(self.telefono.text()) == 10 and str(self.telefono.text()).isnumeric():
                        return True
                    else:
                        QMessageBox.warning(self, "Attenzione!", "Il numero di telefono puo contenere solo 10 cifre")
                else:
                    QMessageBox.warning(self, "Attenzione!", "Il codice fiscale puo contenere solo 16 caratteri")
            else:
                QMessageBox.warning(self, "Attenzione!", "Il cognome deve avere almeno 3 caratteri")
        else:
            QMessageBox.warning(self, "Attenzione!", "Il nome deve avere almeno 3 caratteri")
        return False
