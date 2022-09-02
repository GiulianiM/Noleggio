import pickle
import time

import schedule

from Controller.GestoreClienti import GestoreClienti
from Controller.GestoreMezzi import GestoreMezzi
from Controller.GestoreRicevute import GestoreRicevute
from Utils.Const.PathFiles import PATH_BACKUP


class Backup:

    def __init__(self):
        self.gestore_clienti = GestoreClienti()
        self.gestore_ricevute = GestoreRicevute()
        self.gestore_mezzi = GestoreMezzi()
        self.portafogli = {}
        self.ricevute = {}
        self.clienti = {}
        self.monopattini = {}

    def esegui_backup(self):
        self.clienti = self.gestore_clienti.cliente_corrente.get_clienti()
        self.ricevute = self.gestore_ricevute.get_ricevute()
        self.portafogli = self.gestore_clienti.portafoglio_corrente.get_portafogli()
        self.monopattini = self.gestore_mezzi.get_all_mezzi()

        with open(PATH_BACKUP, "wb") as f:
            for cliente in self.clienti:
                pickle.dump(cliente, f)
            for ricevuta in self.ricevute:
                pickle.dump(ricevuta, f)
            for portafoglio in self.portafogli:
                pickle.dump(portafoglio, f)
            for mezzo in self.monopattini:
                pickle.dump(mezzo, f)

    def backup_daily(self):
        schedule.every().day.at("00:00").do(self.esegui_backup)
        while True:
            schedule.run_pending()
            time.sleep(1)
