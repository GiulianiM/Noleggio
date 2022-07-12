import pickle

from Attivita.Cliente import Cliente
from Attivita.Corsa import Corsa
from Attivita.Portafoglio import Portafoglio
from Attivita.Ricevuta import Ricevuta
from Servizio.Mezzo import Mezzo


class Backup:

    def __init__(self):
        self.portafogli = {}
        self.ricevute = {}
        self.corse = {}
        self.clienti = {}
        self.mezzi = {}

    def eseguiBackup(self):
        self.clienti = Cliente().getClienti()
        self.corse = Corsa().getCorse()
        self.ricevute = Ricevuta().getRicevute()
        self.portafogli = Portafoglio().getPortafogli()
        self.mezzi = Mezzo().getMezzi()

        with open("Dati/Backup.pickle", "wb") as f:
            for cliente in self.clienti:
                pickle.dump(cliente, f)
            for corsa in self.corse:
                pickle.dump(corsa, f)
            for ricevuta in self.ricevute:
                pickle.dump(ricevuta, f)
            for portafoglio in self.portafogli:
                pickle.dump(portafoglio, f)
