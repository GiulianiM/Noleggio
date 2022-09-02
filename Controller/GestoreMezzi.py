import os
import pickle

from Servizio.Monopattino import Monopattino
from Utils.Const.PathFiles import PATH_MONOPATTINI


class GestoreMezzi:
    def __init__(self):
        self.monopattino = Monopattino()

    # metodo setter
    def set_monopattino(self, monopattino):
        self.monopattino = monopattino

    # metodo setter
    # imposta la disponibilita di un monopattino
    def set_disponibilita_monopattino(self, disponibilita):
        self.monopattino.set_disponibilita(disponibilita)

    # ritorna una lista di monopattini con disponibilita True
    # return: List
    def get_mezzi_disponibili(self):
        return self.monopattino.get_disponibili()

    # ritorna un dizionario di tutti i monopattini
    # return: Dict of Monopattino
    def get_all_mezzi(self):
        return self.monopattino.get_monopattini()

    # crea un nuovo monopattino
    def aggiungi_monopattino(self):
        self.monopattino.crea()

    # elimina un monopattino tramite id_monopattino
    # return: Boolean
    def elimina_monopattino(self, id_monopattino):
        temp_monopattino = self.ricerca_monopattino_id(id_monopattino)
        if isinstance(temp_monopattino, Monopattino):
            temp_monopattino.rimuovi()
            return True
        else:
            return False

    # ricerca del monopattino tramite id_monopattino
    # return: Monopattino
    def ricerca_monopattino_id(self, id_monopattino):
        monopattini = {}
        if os.path.isfile(PATH_MONOPATTINI):
            with open(PATH_MONOPATTINI, 'rb') as f:
                monopattini = dict(pickle.load(f))

        if len(monopattini) > 0:
            for monopattino in monopattini.values():
                if monopattino.id == id_monopattino:
                    return monopattino
            return None
        else:
            return None

    # ritorna la disponibilità del monopattino
    # return: Boolean
    def is_disponibile(self):
        return self.monopattino.get_disponibilita()
