import unittest
import os
import Utils.Const.PathFiles as PathFiles

from Controller.GestoreClienti import GestoreClienti
from Controller.GestoreMezzi import GestoreMezzi
from Controller.GestoreRicevute import GestoreRicevute
from Controller.GestoreStatistiche import GestoreStatistiche


class Test(unittest.TestCase):

    def test_registra_cliente(self):
        self.gestore_clienti = GestoreClienti()
        if os.path.exists(PathFiles.PATH_CLIENTI):
            os.remove(PathFiles.PATH_CLIENTI)
        cliente, portafoglio = self.gestore_clienti.registra_cliente("Dario", "Pozzobon", "POZDAR99A01H501R",
                                                                     "3333333333", "password")
        self.assertEqual(cliente.cf, "POZDAR99A01H501R")
        self.assertEqual(portafoglio.saldo, 0)

    def test_creazione_mezzo(self):
        self.gestore_mezzi = GestoreMezzi()
        if os.path.exists(PathFiles.PATH_MONOPATTINI):
            os.remove(PathFiles.PATH_MONOPATTINI)
        for i in range(5):
            self.gestore_mezzi.aggiungi_monopattino()
        self.assertEqual(len(self.gestore_mezzi.get_all_mezzi()), 5)
        self.assertEqual(all(value.disponibilita is True for value in self.gestore_mezzi.get_all_mezzi().values()), True)

    def test_creazione_ricevuta(self):
        self.gestore_ricevute = GestoreRicevute()
        if os.path.exists(PathFiles.PATH_RICEVUTE):
            os.remove(PathFiles.PATH_RICEVUTE)
        ricevuta = self.gestore_ricevute.stila_ricevuta("12345678", 60.0, 0.2, "abcdefgh", 0.0)
        self.assertEqual(ricevuta.id_monopattino, "12345678")

    def test_statistiche(self):
        self.gestore_statistiche = GestoreStatistiche()
        self.gestore_ricevute = GestoreRicevute()
        if os.path.exists(PathFiles.PATH_RICEVUTE):
            os.remove(PathFiles.PATH_RICEVUTE)
        self.gestore_ricevute.stila_ricevuta("12345678", 60.0, 0.2, "abcdefgh", 0.0)
        self.gestore_ricevute.stila_ricevuta("12345567", 30.0, 0.1, "abcdefgh", 0.0)
        self.gestore_ricevute.stila_ricevuta("12345687", 120.0, 0.4, "abcdefgh", 0.0)
        self.assertEqual(len(self.gestore_ricevute.get_ricevute()), 3)

    def test_versamento(self):
        self.gestore_clienti = GestoreClienti()
        if os.path.exists(PathFiles.PATH_CLIENTI):
            os.remove(PathFiles.PATH_CLIENTI)
        cliente, portafoglio = self.gestore_clienti.registra_cliente("Dario", "Pozzobon", "POZDAR99A01H501R",
                                                                     "3333333333", "password")
        portafoglio.versa(10.0)
        self.assertEqual(portafoglio.saldo, 10.0)