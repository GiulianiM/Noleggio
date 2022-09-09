import os
import pathlib
import pickle
import uuid

from Servizio.Monopattino import Monopattino
from Utils.Const.PathFiles import PATH_RICEVUTE


class Ricevuta:

    def __init__(self):
        self.id = ""
        self.id_monopattino = ""
        self.costo_totale = 0.0
        self.tempo_totale = 0.0
        self.saldo_portafoglio = ""
        self.id_cliente = ""

    # 1. crea una nuova ricevuta
    # 2. salva su file
    # return: self (questa ricevuta)
    def crea(self, id_monopattino, costo_totale, tempo_totale, saldo_portafoglio, id_cliente):
        self.id = str(uuid.uuid4())[:8]  # genero un codice identificativo univoco da 8 cifre
        self.id_monopattino = id_monopattino
        self.costo_totale = costo_totale
        self.tempo_totale = tempo_totale
        self.saldo_portafoglio = saldo_portafoglio
        self.id_cliente = id_cliente

        ricevute = {}
        if os.path.isfile(PATH_RICEVUTE):
            with open(PATH_RICEVUTE, "rb") as f:
                ricevute = dict(pickle.load(f))
        ricevute[self.id] = self
        if not os.path.isdir(pathlib.Path(PATH_RICEVUTE).parent):
            os.mkdir(pathlib.Path(PATH_RICEVUTE).parent)
        with open(PATH_RICEVUTE, "wb") as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)

        return self

    # to_string()
    # return: String
    def __str__(self):
        # se sono passati piu di 60 secondi
        if self.tempo_totale >= 60:
            return "Id monopattino: " + self.id_monopattino + "\n" + \
                   "Costo per minuto: " + str(Monopattino().costo_minuto) + " €/min\n" + \
                   "Minuti utilizzati: " + str(format(self.tempo_totale / 60, '.1f')) + "\n" + \
                   "Costo totale: " + str(self.costo_totale) + " €\n"
        # se sono passati meno di 60 secondi
        else:
            return "Id monopattino: " + self.id_monopattino + "\n" + \
                   "Costo per minuto: " + str(Monopattino().costo_minuto) + " €/min\n" + \
                   "Secondi utilizzati: " + str(self.tempo_totale) + "\n" + \
                   "Costo totale: " + str(self.costo_totale) + " €\n"
