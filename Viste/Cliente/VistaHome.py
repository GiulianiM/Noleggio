from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Utils.Const.PathViste import PATH_VISTA_HOME
from Viste.Cliente.VistaCorsa import VistaCorsa
from Viste.Cliente.VistaProfilo import VistaProfilo


class VistaHome(QDialog):
    def __init__(self):
        super(VistaHome, self).__init__()
        loadUi(PATH_VISTA_HOME, self)
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_profilo.clicked.connect(self.go_profilo)
        self.bottone_corsa.clicked.connect(self.go_corsa)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_profilo(self):
        self.profilo = VistaProfilo()
        self.profilo.show()

    def go_corsa(self):
        self.vista_corsa = VistaCorsa()
        self.vista_corsa.show()
