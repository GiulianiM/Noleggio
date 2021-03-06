import os
import pickle


class Portafoglio:
    def __init__(self):
        self.saldo = 0.0
        self.codice = ""

    # crea un nuovo portafoglio
    def crea_portafoglio(self, codice_cliente):
        # come codice univoco del portafoglio associo il codice univoco del cliente
        self.codice = codice_cliente

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
            portafogli[self.codice] = self
            with open("Dati/Portafogli.pickle", "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("File non trovato")

    # ritorna il saldo del portafoglio del cliente
    def getSaldo(self):
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k == self.codice:
                    self.saldo = v.saldo
                    return round(v.saldo, 2)
        else:
            print("File non trovato")

    # versa il denaro nel portafoglio del cliente
    def versaDenaro(self, importo):
        self.saldo += importo

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k is self.codice:
                    v.saldo += importo

            with open("Dati/Portafogli.pickle", "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("File non trovato")

    # preleva il denaro dal portafoglio del cliente
    def prelevaDenaro(self, importo):
        self.saldo -= importo

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k is self.codice:
                    v.saldo -= importo

            with open("Dati/Portafogli.pickle", "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("File non trovato")

    # elimina il portafoglio del cliente
    def rimuoviPortafoglio(self):
        if os.path.isfile('Dati/Portafogli.pickle'):
            with open('Dati/Portafogli.pickle', 'rb') as f:
                portafogli = dict(pickle.load(f))
                del portafogli[self.codice]
            with open('Dati/Portafogli.pickle', 'wb') as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
            self.saldo = 0.0
            self.codice = -1
            del self
        else:
            print("File non trovato")

    # ritorna un dizionario con tutti i portafogli di tutti i clienti
    def getPortafogli(self):
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
                return portafogli or None
        else:
            print("File non trovato")
