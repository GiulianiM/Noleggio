import os
import pickle

from Attivita.Portafoglio import Portafoglio


class Cliente:

    def __init__(self):
        self.portafoglio = None
        self.codice = -1
        self.codiceFiscale = ""
        self.nome = ""
        self.cognome = ""
        self.telefono = ""

    # crea un cliente
    def creaCliente(self, nome, cognome, telefono, codiceFiscale):
        self.portafoglio = Portafoglio()
        self.portafoglio.creaPortafoglio(self.codice)

        clienti = {}
        if os.path.isfile("Dati/Clienti.pickle"):
            # rb significa lettura binaria
            with open("Dati/Clienti.pickle", "rb") as f:
                clienti = pickle.load(f)

        # inseirisco l'istanza all'interno del dizionario
        clienti[self.codice] = self

        # wb significa scrittura binaria
        with open("Dati/Clienti.pickle", "wb") as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    # elimina un cliente a partire dal codice
    def rimuoviCliente(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                del clienti[self.codice]
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        self.portafoglio.rimuoviPortafoglio()
        del self

    # ritorna un cliente a partire dal codice
    def ricercaClienteCodice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti.get(codice, None)
        else:
            return None

    # ritorna un dizionario con tutti i clienti
    def getClienti(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti
        else:
            return None
