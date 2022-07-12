import os
import pickle

from Servizio.Monopattino import Monopattino


class Ricevuta:

    def __init__(self):
        self.codiceCliente = ""
        self.codice = ""
        self.tempoUtilizzo = 0.0
        self.costoTotale = 0.0

    # crea una nuova ricevuta
    def stilaRicevuta(self, codiceCliente):
        self.codiceCliente = codiceCliente
        self.codice =  # todo codice
        # todo data di inizio e di fine corsa
        self.tempoUtilizzo = self.getTempoUtilizzo()
        self.costoTotale = self.getCostoTotale()

        ricevute = {}
        if os.path.isfile("Dati/Ricevute.pickle"):
            with open("Dati/Ricevute.pickle", "rb") as f:
                ricevute = pickle.load(f)

        ricevute[self.codice] = self

        with open("Dati/Ricevute.pickle", "wb") as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)

    # ritorna il costo totale della corsa
    def getCostoTotale(self):
        self.costoTotale = round(self.tempoUtilizzo * Monopattino().costoMinuto, 2)
        return self.costoTotale

    # ritorna il trempo totale di utilizzo del mezzo
    def getTempoUtilizzo(self):
        # round(int((self.dataFine - self.dataInizio).total_seconds()) / 60, 2)
        self.tempoUtilizzo =  # todo tempo utilizzo
        return self.tempoUtilizzo

    # funzione che restituisce un dizionario di tutte le ricevute
    def getRicevute(self):
        if os.path.isfile("Dati/Ricevute.pickle"):
            with open("Dati/Ricevute.pickle", "rb") as f:
                ricevute = dict(pickle.load(f))
                return ricevute
        else:
            return None

    # funzione che stampa a schermo la ricevuta
    def getRicevutaToString(self):
        return "Costo per minuto: " + str(Monopattino().costoMinuto) + "\n" + \
               "Minuti utilizzati: " + str(self.tempoUtilizzo) + "\n" + \
               "Costo totale: " + str(self.getCostoTotale()) + "\n" + \
               "Data inizio: " + str(self.dataInizio) + "\n" + \
               "Data fine: " + str(self.dataFine) + "\n"

    # funzione che restituisce la lista di tutte le ricevute di un cliente specifico
    def getRicevuteCliente(self, codiceCliente):
        ricevute = {}
        if os.path.isfile("Dati/Ricevute.pickle"):
            with open("Dati/Ricevute.pickle", "rb") as f:
                ricevute = pickle.load(f)
        return [ricevuta for ricevuta in ricevute.values() if ricevuta.codiceCliente == codiceCliente]
