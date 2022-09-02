from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.GestoreStatistiche import GestoreStatistiche
from Utils.Const.PathViste import PATH_VISTA_STATISTICHE


class VistaStatistiche(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(PATH_VISTA_STATISTICHE, self)
        self.gestore_statistiche = GestoreStatistiche()
        self.setup_ui()

    def setup_ui(self):
        self.back_button.clicked.connect(self.go_back)
        self.ricavo_label_to_edit.setText(self.gestore_statistiche.get_ricavo_medio())
        self.ricavo_totale_label_to_edit.setText(self.gestore_statistiche.get_ricavo_totale())
        self.tempo_label_to_edit.setText(self.gestore_statistiche.get_tempo_medio())
        self.tempo_totale_label_to_edit.setText(self.gestore_statistiche.get_tempo_totale())
        self.num_corse_label_to_edit.setText(self.gestore_statistiche.get_numero_corse_effettuate())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_back(self):
        self.close()
