import pickle
import time

from Attivita.Cliente import Cliente
from Attivita.Portafoglio import Portafoglio
from Attivita.Ricevuta import Ricevuta
from Servizio.Mezzo import Mezzo
import schedule


class Backup:

    def __init__(self):
        self.portafogli = {}
        self.ricevute = {}
        self.clienti = {}
        self.mezzi = {}

    def esegui_backup(self):
        self.clienti = Cliente().get_clienti()
        self.ricevute = Ricevuta().get_ricevute()
        self.portafogli = Portafoglio().get_portafogli()
        self.mezzi = Mezzo().get_mezzi()

        with open("Dati/Backup.pickle", "wb") as f:
            for cliente in self.clienti:
                pickle.dump(cliente, f)
            for ricevuta in self.ricevute:
                pickle.dump(ricevuta, f)
            for portafoglio in self.portafogli:
                pickle.dump(portafoglio, f)
            for mezzo in self.mezzi:
                pickle.dump(mezzo, f)

    def backup_daily(self):
        schedule.every().day.at("00:00").do(self.esegui_backup)
        while True:
            schedule.run_pending()
            time.sleep(1)
