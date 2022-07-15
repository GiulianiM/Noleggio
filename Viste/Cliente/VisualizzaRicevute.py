from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaRicevute(QDialog):
    def __init__(self, cliente):
        super(VisualizzaRicevute, self).__init__()
        loadUi("viste/cliente/gui/visualizza_ricevute.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_indietro)

    def go_indietro(self):
        self.close()
