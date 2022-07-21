from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Cliente import Cliente
from Viste.Amministratore.ControlPanel import ControlPanel
from Viste.Cliente.HomepageCliente import HomepageCliente


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi("Viste/Accesso/GUI/Login.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def loginfunction(self):
        id = self.id.text().strip()
        password = self.password.text()
        if id == "admin" and password == "password":
            self.admin = ControlPanel()
            self.admin.show()
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            self.close()
        else:
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
    closed = QtCore.pyqtSignal()

    def __init__(self, is_cliente=True):
        super(Signup, self).__init__()
        loadUi("Viste/Accesso/GUI/createacc.ui", self)
        self.is_cliente = is_cliente
        self.signupbutton.clicked.connect(self.crea_account)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def crea_account(self):
        if self.check_campi():
            nome = self.nome.text().capitalize().strip()
            cognome = self.cognome.text().capitalize().strip()
            cf = self.cf.text().upper().strip()
            telefono = self.telefono.text().strip()
            password = self.password.text().strip()
            cliente = Cliente()
            cliente, message = cliente.crea_cliente(nome=nome, cognome=cognome, telefono=telefono, codicefiscale=cf,
                                                    password=password)
            if cliente is not None:
                message_to_print = '<p style=color:white>{}<br>con codice: "{}" e password: "{}"</p>'.format(message,
                                                                                                             str(cliente.codice),
                                                                                                             str(cliente.password))
                mb = QMessageBox()
                mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
                mb.setWindowTitle("Account creato")
                mb.setIcon(QMessageBox.Information)
                mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
                mb.setText(message_to_print)
                mb.exec()

                if self.is_cliente:
                    self.homepage_cliente = HomepageCliente(cliente)
                    self.homepage_cliente.show()
                    self.close()
            else:
                QMessageBox.warning(self, "Attenzione!", message)

    def check_campi(self):
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
