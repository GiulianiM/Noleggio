import os
import pickle
import uuid


class Mezzo:

    def __init__(self):
        self.codice = str(uuid.uuid4())[:8]
        self.disponibile = True
        self.MINIMO_MINUTI = 5

    def inserisci_mezzo(self):
        mezzi = {}
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                mezzi = pickle.load(f)
        mezzi[self.codice] = self
        with open("Dati/Mezzi.pickle", "wb") as f:
            pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)

    def set_disponibilita(self, codice_mezzo, disponibile):
        mezzi = self.get_mezzi()
        mezzi[codice_mezzo].disponibile = disponibile
        with open("Dati/Mezzi.pickle", "wb") as f:
            pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)


    def ricerca_mezzo_codice(self, codice_mezzo):
        mezzi = self.get_mezzi()
        for mezzo in mezzi.values():
            if mezzo.codice == codice_mezzo:
                return mezzo

    def get_mezzi_disponibili(self):
        mezzi = self.get_mezzi()
        mezzi_disponibili = []
        for mezzo in mezzi.values():
            if mezzo.disponibile:
                mezzi_disponibili.append(mezzo)
        return mezzi_disponibili

    # ritorna tutti i mezzi
    def get_mezzi(self):
        if os.path.isfile('Dati/Mezzi.pickle'):
            with open('Dati/Mezzi.pickle', 'rb') as f:
                mezzi = dict(pickle.load(f))
                return mezzi
        else:
            return None

    # elimina un mezzo
    def rimuovi_mezzo(self, codice_mezzo):
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                mezzi = pickle.load(f)
            del mezzi[codice_mezzo]
            with open("Dati/Mezzi.pickle", "wb") as f:
                pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)
            del self
        else:
            print('File non trovato')