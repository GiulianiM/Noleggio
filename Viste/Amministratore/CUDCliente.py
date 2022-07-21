from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Cliente import Cliente
from Viste.Cliente.ModificaProfilo import ModificaProfilo
import Viste.Accesso.Autenticazione as Autenticazione


class CUDCliente(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Viste/Amministratore/GUI/cud_cliente.ui", self)
        self.codice_cliente_selezionato = None

        self.bottone_crea_cliente.clicked.connect(self.go_crea_cliente)
        self.bottone_elimina_cliente.clicked.connect(self.go_elimina_cliente)
        self.bottone_modifica_cliente.clicked.connect(self.go_modifica_cliente)
        self.back_button.clicked.connect(self.go_back)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setStyleSheet("""
        QListView {
            background-color: rgb(127, 127, 127);
            color: rgb(255, 255, 255);
            }
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:3px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(38, 157, 206), stop: 0.5 rgb(38, 157, 206), stop:1 rgb(38, 157, 206));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(38, 157, 206), stop: 0.5 rgb(38, 157, 206),  stop:1 rgb(38, 157, 206));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(38, 157, 206), stop: 0.5 rgb(38, 157, 206),  stop:1 rgb(38, 157, 206));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
    """)
        self.popola_lista_clienti()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def popola_lista_clienti(self):
        clienti = Cliente().get_clienti()
        if clienti is not None:
            self.listWidget.clear()
            self.listWidget.addItems(cliente.get_cliente_to_string() for cliente in clienti.values())
            self.listWidget.clicked.connect(self.seleziona_cliente)

    def seleziona_cliente(self):
        self.codice_cliente_selezionato = self.listWidget.currentItem()

    def go_crea_cliente(self):
        self.crea_account = Autenticazione.Signup(False)
        self.crea_account.closed.connect(self.popola_lista_clienti)
        self.crea_account.show()

    def go_elimina_cliente(self):
        if self.codice_cliente_selezionato is not None:
            message = Cliente().rimuovi_cliente_codice(self.codice_cliente_selezionato.text().split("\n")[0].split(" ")[1])
            QMessageBox.information(self, "Rimozione cliente", message)
            self.popola_lista_clienti()
            self.codice_cliente_selezionato = None

    def go_modifica_cliente(self):
        if self.codice_cliente_selezionato is not None:
            self.modifica_profilo = ModificaProfilo(self.codice_cliente_selezionato.text().split("\n")[0].split(" ")[1])
            self.modifica_profilo.closed.connect(self.popola_lista_clienti)
            self.modifica_profilo.show()
            self.codice_cliente_selezionato = None

    def go_back(self):
        self.close()

