from Controller.GestoreRicevute import GestoreRicevute
from Gestione.Statistiche import Statistiche


class GestoreStatistiche:
    def __init__(self):
        self.gestore_ricevute = GestoreRicevute()
        self.ricevute = self.gestore_ricevute.get_ricevute()
        self.statistiche = Statistiche(self.ricevute)

    def get_numero_corse_effettuate(self):
        return str(self.statistiche.num_ricevute)

    def get_tempo_medio(self):
        return self.formatta_tempo(self.statistiche.tempo_utilizzo_medio())

    def get_tempo_totale(self):
        return self.formatta_tempo(self.statistiche.tempo_utilizzo())

    def get_ricavo_medio(self):
        return format(self.statistiche.ricavo_medio(), '.2f') + "€"

    def get_ricavo_totale(self):
        return format(self.statistiche.ricavo(), ".2f") + "€"

    def formatta_tempo(self, tempo):
        if tempo >= 60:
            return format(tempo / 60, '.1f') + "minuti"
        else:
            return format(tempo, '.1f') + "secondi"
