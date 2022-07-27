import datetime
import uuid

from PyQt5.QtWidgets import QMessageBox

from Attivita.Ricevuta import Ricevuta
from Servizio.Mezzo import Mezzo


class Corsa:

    def __init__(self, cliente):
        self.cliente = cliente
        self.ricevuta = None
        self.mezzo = None
        self.codice = ""
        self.data_inizio = datetime.datetime(year=1970, month=1, day=1)
        self.data_fine = datetime.datetime(year=1970, month=1, day=1)

    # avvia una nuova corsa
    def avvia_corsa(self, codice_mezzo):
        self.mezzo = Mezzo().ricerca_mezzo_codice(codice_mezzo)
        self.codice = str(uuid.uuid4())[:8]
        self.data_inizio = datetime.datetime.now().replace(microsecond=0)
        self.mezzo.set_disponibilita(codice_mezzo=self.mezzo.codice, disponibile=False)

    # termina una corsa:
    #   - imposta la data di fine
    #   - imposta la disponibilita del mezzo a True
    #   - crea una nuova ricevuta e la stampa a schermo
    def termina_corsa(self):
        self.data_fine = datetime.datetime.now().replace(microsecond=0)
        self.mezzo.set_disponibilita(codice_mezzo=self.mezzo.codice, disponibile=True)
        ricevuta = Ricevuta()
        ricevuta.stila_ricevuta(mezzo=self.mezzo, corsa=self,
                                cliente=self.cliente, inizio=self.data_inizio, fine=self.data_fine)
        self.cliente.portafoglio.addebita_denaro(importo=ricevuta.costo_totale)
        del self
        return ricevuta.get_ricevuta_to_string()
