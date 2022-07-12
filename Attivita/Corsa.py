import datetime
import os
import pickle

from Attivita.Ricevuta import Ricevuta


class Corsa:

    def __init__(self):
        self.ricevuta = None
        self.cliente = None
        self.codice = ""
        self.dataInizio = datetime.datetime(year=1970, month=1, day=1)
        self.dataFine = datetime.datetime(year=1970, month=1, day=1)

    # inizializza una nuova corsa
    def iniziaCorsa(self, cliente, monopattino):
        self.codice = #todo codice
        self.dataInizio = datetime.datetime.now().replace(microsecond=0)
        self.cliente = cliente
        self.monopattino = monopattino
        self.ricevuta = Ricevuta()

        self.codiceMezzo = self.monopattino.getCodiceMezzoDisponibile()
        self.monopattino.setDisponibilita(self.codiceMezzo, False)

    # termina una corsa
    def terminaCorsa(self):
        self.dataFine = datetime.datetime.now().replace(microsecond=0)
        self.ricevuta.stilaRicevuta(self.dataInizio, self.dataFine, self.cliente.codice)
        self.monopattino.setDisponibilita(self.codiceMezzo, True)
        self.cliente.portafoglio.prelevaDenaro(self.ricevuta.costoTotale)

        corse = {}
        if os.path.isfile("Dati/Corse.pickle"):
            with open("Dati/Corse.pickle", "rb") as f:
                corse = pickle.load(f)

        corse[self.codice] = self
        with open("Dati/Corse.pickle", "wb") as f:
            pickle.dump(corse, f, pickle.HIGHEST_PROTOCOL)

    # ritorna le corse di tutti i clienti
    def getCorse(self):
        if os.path.isfile("Dati/Corse.pickle"):
            with open("Dati/Corse.pickle", "rb") as f:
                corse = dict(pickle.load(f))
                return corse
        else:
            return None
