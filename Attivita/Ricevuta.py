import datetime
import os
import pickle
import uuid

from Servizio.Monopattino import Monopattino


class Ricevuta:

    def __init__(self):
        self.codice = ""
        self.codice_cliente = ""
        self.codice_mezzo = ""
        self.codice_corsa = ""
        self.inizio = datetime.datetime(year=1970, month=1, day=1)
        self.fine = datetime.datetime(year=1970, month=1, day=1)
        self.tempo_utilizzo = 0.0
        self.costo_totale = 0.0

    # crea una nuova ricevuta
    def stila_ricevuta(self, codice_mezzo, codice_corsa, codice_cliente, inizio, fine):
        self.codice = str(uuid.uuid4())[:8]
        self.codice_cliente = codice_cliente
        self.codice_mezzo = codice_mezzo
        self.codice_corsa = codice_corsa
        self.inizio = inizio
        self.fine = fine

        self.tempo_utilizzo = self.get_tempo_utilizzo()
        self.costo_totale = self.get_costo_totale()

        ricevute = {}
        if os.path.isfile("Dati/Ricevute.pickle"):
            with open("Dati/Ricevute.pickle", "rb") as f:
                ricevute = dict(pickle.load(f))
        ricevute[self.codice] = self
        with open("Dati/Ricevute.pickle", "wb") as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)

    # ritorna il costo totale della corsa
    def get_costo_totale(self):
        return round(self.tempo_utilizzo * Monopattino().costo_minuto, 2)

    # ritorna il trempo totale di utilizzo del mezzo
    def get_tempo_utilizzo(self):
        return round(int((self.fine - self.inizio).total_seconds()) / 60, 2)

    # funzione che restituisce un dizionario di tutte le ricevute
    def get_ricevute(self):
        if os.path.isfile("Dati/Ricevute.pickle"):
            with open("Dati/Ricevute.pickle", "rb") as f:
                ricevute = dict(pickle.load(f))
                return ricevute or None
        else:
            print("File Ricevute.pickle non trovato")

    # funzione che stampa a schermo la ricevuta
    def get_ricevuta_to_string(self):
        return "Costo per minuto: " + str(Monopattino().costo_minuto) + "\n" + \
               "Minuti utilizzati: " + str(self.tempo_utilizzo) + "\n" + \
               "Costo totale: " + str(self.costo_totale) + "\n" + \
               "Data inizio: " + str(self.inizio) + "\n" + \
               "Data fine: " + str(self.fine) + "\n"

    # funzione che restituisce la lista di tutte le ricevute di un cliente specifico
    def get_ricevute_cliente(self, codice_cliente):
        if os.path.isfile("Dati/Ricevute.pickle"):
            with open("Dati/Ricevute.pickle", "rb") as f:
                ricevute = dict(pickle.load(f))
            return [ricevuta for ricevuta in ricevute.values() if ricevuta.codice_cliente == codice_cliente]
        else:
            print("File Ricevute.pickle non trovato")
            return None