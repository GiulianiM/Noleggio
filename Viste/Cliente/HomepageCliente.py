from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Gestione.Backup import Backup
from Viste.Cliente.VistaCorsa import Corsa, VistaCorsa
from Viste.Cliente.Profilo import Profilo


class HomepageCliente(QDialog):
    def __init__(self, cliente):
        super(HomepageCliente, self).__init__()
        loadUi("viste/cliente/gui/homepage_utente.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_profilo.clicked.connect(self.go_profilo)
        self.bottone_corsa.clicked.connect(self.go_corsa)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        """m1 = Mezzo()
        m1.inserisci_mezzo()"""

    def go_profilo(self):
        self.profilo = Profilo(self.cliente)
        self.profilo.show()

    def go_corsa(self):
        self.vista_corsa = VistaCorsa(self.cliente)
        self.vista_corsa.show()

    def closeEvent(self, event):
        Backup().esegui_backup()
