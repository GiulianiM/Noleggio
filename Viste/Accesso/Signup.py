from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathViste import PATH_VISTA_SIGNUP
from Viste.Cliente.VistaHome import VistaHome


class Signup(QDialog):
    closed = QtCore.pyqtSignal()

    # Si possono verificare due casi:
    # UNO. L'amministratore vuole creare un nuovo account per un cliente -> is_cliente = False
    # DUE. Un cliente vuole creare un nuovo account -> is_cliente = True
    # la variabile "is_cliente" se True mostra la homepage cliente
    def __init__(self, is_cliente=True):
        super(Signup, self).__init__()
        loadUi(PATH_VISTA_SIGNUP, self)
        self.gestore_clienti = GestoreClienti()
        self.is_cliente = is_cliente
        self.setup_ui()

    def setup_ui(self):
        self.signupbutton.clicked.connect(self.crea_account)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def crea_account(self):

        if self.check_campi():
            nome = self.nome.text().capitalize().strip()
            cognome = self.cognome.text().capitalize().strip()
            CF = self.cf.text().upper().strip()
            telefono = self.telefono.text().strip()
            password = self.password.text().strip()

            cliente, portafoglio = self.gestore_clienti.registra_cliente(
                nome=nome,
                cognome=cognome,
                cf=CF,
                telefono=telefono,
                password=password
            )
            if cliente is None and portafoglio is None:
                self.show_msg(
                    livello=2,
                    titolo="Creazione Account!",
                    msg='<p style=color:white> Errore! Account già esistente!'
                )
            else:
                self.show_msg(
                    livello=0,
                    titolo="Creazione Account!",
                    msg='<p style=color:white> Registrato con successo,<br> con id: "{}" e password: "{}"</p>'.format(
                        cliente.id,
                        cliente.password
                    )
                )

                if self.is_cliente:
                    self.homepage_cliente = VistaHome()
                    self.homepage_cliente.show()
                    self.close()
                else:
                    self.close()

    def check_campi(self):
        # il nome deve avere minimo 3 caratteri
        if len(self.nome.text()) < 3:
            self.show_msg(
                livello=1,
                titolo="Attenzione!",
                msg="Il nome deve avere almeno 3 caratteri"
            )

        # il cognome deve avere minimo 3 caratteri
        elif len(self.cognome.text()) < 3:
            self.show_msg(
                livello=1,
                titolo="Attenzione!",
                msg="Il cognome deve avere almeno 3 caratteri"
            )
        # il id_cliente fiscale deve essere esattamente di 16 caratteri
        elif len(self.cf.text()) != 16 or not self.cf.text().isalnum():
            self.show_msg(
                livello=1,
                titolo="Attenzione!",
                msg="Il codice fiscale può contenere solo 16 caratteri"
            )
        # il numero di telefono puo avere solo 10 cifre
        elif len(self.telefono.text()) != 10 or not str(self.telefono.text()).isnumeric():
            self.show_msg(
                livello=1,
                titolo="Attenzione!",
                msg="Il numero di telefono può contenere solo 10 cifre"
            )
        # la password deve avere minimo 4 caratteri
        elif len(self.password.text()) < 4:
            self.show_msg(
                livello=1,
                titolo="Attenzione!",
                msg="La password deve avere almeno 4 caratteri"
            )
        else:
            return True

    def show_msg(self, livello, titolo, msg):
        mb = QMessageBox()
        mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mb.setWindowTitle(titolo)
        if livello == 0:
            mb.setIcon(QMessageBox.Information)
        elif livello == 1:
            mb.setIcon(QMessageBox.Warning)
        mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mb.setText(msg)
        mb.exec()

    def closeEvent(self, event):
        self.closed.emit()
