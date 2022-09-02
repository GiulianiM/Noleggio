class Statistiche:

    def __init__(self, ricevute):
        self.ricevute = ricevute
        self.num_ricevute = len(ricevute)

    def ricavo_medio(self):
        return self.ricavo() / self.num_ricevute

    def ricavo(self):
        if self.ricevute is not None:
            ricavo = 0.0
            for ricevuta in self.ricevute.values():
                ricavo += ricevuta.costo_totale
            return ricavo
        else:
            return 0.0

    def tempo_utilizzo_medio(self):
        return self.tempo_utilizzo() / self.num_ricevute

    def tempo_utilizzo(self):
        if self.ricevute is not None:
            tempo_medio = 0.00
            for ricevuta in self.ricevute.values():
                tempo_medio += ricevuta.tempo_totale
            return tempo_medio
        else:
            return 0.0
