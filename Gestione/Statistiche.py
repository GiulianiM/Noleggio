from Attivita.Ricevuta import Ricevuta


class Statistiche:

    def __init__(self):
        self.tempo_utilizzo_medio = 0.0
        self.ricavo_medio = 0.0
        self.ricevute = {}

    def genera_statistiche(self):
        self.ricevute = Ricevuta().get_ricevute()
        if self.ricevute is not None:
            self.tempo_utilizzo_medio = self.calcola_tempo_utilizzo_medio()
            self.ricavo_medio = self.calcola__ricavo_medio()
            return round(self.tempo_utilizzo_medio, 2), round(self.ricavo_medio, 2)
        else:
            return 0.0, 0.0

    def calcola_tempo_utilizzo_medio(self):
        if len(self.ricevute) > 0:
            for key, ricevuta in self.ricevute.items():
                self.tempo_utilizzo_medio += ricevuta.tempo_utilizzo
            self.tempo_utilizzo_medio /= len(self.ricevute)
        return self.tempo_utilizzo_medio

    def calcola_ricavo_medio(self):
        if len(self.ricevute) > 0:
            for key, ricevuta in self.ricevute.items():
                self.ricavo_medio += ricevuta.costo_totale
            self.ricavo_medio /= len(self.ricevute)
        return self.ricavo_medio
