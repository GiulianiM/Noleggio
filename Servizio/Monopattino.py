import os
import pathlib
import pickle
import uuid

from Utils.Const.PathFiles import PATH_MONOPATTINI


class Monopattino:

    def __init__(self):
        self.id = ""
        self.costo_minuto = 0.20
        self.disponibilita = True

    # 1. crea un nuovo monopattino
    # 2. salva sul file
    # return: self (questo monopattino)
    def crea(self):
        self.id = str(uuid.uuid4())[:8]  # genero un codice univoco identificativo da 8 cifre
        self.disponibilita = True
        monopattini = {}
        if os.path.isfile(PATH_MONOPATTINI):
            with open(PATH_MONOPATTINI, "rb") as f:
                monopattini = pickle.load(f)

        monopattini[self.id] = self
        if not os.path.isdir(pathlib.Path(PATH_MONOPATTINI).parent):
            os.mkdir(pathlib.Path(PATH_MONOPATTINI).parent)
        with open(PATH_MONOPATTINI, "wb") as f:
            pickle.dump(monopattini, f, pickle.HIGHEST_PROTOCOL)

        return self

    # Metodo setter
    # 1. setta la disponibilità
    # 2. salva su file
    def set_disponibilita(self, disponibilita):
        self.disponibilita = disponibilita

        monopattini = {}
        if os.path.isfile(PATH_MONOPATTINI):
            with open(PATH_MONOPATTINI, 'rb') as f:
                monopattini = dict(pickle.load(f))

        monopattini[self.id].disponibilita = disponibilita
        with open(PATH_MONOPATTINI, "wb") as f:
            pickle.dump(monopattini, f, pickle.HIGHEST_PROTOCOL)

    # metodo getter
    # ritorna lo stato attuale del monopattino relativo alla disponibilità
    # return: Boolean
    def get_disponibilita(self):
        return self.disponibilita

    # 1. elimina il monopattino
    # 2. salva su file
    def rimuovi(self):
        if os.path.isfile(PATH_MONOPATTINI):
            with open(PATH_MONOPATTINI, "rb") as f:
                monopattini = pickle.load(f)
                del monopattini[self.id]
            with open(PATH_MONOPATTINI, "wb") as f:
                pickle.dump(monopattini, f, pickle.HIGHEST_PROTOCOL)
            del self

    # ritorna un dizionario con tutti i monopattini
    # return: Dict of Monopattino
    def get_monopattini(self):
        monopattini = {}
        if os.path.isfile(PATH_MONOPATTINI):
            with open(PATH_MONOPATTINI, 'rb') as f:
                monopattini = dict(pickle.load(f))
        return monopattini

    # ritorna una lista di monopattini con disponibilità True
    # return: List
    def get_disponibili(self):
        disponibili = []
        if os.path.isfile(PATH_MONOPATTINI):
            with open(PATH_MONOPATTINI, 'rb') as f:
                monopattini = dict(pickle.load(f))
                for monopattino in monopattini.values():
                    if monopattino.disponibilita:
                        disponibili.append(monopattino)
        return disponibili

    # to_string()
    # return: String
    def __str__(self):
        if self.disponibilita:
            return "Id monopattino: " + self.id + "\n" + \
               "Costo al minuto: " + str(self.costo_minuto) + "\n" + \
               "Disponibilita: Disponibile" + "\n"
        else:
            return "Id monopattino: " + self.id + "\n" + \
               "Costo al minuto: " + str(self.costo_minuto) + "\n" + \
               "Disponibilita: Non disponibile" + "\n"
