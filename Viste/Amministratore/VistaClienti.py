from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreClienti import GestoreClienti
from Utils.Const.PathViste import PATH_VISTA_CLIENTI
from Viste.Accesso.Signup import Signup
from Viste.Cliente.VistaModificaProfilo import VistaModificaProfilo


class VistaClienti(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(PATH_VISTA_CLIENTI, self)
        self.gestore_clienti = GestoreClienti()
        self.id_cliente = None
        self.lista_clienti = {}
        self.setup_ui()

    def setup_ui(self):
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
        self.listWidget.clear()
        self.lista_clienti = self.gestore_clienti.visualizza_clienti()
        if self.lista_clienti is not None:
            self.listWidget.addItems(cliente.__str__() for cliente in self.lista_clienti.values())
            self.listWidget.clicked.connect(self.seleziona_cliente)

    def seleziona_cliente(self):
        riga = self.listWidget.currentRow()
        keys = list(self.lista_clienti.keys())
        da_cercare = keys[riga]
        cliente = self.lista_clienti.get(da_cercare)
        self.id_cliente = cliente.id

    def go_crea_cliente(self):
        self.crea_account = Signup(False)
        self.crea_account.closed.connect(self.popola_lista_clienti)
        self.crea_account.show()

    def go_elimina_cliente(self):
        if self.id_cliente is not None:
            res = self.gestore_clienti.rimuovi_cliente(self.id_cliente)
            if res:
                self.print_messagebox("Cliente rimosso con successo")
            else:
                self.print_messagebox("Errore nella rimozione del cliente!")
            self.id_cliente = None
        self.popola_lista_clienti()

    def go_modifica_cliente(self):
        if self.id_cliente is not None:
            self.modifica_profilo = VistaModificaProfilo(self.id_cliente)
            self.modifica_profilo.closed.connect(self.popola_lista_clienti)
            self.modifica_profilo.show()
            self.id_cliente = None

    def go_back(self):
        self.close()

    def print_messagebox(self, message):
        mb = QMessageBox()
        mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mb.setWindowTitle("Rimozione cliente")
        mb.setIcon(QMessageBox.Information)
        mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mb.setText(message)
        mb.exec()
