import os
import pickle

from Utils.Const.PathFiles import PATH_PORTAFOGLI, PATH_CURRENT_WALLET


class Portafoglio:
    def __init__(self):
        self.saldo = 0.00
        self.id = ""

    # 1. istanzia un nuovo portafoglio
    # 2. salva su file
    # return: self (questo portafoglio)
    def crea(self, codice_cliente):
        # come id_cliente univoco del portafoglio associo il id_cliente univoco del cliente
        self.id = codice_cliente

        portafogli = {}
        if os.path.isfile(PATH_PORTAFOGLI):
            with open(PATH_PORTAFOGLI, "rb") as f:
                portafogli = dict(pickle.load(f))
        portafogli[self.id] = self
        with open(PATH_PORTAFOGLI, "wb") as f:
            pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

        with open(PATH_CURRENT_WALLET, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        return self

    # ritorna il saldo attuale
    # return: String
    def get_saldo(self):
        return format(self.saldo, '0.2f')

    # 1. aggiorna il saldo addizionando l'importo
    # 2. salva su file
    # return: String
    def versa(self, importo):
        self.saldo += importo

        if os.path.isfile(PATH_PORTAFOGLI):
            with open(PATH_PORTAFOGLI, "rb") as f:
                portafogli = dict(pickle.load(f))
                for k, v in portafogli.items():
                    if k == self.id:
                        v.saldo += importo
            with open(PATH_PORTAFOGLI, "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

        if os.path.isfile(PATH_CURRENT_WALLET):
            with open(PATH_CURRENT_WALLET, "rb") as f:
                portafoglio_corrente = pickle.load(f)
                portafoglio_corrente.saldo = self.saldo
            with open(PATH_CURRENT_WALLET, "wb") as f:
                pickle.dump(portafoglio_corrente, f, pickle.HIGHEST_PROTOCOL)

        return self.get_saldo()

    # 1. aggiorna il saldo sottraendo l'importo
    # 2. salva su file
    # return: String
    def preleva(self, importo):
        self.saldo -= importo

        if os.path.isfile(PATH_PORTAFOGLI):
            with open(PATH_PORTAFOGLI, "rb") as f:
                portafogli = dict(pickle.load(f))
                for k, v in portafogli.items():
                    if k == self.id:
                        v.saldo -= importo
            with open(PATH_PORTAFOGLI, "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

        if os.path.isfile(PATH_CURRENT_WALLET):
            with open(PATH_CURRENT_WALLET, "rb") as f:
                portafoglio_corrente = pickle.load(f)
                portafoglio_corrente.saldo -= importo
            with open(PATH_CURRENT_WALLET, "wb") as f:
                pickle.dump(portafoglio_corrente, f, pickle.HIGHEST_PROTOCOL)

        return self.get_saldo()

    # 1. elimina l'istanza
    # 2. salva su file
    def rimuovi(self):
        if os.path.isfile(PATH_PORTAFOGLI):
            with open(PATH_PORTAFOGLI, 'rb') as f:
                portafogli = dict(pickle.load(f))
                del portafogli[self.id]
            with open(PATH_PORTAFOGLI, 'wb') as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
            del self

    # ritorna un dizionario con tutti i portafogli di tutti i clienti
    # return: Dict of Portafogli
    def get_portafogli(self):
        if os.path.isfile(PATH_PORTAFOGLI):
            with open(PATH_PORTAFOGLI, "rb") as f:
                portafogli = dict(pickle.load(f))
                return portafogli or None

    # to_string
    # return: String
    def __str__(self) -> str:
        return "Id: " + self.id + "\n" + \
               "Saldo: " + self.get_saldo()
