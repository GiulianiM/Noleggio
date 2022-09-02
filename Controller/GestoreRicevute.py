import os
import pickle

from Attivita.Ricevuta import Ricevuta
from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathFiles import PATH_RICEVUTE


class GestoreRicevute:
    def __init__(self):
        self.gestore_clienti = GestoreClienti()
        self.ricevuta = None

    # ritorna un dizionario di tutte le ricevute del cliente corrente
    # return: Dict of Ricevuta
    def get_ricevute_cliente(self):
        if os.path.isfile(PATH_RICEVUTE):
            with open(PATH_RICEVUTE, "rb") as f:
                ricevute = dict(pickle.load(f))
            return [ricevuta for ricevuta in ricevute.values() if
                    ricevuta.id_cliente == self.gestore_clienti.cliente_corrente.id]
        else:
            return None

    # ritorna un dizionario con tutte le ricevute
    # return: Dict of Ricevuta
    def get_ricevute(self):
        ricevute = {}
        if os.path.isfile(PATH_RICEVUTE):
            with open(PATH_RICEVUTE, "rb") as f:
                ricevute = dict(pickle.load(f))
        if len(ricevute) > 0:
            return ricevute
        else:
            return None

            # provvede a creare una ricevuta

    # return: String
    def stila_ricevuta(self, id_monopattino, tempo_totale, costo_totale, id_cliente, saldo_portafoglio):
        self.ricevuta = Ricevuta()
        return self.ricevuta.crea(
            id_monopattino=id_monopattino,
            costo_totale=costo_totale,
            tempo_totale=tempo_totale,
            id_cliente=id_cliente,
            saldo_portafoglio=saldo_portafoglio
        )
