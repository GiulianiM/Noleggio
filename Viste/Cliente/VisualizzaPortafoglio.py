from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


class VisualizzaPortafoglio(QDialog):
    def __init__(self, cliente):
        super(VisualizzaPortafoglio, self).__init__()
        loadUi("viste/cliente/gui/portafoglio.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_indietro)
        self.confirm_button.clicked.connect(self.go_conferma_versamento)
        self.saldo_label_to_edit.setText(str(self.cliente.portafoglio.get_saldo()) + "€")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_conferma_versamento(self):
        value = self.quantita_da_versare.value()
        saldo, message = self.cliente.portafoglio.versa_denaro(value)
        self.saldo_label_to_edit.setText(str(saldo) + "€")
        message_to_print = '<p style=color:white>{}</p>'.format(message)
        QMessageBox.information(self, "Attenzione!", message_to_print)

    def go_indietro(self):
        self.close()
