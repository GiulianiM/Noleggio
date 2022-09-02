from builtins import len

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathViste import PATH_VISTA_MODIFICA_PROFILO


class VistaModificaProfilo(QDialog):
    closed = pyqtSignal()

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
                    QMessageBox.warning(self, "Attenzione", "Nessun utente trovato!")
                else:
                    QMessageBox.information(self, "Attenzione", "Modificato Correttamente!")
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
            QMessageBox.warning(self,
                                "Attenzione!",
                                '<p style=color:white>La vecchia password non è corretta</p>'
                                )
            return False

        elif self.new_pw_input.text() != self.new_pw_input_check.text():
            QMessageBox.warning(self,
                                "Attenzione!",
                                '<p style=color:white>Le nuove password non corrispondono</p>'
                                )
            return False
        elif self.new_pw_input.text() == self.old_pw_input.text() or self.new_pw_input_check.text() == self.old_pw_input.text():
            QMessageBox.warning(self,
                                "Attenzione!",
                                '<p style=color:white>La nuova password è uguale alla vecchia</p>'
                                )
            return False
        elif len(self.new_pw_input.text()) < 4 or len(self.new_pw_input_check.text()) < 4:
            QMessageBox.warning(self,
                                "Attenzione!",
                                '<p style=color:white>La nuova password deve avere almeno 4 caratteri</p>'
                                )
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
        if len(self.new_name_input.text()) > 3:
            self.nome = self.new_name_input.text()
        elif 3 > len(self.new_name_input.text()) > 0:
            QMessageBox.warning(self,
                                "Attenzione!",
                                "<p style=color:white>Il nome deve avere almeno 3 caratteri"
                                )
            return False

        # check cognome
        if len(self.new_surname_input.text()) > 3:
            self.cognome = self.new_surname_input.text()
        elif 3 > len(self.new_surname_input.text()) > 0:
            QMessageBox.warning(self,
                                "Attenzione!",
                                "<p style=color:white>Il cognome deve avere almeno 3 caratteri"
                                )
            return False

        # check codice fiscale
        # se ha inserito 16 caratteri (senza spazi, ecc...) --> OK
        if len(self.new_cf_input.text()) == 16 and self.new_cf_input.text().isalnum():
            self.cf = self.new_cf_input.text()
        # altrimenti --> Genera Errore!
        elif len(self.new_cf_input.text()) != 16:
            if len(self.new_cf_input.text()) > 0:
                if not self.new_cf_input.text().isalnum():
                    QMessageBox.warning(self,
                                        "Attenzione!",
                                        "<p style=color:white>Il id_cliente fiscale puo contenere solo 16 caratteri"
                                        )
                    return False

        # check telefono
        # se ha inserito 10 numeri --> OK
        if len(self.new_phone_input.text()) == 10 and self.new_phone_input.text().isnumeric():
            self.telefono = self.new_phone_input.text()
        # altrimenti  --> Genera Errore!
        elif len(self.new_phone_input.text()) != 10:
            if len(self.new_phone_input.text()) > 0:
                if not self.new_phone_input.text().isnumeric():
                    QMessageBox.warning(self,
                                        "Attenzione!",
                                        "<p style=color:white>Il numero di telefono puo contenere solo 10 cifre"
                                        )
                    return False

        return True

    def closeEvent(self, event):
        self.closed.emit()

    def go_back(self):
        self.close()
