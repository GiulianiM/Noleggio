from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Viste.Cliente.Profilo import Profilo


class HomepageCliente(QDialog):
    def __init__(self, cliente):
        super(HomepageCliente, self).__init__()
        loadUi("viste/cliente/gui/homepage_utente.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_profilo.clicked.connect(self.go_profilo)
        self.bottone_corsa.clicked.connect(self.go_corsa)

    def go_profilo(self):
        self.profilo = Profilo(self.cliente)
        self.profilo.show()


    def go_corsa(self):
        pass