import datetime
import uuid

from Attivita.Ricevuta import Ricevuta


class Corsa:

    def __init__(self):
        self.ricevuta = None
        self.mezzo = None
        self.codice = ""
        self.data_inizio = datetime.datetime(year=1970, month=1, day=1)
        self.data_fine = datetime.datetime(year=1970, month=1, day=1)

    def inizializza_corsa(self, mezzo):
        self.mezzo = mezzo
        self.codice = uuid.uuid4()[:8]

    # avvia una nuova corsa
    def avvia_corsa(self):
        self.data_inizio = datetime.datetime.now().replace(microsecond=0)

    # termina una corsa
    def termina_corsa(self, cliente):
        self.dataFine = datetime.datetime.now().replace(microsecond=0)
        self.ricevuta = Ricevuta()
        self.ricevuta.stilaRicevuta(codice_mezzo=self.mezzo.codice, codice_corsa=self.codice,
                                    codice_cliente=cliente.codice, inizio=self.data_inizio, fine=self.data_fine)
        del self
