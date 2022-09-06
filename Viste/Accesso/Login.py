import pickle

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Cliente import Cliente
from Attivita.Portafoglio import Portafoglio
from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathFiles import PATH_CURRENT_USER, PATH_CURRENT_WALLET
from Utils.Const.PathViste import PATH_VISTA_LOGIN
from Viste.Accesso.Signup import Signup
from Viste.Amministratore.VistaPannelloDiControllo import VistaPannelloDiControllo
from Viste.Cliente.VistaHome import VistaHome


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi(PATH_VISTA_LOGIN, self)
        self.gestore_clienti = None
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.loginbutton.clicked.connect(self.go_accedi)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.go_registra)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    # si verificano due casi:
    # se le credinziali inserite sono "admin" e "password" -> mostra il pannello di controllo amministratore
    # se le credenziali inserite sono di un utente qualsiasi:
    #   controllo se esiste un cliente con tale credenziali, se esiste -> mostro la homepage del cliente
    def go_accedi(self):
        id = self.id.text().strip()
        password = self.password.text()

        if id == "admin" and password == "password":
            self.admin = VistaPannelloDiControllo()
            self.admin.show()
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            self.close()
        else:
            cliente = GestoreClienti().ricerca_cliente_id(id)
            portafoglio = GestoreClienti().ricerca_portafoglio_id(id)

            if isinstance(cliente, Cliente) and isinstance(portafoglio, Portafoglio):
                if cliente.password == password:
                    with open(PATH_CURRENT_USER, "wb") as f:
                        pickle.dump(cliente, f, pickle.HIGHEST_PROTOCOL)
                    with open(PATH_CURRENT_WALLET, "wb") as f:
                        pickle.dump(portafoglio, f, pickle.HIGHEST_PROTOCOL)
                    self.homepage = VistaHome()
                    self.homepage.show()
                    self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
                    self.close()
                else:
                    QMessageBox.warning(self, "Attenzione!", "Password errata!")
            else:
                QMessageBox.warning(self, "Attenzione!", "Cliente non trovato con questo ID")

    def go_registra(self):
        self.signup = Signup()
        self.signup.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.close()


