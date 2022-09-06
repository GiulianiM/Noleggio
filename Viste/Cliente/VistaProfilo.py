from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathViste import PATH_VISTA_PROFILO
from Viste.Cliente.VistaModificaProfilo import VistaModificaProfilo
from Viste.Cliente.VistaPortafoglio import VistaPortafoglio
from Viste.Cliente.VistaRicevute import VistaRicevute


class VistaProfilo(QDialog):
    def __init__(self):
        super(VistaProfilo, self).__init__()
        loadUi(PATH_VISTA_PROFILO, self)
        self.gestore_clienti = GestoreClienti()
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        # setup dei label
        self.id_label_to_edit.setText(self.gestore_clienti.cliente_corrente.id)
        self.nome_label_to_edit.setText(self.gestore_clienti.cliente_corrente.nome)
        self.cognome_label_to_edit.setText(self.gestore_clienti.cliente_corrente.cognome)
        self.cf_label_to_edit.setText(self.gestore_clienti.cliente_corrente.cf)
        self.telefono_label_to_edit.setText(self.gestore_clienti.cliente_corrente.telefono)
        # setup dei bottoni
        self.back_button.clicked.connect(self.go_back)
        self.bottone_modifica.clicked.connect(self.go_modifica_profilo)
        self.bottone_visualizza_portafoglio.clicked.connect(self.go_visualizza_portafoglio)
        self.bottone_visualizza_ricevute.clicked.connect(self.go_visualizza_ricevute)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_modifica_profilo(self):
        self.modifica_profilo = VistaModificaProfilo()
        self.modifica_profilo.closed.connect(self.refresh_labels)
        self.modifica_profilo.show()

    def go_visualizza_portafoglio(self):
        self.visualizza_portafoglio = VistaPortafoglio()
        self.visualizza_portafoglio.show()

    def go_visualizza_ricevute(self):
        self.visualizza_ricevute = VistaRicevute()
        self.visualizza_ricevute.show()

    def go_back(self):
        self.close()

    def refresh_labels(self):
        self.gestore_clienti = GestoreClienti()
        self.nome_label_to_edit.setText(self.gestore_clienti.cliente_corrente.nome)
        self.cognome_label_to_edit.setText(self.gestore_clienti.cliente_corrente.cognome)
        self.cf_label_to_edit.setText(self.gestore_clienti.cliente_corrente.cf)
        self.telefono_label_to_edit.setText(self.gestore_clienti.cliente_corrente.telefono)