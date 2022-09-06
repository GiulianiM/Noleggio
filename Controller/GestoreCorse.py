from Attivita.Corsa import Corsa
from Controller.GestoreClienti import GestoreClienti
from Controller.GestoreMezzi import GestoreMezzi
from Controller.GestoreRicevute import GestoreRicevute
from Servizio.Monopattino import Monopattino


class GestoreCorse:

    def __init__(self):
        self.gestore_clienti = GestoreClienti()
        self.gestore_ricevute = GestoreRicevute()
        self.gestore_mezzi = GestoreMezzi()
        self.corsa = None

    # 1. controllo il saldo (minimo 5€)
    # 2. prelevo le informazioni del monopattino
    # 3. setto il monopattino a "non disponibile"
    # 4. avvio la corsa
    # return: Boolean
    def avvia_corsa(self, id_monopattino):
        if float(self.gestore_clienti.visualizza_portafoglio()) >= 5.00:
            monopattino = self.gestore_mezzi.ricerca_monopattino_id(id_monopattino)
            if isinstance(monopattino, Monopattino):
                self.gestore_mezzi.set_monopattino(monopattino)
                self.gestore_mezzi.set_disponibilita_monopattino(False)
                self.corsa = Corsa()
                self.corsa.avvia()
                return True
        return False

    # 1. controllo se esiste una corsa avviata
    # 2. calcolo il tempo_utilizzo impiegato e il costo totale
    # 3. prelevo il denaro dal conto
    # 4. stilo la gestore_statistiche
    # return: String
    def termina_corsa(self):
        if isinstance(self.corsa, Corsa) and isinstance(self.gestore_mezzi.monopattino, Monopattino):
            self.corsa.termina()
            self.gestore_mezzi.set_disponibilita_monopattino(True)
            tempo_totale = self.corsa.tempo_utilizzo()
            costo_totale = self.corsa.costo_totale()
            self.gestore_clienti.preleva_denaro(costo_totale)
            ricevuta = self.gestore_ricevute.stila_ricevuta(
                id_monopattino=self.gestore_mezzi.monopattino.id,
                tempo_totale=tempo_totale,
                costo_totale=costo_totale,
                saldo_portafoglio=self.gestore_clienti.visualizza_portafoglio(),
                id_cliente=self.gestore_clienti.cliente_corrente.id
            )
            self.corsa = None
            return True, ricevuta
        return False, None
