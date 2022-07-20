from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Gestione.Backup import Backup
from Viste.Amministratore.CUDCliente import CUDCliente
from Viste.Amministratore.CUDMezzo import CUDMezzo
from Viste.Amministratore.VisualizzaStatistiche import VisualizzaStatistiche


class ControlPanel(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Viste/Amministratore/GUI/homepage_amministratore.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_cud_cliente.clicked.connect(self.go_CUD_cliente)
        self.bottone_cud_mezzo.clicked.connect(self.go_CUD_mezzi)
        self.bottone_visualizza_statistiche.clicked.connect(self.go_visualizza_statistiche)

    def go_CUD_cliente(self):
        self.cud_cliente = CUDCliente()
        self.cud_cliente.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_CUD_mezzi(self):
        self.cud_mezzi = CUDMezzo()
        self.cud_mezzi.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_visualizza_statistiche(self):
        self.visualizza_statistiche = VisualizzaStatistiche()
        self.visualizza_statistiche.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def closeEvent(self, event):
        Backup().esegui_backup()
