import os
import pickle


class Portafoglio:
    def __init__(self):
        self.saldo = 0.0
        self.codice = -1

    # crea un nuovo portafoglio
    def creaPortafoglio(self, codiceCliente):
        self.codice = codiceCliente

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
        else:
            portafogli = {}

        portafogli[self.codice] = self

        with open("Dati/Portafogli.pickle", "wb") as f:
            pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

    # ritorna il saldo del portafoglio di un cliente tramite codice
    def getSaldo(self):
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k == self.codice:
                    self.saldo = v.saldo
                    return round(v.saldo, 2)

    # versa il denaro nel portafoglio del cliente
    def versaDenaro(self, importo):
        self.saldo += importo

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k == self.codice:
                    v.saldo += importo

            with open("Dati/Portafogli.pickle", "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

    # preleva il denaro dal portafoglio del cliente
    def prelevaDenaro(self, importo):
        self.saldo -= importo

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
        else:
            portafogli = {}

        for k, v in portafogli.items():
            if k == self.codice:
                v.saldo -= importo

        with open("Dati/Portafogli.pickle", "wb") as f:
            pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

    # elimina il portafoglio del cliente
    def rimuoviPortafoglio(self):
        if os.path.isfile('Dati/Portafogli.pickle'):
            with open('Dati/Portafogli.pickle', 'rb') as f:
                portafogli = dict(pickle.load(f))
                del portafogli[self.codice]
            with open('Dati/Portafogli.pickle', 'wb') as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
        self.saldo = -1
        self.codice = -1
        del self

    # ritorna un dizionario con tutti i portafogli di tutti i clienti
    def getPortafogli(self):
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
                return portafogli
        else:
            return None
