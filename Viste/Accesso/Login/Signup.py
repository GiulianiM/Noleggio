from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Cliente import Cliente


class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("Viste/Accesso/Login/createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        if self.check_campi():
            cliente = Cliente()
            nome = self.nome.text()
            cognome = self.cognome.text()
            cf = self.cf.text()
            telefono = self.telefono.text()
            password = self.password.text()
            message = cliente.crea_cliente(nome=nome, cognome=cognome, telefono=telefono, codicefiscale=cf,
                                           password=password)
            QMessageBox.information(self, "Attenzione!", message)

    def check_campi(self):
        # il nome deve avere minimo 3 caratteri
        if len(self.nome.text()) > 2:
            # il cognome deve avere minimo 3 caratteri
            if len(self.cognome.text()) > 2:
                # il codice fiscale deve essere esattamente di 16 caratteri
                if len(self.cf.text()) == 16:
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
