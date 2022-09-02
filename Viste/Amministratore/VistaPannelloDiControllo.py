from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Utils.Const.PathViste import PATH_VISTA_PANNELLO_DI_CONTROLLO
from Viste.Amministratore.VistaClienti import VistaClienti
from Viste.Amministratore.VistaMezzi import VistaMezzi
from Viste.Amministratore.VistaStatistiche import VistaStatistiche


class VistaPannelloDiControllo(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(PATH_VISTA_PANNELLO_DI_CONTROLLO, self)
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_cud_cliente.clicked.connect(self.go_cliente)
        self.bottone_cud_mezzo.clicked.connect(self.go_monopattini)
        self.bottone_visualizza_statistiche.clicked.connect(self.go_visualizza_statistiche)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_cliente(self):
        self.cud_cliente = VistaClienti()
        self.cud_cliente.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_monopattini(self):
        self.cud_monopattino = VistaMezzi()
        self.cud_monopattino.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_visualizza_statistiche(self):
        self.visualizza_statistiche = VistaStatistiche()
        self.visualizza_statistiche.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
