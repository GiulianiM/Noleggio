from builtins import len

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


class ModificaProfilo(QDialog):
    closed = pyqtSignal()

    def __init__(self, cliente):
        super(ModificaProfilo, self).__init__()
        loadUi("viste/cliente/gui/modifica_profilo.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.old_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_input_check.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_button.clicked.connect(self.go_conferma_modifiche)
        self.back_button.clicked.connect(self.go_indietro)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_conferma_modifiche(self):
        self.check_campi_password()
        self.check_campi_profilo()
        print (self.password, self.nome, self.cognome, self.codicefiscale, self.telefono, self.password, self.cliente.codice)
        message = self.cliente.modifica_cliente(nuovo_nome=self.nome,
                                                nuovo_cognome=self.cognome,
                                                nuovo_cf=self.codicefiscale,
                                                nuovo_telefono=self.telefono,
                                                nuova_password=self.password,
                                                codice_cliente=self.cliente.codice)
        QMessageBox.information(self, "Attenzione!", message)
        self.close()

    def check_campi_password(self):
        if len(self.old_pw_input.text()) == 0 and len(self.new_pw_input.text()) == 0 and len(
                self.new_pw_input_check.text()) == 0:
            self.password = self.cliente.password
            return True

        if self.old_pw_input.text() != self.cliente.password:
            QMessageBox.warning(self, "Attenzione!", '<p style=color:white>La vecchia password non è corretta</p>')
        elif self.new_pw_input.text() != self.new_pw_input_check.text():
            QMessageBox.warning(self, "Attenzione!", '<p style=color:white>Le nuove password non corrispondono</p>')
        elif self.new_pw_input.text() == self.old_pw_input.text() or self.new_pw_input_check.text() == self.old_pw_input.text():
            QMessageBox.warning(self, "Attenzione!",
                                '<p style=color:white>La nuova password è uguale alla vecchia</p>')
        elif len(self.new_pw_input.text()) < 4 or len(self.new_pw_input_check.text()) < 4:
            QMessageBox.warning(self, "Attenzione!",
                                '<p style=color:white>La nuova password deve avere almeno 4 caratteri</p>')
        else:
            self.password = self.new_pw_input.text()

    def check_campi_profilo(self):
        # il nome deve avere minimo 3 caratteri
        if len(self.new_name_input.text()) == 0:
            self.nome = self.cliente.nome
        elif len(self.new_name_input.text()) < 3 and len(self.new_name_input.text()) > 0:
            QMessageBox.warning(self, "Attenzione!", "<p style=color:white>Il nome deve avere almeno 3 caratteri")
        else:
            self.nome = self.new_name_input.text()

        if len(self.new_surname_input.text()) == 0:
            self.cognome = self.cliente.cognome
        elif len(self.new_surname_input.text()) < 3 and len(self.new_surname_input.text()) > 0:
            QMessageBox.warning(self, "Attenzione!", "<p style=color:white>Il cognome deve avere almeno 3 caratteri")
        else:
            self.cognome = self.new_surname_input.text()

        if len(self.new_cf_input.text()) == 0:
            self.codicefiscale = self.cliente.codicefiscale
        elif len(self.new_cf_input.text()) != 16 or not self.new_cf_input.text().isalnum():
            QMessageBox.warning(self, "Attenzione!",
                                "<p style=color:white>Il codice fiscale puo contenere solo 16 caratteri")
        else:
            self.codicefiscale = self.new_cf_input.text()

        if len(self.new_phone_input.text()) == 0:
            self.telefono = self.cliente.telefono
        elif len(self.new_phone_input.text()) != 10 or not str(self.new_phone_input.text()).isnumeric():
            QMessageBox.warning(self, "Attenzione!",
                                "<p style=color:white>Il numero di telefono puo contenere solo 10 cifre")
        else:
            self.telefono = self.new_phone_input.text()

    def closeEvent(self, event):
        self.closed.emit()

    def go_indietro(self):
        self.close()
