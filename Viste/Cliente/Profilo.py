from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Viste.Cliente.ModificaProfilo import ModificaProfilo
from Viste.Cliente.VisualizzaPortafoglio import VisualizzaPortafoglio
from Viste.Cliente.VisualizzaRicevute import VisualizzaRicevute


class Profilo(QDialog):
    def __init__(self, cliente):
        super(Profilo, self).__init__()
        loadUi("viste/cliente/gui/profilo.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        # setup dei label
        self.id_label_to_edit.setText(str(self.cliente.codice))
        self.nome_label_to_edit.setText(self.cliente.nome)
        self.cognome_label_to_edit.setText(self.cliente.cognome)
        self.cf_label_to_edit.setText(self.cliente.codicefiscale)
        self.telefono_label_to_edit.setText(self.cliente.telefono)
        # setup dei bottoni
        self.back_button.clicked.connect(self.go_indietro)
        self.bottone_modifica.clicked.connect(self.go_modifica_profilo)
        self.bottone_visualizza_portafoglio.clicked.connect(self.go_visualizza_portafoglio)
        self.bottone_visualizza_ricevute.clicked.connect(self.go_visualizza_ricevute)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_modifica_profilo(self):
        self.modifica_profilo = ModificaProfilo(self.cliente)
        self.modifica_profilo.show()

    def go_visualizza_portafoglio(self):
        self.visualizza_portafoglio = VisualizzaPortafoglio(self.cliente)
        self.visualizza_portafoglio.show()

    def go_visualizza_ricevute(self):
        self.visualizza_ricevute = VisualizzaRicevute(self.cliente)
        self.visualizza_ricevute.show()

    def go_indietro(self):
        self.close()
