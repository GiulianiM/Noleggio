import os
import pickle
from abc import abstractmethod


class Mezzo:

    def __init__(self):
        self.codice = ""

    @abstractmethod
    def inserisciMezzo(self):
        pass

    @abstractmethod
    def setDisponibilita(self, codiceMezzo, disponibile):
        pass

    @abstractmethod
    def getCodiceMezzoDisponibile(self):
        pass

    # ritorna tutti i mezzi
    def getMezzi(self):
        if os.path.isfile('Dati/Mezzi.pickle'):
            with open('Dati/Mezzi.pickle', 'rb') as f:
                mezzi = dict(pickle.load(f))
                return mezzi
        else:
            return None

    # elimina un mezzo
    def rimuoviMezzo(self):
        self.codice = -1
