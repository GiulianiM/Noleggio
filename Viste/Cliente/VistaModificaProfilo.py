from builtins import len

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathViste import PATH_VISTA_MODIFICA_PROFILO


class VistaModificaProfilo(QDialog):
    closed = QtCore.pyqtSignal()

    def __init__(self, cliente_selezionato=None):
        super(VistaModificaProfilo, self).__init__()
        loadUi(PATH_VISTA_MODIFICA_PROFILO, self)
        if cliente_selezionato is not None:
            self.gestore_clienti = GestoreClienti(cliente_selezionato)
        else:
            self.gestore_clienti = GestoreClienti()

        self.nome = None
        self.cognome = None
        self.telefono = None
        self.password = None
        self.cf = None

        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.old_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_input_check.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_button.clicked.connect(self.go_conferma_modifiche)
        self.back_button.clicked.connect(self.go_back)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_conferma_modifiche(self):
        if self.check_campi_password() and self.check_campi_profilo():
            ret = self.gestore_clienti.modifica_cliente(
                nome=self.nome,
                cognome=self.cognome,
                cf=self.cf,
                telefono=self.telefono,
                password=self.password
            )
            if not ret:
                self.print_messagebox("Errore durante la modifica del profilo")
            else:
                self.print_messagebox("Profilo modificato con successo")
                self.close()

    # controllo della password:
    # 1) se i campi della password rimangono vuoti allora non modificare la password
    # 2) se la vecchia password non coincide con quella inserita
    # 3) se "nuova password" e "reinserisci password" non coincidono
    # 4) se la nuova passowrd coincide alla vecchia password
    # 5) se la password contiene meno di 4 caratteri
    def check_campi_password(self):
        if len(self.old_pw_input.text()) == 0 and len(self.new_pw_input.text()) == 0 and len(
                self.new_pw_input_check.text()) == 0:
            self.password = self.gestore_clienti.cliente_corrente.password
            return True
        if self.old_pw_input.text() != self.gestore_clienti.cliente_corrente.password:
            self.print_messagebox("La vecchia password non coincide con quella inserita")
            return False
        elif self.new_pw_input.text() != self.new_pw_input_check.text():
            self.print_messagebox("Le password non coincidono")
            return False
        elif self.new_pw_input.text() == self.old_pw_input.text() or self.new_pw_input_check.text() == self.old_pw_input.text():
            self.print_messagebox("La nuova password coincide con la vecchia")
            return False
        elif len(self.new_pw_input.text()) < 4 or len(self.new_pw_input_check.text()) < 4:
            self.print_messagebox("La password deve contenere almeno 4 caratteri")
            return False
        else:
            self.password = self.new_pw_input.text()
            return True

    # controllo dei campi anagrafici e telefono:
    # 1) i campi lasciati vuoti non bisogna procedere con la modifica di tali
    # 2) il nome e cognome devono avere più di 3 caratteri
    # 3) il id_cliente fiscale deve contenere 16 caratteri di sole lettere e numeri
    # 4) il telefono deve contenere 10 cifre
    def check_campi_profilo(self):
        # check nome
        if len(self.new_name_input.text()) >= 3:
            self.nome = self.new_name_input.text()
        elif 3 > len(self.new_name_input.text()) > 0:
            self.print_messagebox("Il nome deve contenere almeno 3 caratteri")
            return False

        # check cognome
        if len(self.new_surname_input.text()) >= 3:
            self.cognome = self.new_surname_input.text()
        elif 3 > len(self.new_surname_input.text()) > 0:
            self.print_messagebox("Il cognome deve contenere almeno 3 caratteri")
            return False

        # check codice fiscale
        # se ha inserito 16 caratteri (senza spazi, ecc...) --> OK
        if len(self.new_cf_input.text()) == 16 and self.new_cf_input.text().isalnum():
            self.cf = self.new_cf_input.text()
        # altrimenti --> Genera Errore!
        elif len(self.new_cf_input.text()) > 0:
            self.print_messagebox("Il codice fiscale deve contenere 16 caratteri alfanumerici")
            return False

        # check telefono
        # se ha inserito 10 numeri --> OK
        if len(self.new_phone_input.text()) == 10 and self.new_phone_input.text().isnumeric():
            self.telefono = self.new_phone_input.text()
        # altrimenti  --> Genera Errore!
        elif len(self.new_phone_input.text()) > 0:
            self.print_messagebox("Il numero di telefono deve contenere 10 cifre")
            return False

        return True

    def print_messagebox(self, message):
        mb = QMessageBox()
        mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mb.setWindowTitle("Attenzione")
        mb.setIcon(QMessageBox.Information)
        mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mb.setText(message)
        mb.exec()

    def closeEvent(self, event):
        self.closed.emit()

    def go_back(self):
        self.close()
