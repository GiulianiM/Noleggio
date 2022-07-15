import os
import pickle
import uuid

from Attivita.Portafoglio import Portafoglio


class Cliente:

    def __init__(self):
        self.portafoglio = None
        self.codice = ""
        self.codicefiscale = ""
        self.nome = ""
        self.cognome = ""
        self.telefono = ""
        self.password = ""

    # ritorna un cliente a partire dal codice
    def ricerca_cliente_codice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.codice == codice:
                        return cliente
                return None

    # ritorna un cliente a partire dal codice fiscale
    def ricerca_cliente_codicefiscale(self, codicefiscale):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.codicefiscale == codicefiscale:
                        return cliente
                return None

    # crea un cliente, lo inserisce nel dizionario e lo salva su file
    def crea_cliente(self, nome, cognome, telefono, codicefiscale, password):
        # ricerco omonimi con codice fiscale per evitare duplicazioni
        if self.ricerca_cliente_codicefiscale(codicefiscale) is None:
            self.nome = nome
            self.cognome = cognome
            self.telefono = telefono
            self.codicefiscale = codicefiscale
            self.codice = str(uuid.uuid4())[:8]
            self.portafoglio = Portafoglio()
            self.portafoglio.crea_portafoglio(self.codice)
            self.password = password

            clienti = {}
            if os.path.isfile("Dati/Clienti.pickle"):
                with open("Dati/Clienti.pickle", "rb") as f:
                    clienti = dict(pickle.load(f))
            clienti[self.codice] = self
            with open("Dati/Clienti.pickle", "wb") as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            return self, "Registrazione avvenuta con successo"
        else:
            return None, "Utente già presente con lo stesso codice fiscale"

    #def modifica_cliente(self, codice, nome, cognome, telefono, codice_fiscale):
    def modifica_cliente(self, nuova_pwd, codice_cliente):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                #clienti[codice_cliente].nome = nome
                clienti[codice_cliente].password = nuova_pwd
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            return "Modifica avvenuta con successo"
        else:
            return "Modifica non avvenuta"

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
