import os
import pickle
import uuid

from Attivita.Portafoglio import Portafoglio


class Cliente:

    def __init__(self):
        self.portafoglio = None
        self.codice = ""
        self.codice_fiscale = ""
        self.nome = ""
        self.cognome = ""
        self.telefono = ""
        self.password = ""

    # ritorna un cliente a partire dal codice
    def ricerca_cliente_codice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti.get(codice, None)
        else:
            print("File non trovato")

    # ritorna un cliente a partire dal codice fiscale
    def ricerca_cliente_codicefiscale(self, codicefiscale):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti.get(codicefiscale, None)
        else:
            print("File non trovato")

    # crea un cliente, lo inserisce nel dizionario e lo salva su file
    def crea_cliente(self, nome, cognome, telefono, codice_fiscale, password):
        # ricerco omonimi con codice fiscale per evitare duplicazioni
        if self.ricerca_cliente_codicefiscale(codice_fiscale) is None:
            self.nome = nome
            self.cognome = cognome
            self.telefono = telefono
            self.codice_fiscale = codice_fiscale
            self.password = password
            self.codice = uuid.uuid4()
            self.portafoglio = Portafoglio()
            self.portafoglio.crea_portafoglio(self.codice)

            if os.path.isfile("Dati/Clienti.pickle"):
                with open("Dati/Clienti.pickle", "rb") as f:
                    clienti = dict(pickle.load(f))
                clienti[self.codice] = self
                with open("Dati/Clienti.pickle", "wb") as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
                print("Registrazione avvenuta con successo")
            else:
                print("File non trovato")
        else:
            print("Cliente già presente")

    def modifica_cliente(self, codice, nome, cognome, telefono, codice_fiscale, password):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                clienti[codice].nome = nome
                clienti[codice].cognome = cognome
                clienti[codice].telefono = telefono
                clienti[codice].codice_fiscale = codice_fiscale
                clienti[codice].password = password
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            print("Modifica avvenuta con successo")
        else:
            print("File non trovato")

    # elimina un cliente a partire dal codice
    def rimuovi_cliente_codice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                del clienti[codice]
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            self.portafoglio.rimuoviPortafoglio()
            del self
        else:
            print("File non trovato")

    # ritorna un dizionario con tutti i clienti
    def get_clienti(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti or None
        else:
            print("File non trovato")
