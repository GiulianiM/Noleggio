from Attivita.Ricevuta import Ricevuta


class Statistiche:

    def __init__(self):
        self.tempoUtilizzoMedio = 0.0
        self.ricavoMedio = 0.0
        self.ricevute = {}

    def generaStatistiche(self):
        self.ricevute = Ricevuta().getRicevute()
        if self.ricevute is not None:
            self.tempoUtilizzoMedio = self.calcolaTempoUtilizzoMedio()
            self.ricavoMedio = self.calcolaRicavoMedio()
            return round(self.tempoUtilizzoMedio, 2), round(self.ricavoMedio, 2)
        else:
            return 0.0, 0.0

    def calcolaTempoUtilizzoMedio(self):
        if len(self.ricevute) > 0:
            for key, ricevuta in self.ricevute.items():
                self.tempoUtilizzoMedio += ricevuta.tempoUtilizzo
            self.tempoUtilizzoMedio /= len(self.ricevute)
        return self.tempoUtilizzoMedio

    def calcolaRicavoMedio(self):
        if len(self.ricevute) > 0:
            for key, ricevuta in self.ricevute.items():
                self.ricavoMedio += ricevuta.costoTotale
            self.ricavoMedio /= len(self.ricevute)
        return self.ricavoMedio
