from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


class ModificaProfilo(QDialog):
    def __init__(self, cliente):
        super(ModificaProfilo, self).__init__()
        loadUi("viste/cliente/gui/modifica_profilo.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.old_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_input_check.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_button.clicked.connect(self.go_conferma_modifiche)

    # eseguo i segenti controlli:
    # 1) le password non devono essere vuote
    # 2) se la password vecchia non corrisponde alla password del cliente
    # 3) se la nuova password è uguale alla vecchia
    # 4) se la nuova password è uguale alla nuova

    def go_conferma_modifiche(self):
        if len(self.old_pw_input.text()) <= 0 or len(self.new_pw_input.text()) <= 0 or len(
                self.new_pw_input_check.text()) <= 0:
            QMessageBox.warning(self, "Attenzione!", "Compilare tutti i campi")
        elif self.old_pw_input.text() != self.cliente.password:
            QMessageBox.warning(self, "Attenzione!", "Password vecchia errata")
        elif self.new_pw_input.text() != self.new_pw_input_check.text():
            QMessageBox.warning(self, "Attenzione!", "Le password non corrispondono")
        elif self.new_pw_input.text() == self.old_pw_input.text() or self.new_pw_input_check.text() == self.old_pw_input.text():
            QMessageBox.warning(self, "Attenzione!", "La nuova password è la vecchia")
        else:
            message = self.cliente.modifica_cliente(nuova_pwd=self.new_pw_input.text(),
                                                    codice_cliente=self.cliente.codice)
            QMessageBox.information(self, "Attenzione!", message)
            self.close()
