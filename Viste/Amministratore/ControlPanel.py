from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import Viste.Amministratore.VisualizzaClienti as VisualizzaClienti
from Viste.Amministratore.CUDCliente import CUDCliente
from Viste.Amministratore.CUDMezzo import CUDMezzo
from Viste.Amministratore.VisualizzaMezzi import VisualizzaMezzi
from Viste.Amministratore.VisualizzaStatistiche import VisualizzaStatistiche


class ControlPanel(QDialog):
    def __init__(self):
        super(ControlPanel, self).__init__()
        loadUi("Viste/Accesso/Login/Login.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.visualizza_clienti_button.connect(self.go_visualizza_clienti)
        self.CUD_clienti_button.connect(self.go_CUD_cliente)
        self.visualizza_mezzi_button.connect(self.go_visualizza_mezzi)
        self.CUD_mezzi_button.connect(self.go_CUD_mezzi)
        self.visualizza_statistiche_button.connect(self.go_visualizza_statistiche)

    def go_visualizza_clienti(self):
        self.visualizza_clienti = VisualizzaClienti()
        self.visualizza_clienti.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_CUD_cliente(self):
        self.cud_cliente = CUDCliente()
        self.cud_cliente.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_visualizza_mezzi(self):
        self.visualizza_mezzi = VisualizzaMezzi()
        self.visualizza_mezzi.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_CUD_mezzi(self):
        self.cud_mezzi = CUDMezzo()
        self.cud_mezzi.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_visualizza_statistiche(self):
        self.visualizza_statistiche = VisualizzaStatistiche()
        self.visualizza_statistiche.show()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)