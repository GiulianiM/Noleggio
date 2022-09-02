from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathViste import PATH_VISTA_PORTAFOGLIO


class VistaPortafoglio(QDialog):
    def __init__(self):
        super(VistaPortafoglio, self).__init__()
        loadUi(PATH_VISTA_PORTAFOGLIO, self)
        self.gestore_clienti = GestoreClienti()
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_back)
        self.confirm_button.clicked.connect(self.go_versamento)
        self.saldo_label_to_edit.setText(self.gestore_clienti.visualizza_portafoglio())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_versamento(self):
        value = self.quantita_da_versare.value()
        saldo = self.gestore_clienti.versa_denaro(value)
        self.saldo_label_to_edit.setText(saldo + "€")

        QMessageBox.information(self,
                                "Attenzione!",
                                '<p style=color:white> Denaro versato correttamente! </p>'
                                )

    def go_back(self):
        self.close()
