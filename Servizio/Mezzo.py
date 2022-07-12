import os
import pickle
import uuid


class Mezzo:

    def __init__(self):
        self.codice = uuid.uuid4()[:8]
        self.disponibile = True

    def inserisci_mezzo(self):
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                mezzi = pickle.load(f)
            mezzi[self.codice] = self
            with open("Dati/Clienti.pickle", "wb") as f:
                pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)
        else:
            print('File non trovato')

    def set_disponibilita(self, codice_mezzo, disponibile):
        if os.path.isfile("Dati/Mezzi.pickle"):
            with open("Dati/Mezzi.pickle", "rb") as f:
                mezzi = pickle.load(f)
            mezzi[codice_mezzo].disponibile = disponibile
            with open("Dati/Mezzi.pickle", "wb") as f:
                pickle.dump(mezzi, f, pickle.HIGHEST_PROTOCOL)
        else:
            print('File non trovato')

    def visualizza_mezzi_disponibili(self):
        mezzi = Mezzo.get_mezzi(self)
        mezzi_disponibili = []
        for mezzo in mezzi:
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
