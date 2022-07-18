from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Attivita.Ricevuta import Ricevuta


class VisualizzaStatistiche(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('Viste/Amministratore/GUI/statistiche.ui', self)
        self.back_button.clicked.connect(self.go_back)
        self.ricavo_label_to_edit.setText(self.get_ricavo_medio() + " €")
        self.tempo_label_to_edit.setText(self.get_tempo_medio() + " min")
        self.num_corse_label_to_edit.setText(str(len(Ricevuta().get_ricevute())))

    def get_ricavo_medio(self):
        ricevute = Ricevuta().get_ricevute()
        ricavo_medio = 0.00
        if ricevute is not None:
            for ricevuta in ricevute.values():
                ricavo_medio += ricevuta.get_costo_totale()
            return str(ricavo_medio / len(ricevute))
        else:
            return str(ricavo_medio)

    def get_tempo_medio(self):
        ricevute = Ricevuta().get_ricevute()
        tempo_medio = 0.00
        if ricevute is not None:
            for ricevuta in ricevute.values():
                tempo_medio += ricevuta.get_tempo_utilizzo()
            return str(tempo_medio / len(ricevute))
        else:
            return str(tempo_medio)

    def go_back(self):
        self.close()
