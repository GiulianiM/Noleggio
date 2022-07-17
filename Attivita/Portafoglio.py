import os
import pickle


class Portafoglio:
    def __init__(self):
        self.saldo = 0.00
        self.codice = ""

    # crea un nuovo portafoglio
    def crea_portafoglio(self, codice_cliente):
        # come codice univoco del portafoglio associo il codice univoco del cliente
        self.codice = codice_cliente

        portafogli = {}
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
        portafogli[self.codice] = self
        with open("Dati/Portafogli.pickle", "wb") as f:
            pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)

    # ritorna il saldo del portafoglio del cliente
    def get_saldo(self):
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k == self.codice:
                    self.saldo = v.saldo
                    return format(v.saldo, '0.2f')
        else:
            return None

    # versa il denaro nel portafoglio del cliente
    def versa_denaro(self, importo):
        print(format(self.saldo, '0.2f'))
        self.saldo += importo

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k == self.codice:
                    v.saldo += importo

            with open("Dati/Portafogli.pickle", "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
            return format(self.saldo, '0.2f') , "Importo versato correttamente"

    # preleva il denaro dal portafoglio del cliente
    def preleva_denaro(self, importo):
        self.saldo -= importo

        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))

            for k, v in portafogli.items():
                if k == self.codice:
                    v.saldo -= importo

            with open("Dati/Portafogli.pickle", "wb") as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("File non trovato")

    # elimina il portafoglio del cliente
    def rimuovi_portafoglio(self):
        if os.path.isfile('Dati/Portafogli.pickle'):
            with open('Dati/Portafogli.pickle', 'rb') as f:
                portafogli = dict(pickle.load(f))
                del portafogli[self.codice]
            with open('Dati/Portafogli.pickle', 'wb') as f:
                pickle.dump(portafogli, f, pickle.HIGHEST_PROTOCOL)
            self.saldo = 0.00
            self.codice = -1
            del self
        else:
            print("File non trovato")

    # ritorna un dizionario con tutti i portafogli di tutti i clienti
    def get_portafogli(self):
        if os.path.isfile("Dati/Portafogli.pickle"):
            with open("Dati/Portafogli.pickle", "rb") as f:
                portafogli = dict(pickle.load(f))
                return portafogli or None
        else:
            print("File non trovato")
