import os
import pickle

import shortuuid

from Servizio.Mezzo import Mezzo


class Monopattino(Mezzo):

    def __init__(self):
        super(Monopattino, self).__init__()
        self.costoMinuto = 0.20
        self.disponibile = True


    def setDisponibilita(self, codiceMezzo, disponibile):
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                mezzi = pickle.load(f)

            mezzi[codiceMezzo].disponibile = disponibile

            with open("Dati/Mezzi.pickle", "wb") as f:
                pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)

    # Metodo che aggiunge un monopattino
    def inserisciMezzo(self):
        self.codice = shortuuid.uuid()[:5]

        monopattini = {}
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                monopattini = pickle.load(f)

        monopattini[self.codice] = self

        with open("Dati/Mezzi.pickle", "wb") as f:
            pickle.dump(monopattini, f, pickle.HIGHEST_PROTOCOL)

    # Metodo che restituisce il codice del monopattino
    def getCodiceMezzoDisponibile(self):
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                monopattini = dict(pickle.load(f))

            for codice, monopattino in monopattini.items():
                if monopattino.disponibile:
                    return codice

        return None

    # Metodo che elimina il monopattino dalla lista
    def rimuoviMonopattino(self, codiceMezzo):
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                mezzi = dict(pickle.load(f))
                del mezzi[codiceMezzo]
            with open("Dati/Mezzi.pickle", "wb") as f:
                pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviMezzo()
        self.disponibile = False
        self.costoMinuto = 0.0
        del self


