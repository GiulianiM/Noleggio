from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Attivita.Ricevuta import Ricevuta


class VisualizzaRicevute(QDialog):
    def __init__(self, cliente):
        super(VisualizzaRicevute, self).__init__()
        loadUi("viste/cliente/gui/visualizza_ricevute.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_indietro)
        self.popola_lista_ricevute()

    def go_indietro(self):
        self.close()

    def popola_lista_ricevute(self):
        ricevute = Ricevuta().get_ricevute_cliente(self.cliente.codice)
        if ricevute is not None:
            self.listWidget.clear()
            self.listWidget.addItems(ricevuta.get_ricevuta_to_string() for ricevuta in ricevute)
