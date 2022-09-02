import datetime
import uuid

from Servizio.Monopattino import Monopattino


class Corsa:

    def __init__(self):
        self.id = ""
        self.data_inizio = datetime.datetime(year=1970, month=1, day=1)
        self.data_fine = datetime.datetime(year=1970, month=1, day=1)

    # avvia una nuova corsa
    def avvia(self):
        self.id = str(uuid.uuid4())[:8]  # genero un id_cliente univoco da 8 cifre
        self.data_inizio = datetime.datetime.now().replace(microsecond=0)

    # termina una corsa
    def termina(self):
        self.data_fine = datetime.datetime.now().replace(microsecond=0)

    # calcolo del costo
    # return: Float
    def costo_totale(self):
        return round(self.tempo_utilizzo() / 60 * Monopattino().costo_minuto, 2)

    # calcolo del tempo_utilizzo di utilizzo
    # return: Float
    def tempo_utilizzo(self):
        return (self.data_fine - self.data_inizio).total_seconds()
