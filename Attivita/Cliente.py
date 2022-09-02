import os
import pickle
import uuid

from Utils.Const.PathFiles import PATH_CLIENTI, PATH_CURRENT_USER


class Cliente:

    def __init__(self):
        self.id = ""
        self.cf = ""
        self.nome = ""
        self.cognome = ""
        self.telefono = ""
        self.password = ""

    # 1. istanzia un nuovo utente
    # 2. salva l'istanza su file
    # return: self (questo cliente)
    def crea(self, nome, cognome, telefono, cf, password):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.cf = cf
        self.password = password
        self.id = str(uuid.uuid4())[:8]  # genero un id_cliente da 8 caratteri alfanumerici

        clienti = {}
        if os.path.isfile(PATH_CLIENTI):
            with open(PATH_CLIENTI, "rb") as f:
                clienti = dict(pickle.load(f))
        clienti[self.id] = self
        with open(PATH_CLIENTI, "wb") as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

        # salvo su file i dati l'utente loggato
        with open(PATH_CURRENT_USER, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        return self

    # 1. modifica il profilo con i valori passati come parametri
    # 2. salva su file
    def modifica(self, nuovo_nome, nuovo_cognome, nuovo_cf, nuovo_telefono, nuova_password):
        self.nome = nuovo_nome
        self.cognome = nuovo_cognome
        self.cf = nuovo_cf
        self.telefono = nuovo_telefono
        self.password = nuova_password

        if os.path.isfile(PATH_CLIENTI):
            with open(PATH_CLIENTI, 'rb') as f:
                clienti = dict(pickle.load(f))
                clienti[self.id].nome = nuovo_nome
                clienti[self.id].cognome = nuovo_cognome
                clienti[self.id].cf = nuovo_cf
                clienti[self.id].telefono = nuovo_telefono
                clienti[self.id].password = nuova_password
        with open(PATH_CLIENTI, 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

        if os.path.isfile(PATH_CURRENT_USER):
            with open(PATH_CURRENT_USER, "rb") as f:
                portafoglio_corrente = pickle.load(f)
                portafoglio_corrente.nome = nuovo_nome
                portafoglio_corrente.cognome = nuovo_cognome
                portafoglio_corrente.cf = nuovo_cf
                portafoglio_corrente.telefono = nuovo_telefono
                portafoglio_corrente.password = nuova_password
        with open(PATH_CURRENT_USER, "wb") as f:
            pickle.dump(portafoglio_corrente, f, pickle.HIGHEST_PROTOCOL)

    # 1. rimuove l'istanza del cliente a partire dal id_cliente
    # 2. salva su file
    # return: Boolean
    def rimuovi(self):
        if os.path.isfile(PATH_CLIENTI):
            with open(PATH_CLIENTI, 'rb') as f:
                clienti = dict(pickle.load(f))
                del clienti[self.id]
            with open(PATH_CLIENTI, 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            del self

    # preleva tutti i clienti registrati al sistema
    # return: Dict of Cliente
    def get_clienti(self):
        if os.path.isfile(PATH_CLIENTI):
            with open(PATH_CLIENTI, 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti or None

    # to_string()
    # return: String
    def __str__(self):
        return "Codice: " + self.id + "\n" + \
               "Nome: " + self.nome + "\n" + \
               "Cognome: " + self.cognome + "\n" + \
               "Telefono: " + self.telefono + "\n" + \
               "Codice fiscale: " + self.cf + "\n" + \
               "Password: " + self.password + "\n"
