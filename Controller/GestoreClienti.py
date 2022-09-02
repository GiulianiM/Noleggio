import os
import pickle

from Attivita.Cliente import Cliente
from Attivita.Portafoglio import Portafoglio
from Utils.Const.PathFiles import PATH_CLIENTI, PATH_CURRENT_USER, PATH_PORTAFOGLI, PATH_CURRENT_WALLET


class GestoreClienti:
    # Si possono verificare due casi di chiamata a questa classe:
    # 1. L'amministratore vuole modificare un cliente:
    #       istanzia questa classe passando il codice del cliente
    # 2. Un cliente si è autenticato al sistema:
    #       isntanzia questa classe e vengono prelevati:
    #           - dati del cliente
    #           - deati delm portafoglio
    def __init__(self, *args):
        if len(args) > 0:
            for i in args:
                self.cliente_corrente = self.ricerca_cliente_id(i)
        else:
            self.cliente_corrente = self.get_cliente_corrente()
            self.portafoglio_corrente = self.get_portafoglio_corrente()

    # ritorna il cliente attualmente autenticato al sistema
    # return: Cliente
    def get_cliente_corrente(self):
        if os.path.isfile(PATH_CURRENT_USER):
            with open(PATH_CURRENT_USER, "rb") as f:
                return pickle.load(f)

    # ritorna il portafoglio del cliente attualmente autenticato al sistema
    # return: Portafoglio
    def get_portafoglio_corrente(self):
        if os.path.isfile(PATH_CURRENT_WALLET):
            with open(PATH_CURRENT_WALLET, "rb") as f:
                return pickle.load(f)

    # ricerca del portafoglio tramite id_portafoglio
    # return: Portafoglio
    def ricerca_portafoglio_id(self, id_portafoglio):
        portafogli = {}
        if os.path.isfile(PATH_PORTAFOGLI):
            with open(PATH_PORTAFOGLI, 'rb') as f:
                portafogli = dict(pickle.load(f))
        if len(portafogli) > 0:
            for portafoglio in portafogli.values():
                if portafoglio.id == id_portafoglio:
                    return portafoglio
        else:
            return None

    # ritorna un cliente specifico tramite id_cliente
    # return: Cliente
    def ricerca_cliente_id(self, id_cliente):
        clienti = {}
        if os.path.isfile(PATH_CLIENTI):
            with open(PATH_CLIENTI, 'rb') as f:
                clienti = dict(pickle.load(f))

        if len(clienti) > 0:
            for cliente in clienti.values():
                if cliente.id == id_cliente:
                    return cliente
        else:
            return None

    # ritorna un cliente specifico tramite codice fiscale
    # return: Cliente
    def ricerca_cliente_cf(self, cf):
        clienti = {}
        if os.path.isfile(PATH_CLIENTI):
            with open(PATH_CLIENTI, 'rb') as f:
                clienti = dict(pickle.load(f))

        if len(clienti) > 0:
            for cliente in clienti.values():
                if cliente.cf == cf:
                    return cliente
            else:
                return None
        else:
            return None

    # processo di registrazione del cliente al sistema
    # il sistema crea un'istanza di Cliente
    # il sistema crea un istanza di Portafoglio
    # return: Cliente, Portafoglio
    def registra_cliente(self, nome, cognome, cf, telefono, password):
        temp_cliente = self.ricerca_cliente_cf(cf)
        if not isinstance(temp_cliente, Cliente):
            nuovo_cliente = Cliente().crea(
                nome=nome,
                cognome=cognome,
                cf=cf,
                telefono=telefono,
                password=password
            )
            nuovo_portafoglio = Portafoglio().crea(nuovo_cliente.id)
            return nuovo_cliente, nuovo_portafoglio
        else:
            return None, None

    # 1. controllo se il campo codice fiscale è NON vuoto, se così fosse:
    #   a) controllo se NON esiste nessuno con quel codice fiscale
    # 2. controllo se anche gli altri parametri sono NON vuoti
    # 3.
    # return: Boolean
    def modifica_cliente(self, nome, cognome, cf, telefono, password):
        if cf is not None:
            self.cliente_corrente.cf = cf
            if self.ricerca_cliente_cf(cf) is not None:
                return False
        if nome is not None:
            self.cliente_corrente.nome = nome
        if cognome is not None:
            self.cliente_corrente.cognome = cognome
        if telefono is not None:
            self.cliente_corrente.telefono = telefono
        if password is not None:
            self.cliente_corrente.password = password

        self.cliente_corrente.modifica(
            nuovo_nome=self.cliente_corrente.nome,
            nuovo_cognome=self.cliente_corrente.cognome,
            nuovo_cf=self.cliente_corrente.cf,
            nuovo_telefono=self.cliente_corrente.telefono,
            nuova_password=self.cliente_corrente.password
        )
        return True

    # return: Dict of Clienti
    def visualizza_clienti(self):
        return self.cliente_corrente.get_clienti()

    # 1. ricerca il cliente
    # 2. se esiste provvede a elimiarlo
    # return: Boolean
    def rimuovi_cliente(self, id_cliente):
        temp_cliente = self.ricerca_cliente_id(id_cliente)
        if isinstance(temp_cliente, Cliente):  # controllo se il cliente è esistente o meno
            temp_cliente.rimuovi()
            return True
        else:
            return False

    # ritorna il saldo attuale del cliente
    # return: String
    def visualizza_portafoglio(self):
        return self.portafoglio_corrente.get_saldo()

    # versa il denaro
    # return: String
    def versa_denaro(self, importo):
        return self.portafoglio_corrente.versa(importo)

    # preleva il denaro
    # return: Stirng
    def preleva_denaro(self, importo):
        return self.portafoglio_corrente.preleva(importo)
