from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreMezzi import GestoreMezzi
from Utils.Const.PathViste import PATH_VISTA_MEZZI
from Viste.Amministratore.VistaModificaMonopattino import VistaModificaMonopattino


class VistaMezzi(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(PATH_VISTA_MEZZI, self)
        self.gestore_mezzi = GestoreMezzi()
        self.id_monopattino = None
        self.lista_monopattini = {}
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_crea_mezzo.clicked.connect(self.go_aggiungi_monopattino)
        self.bottone_elimina_mezzo.clicked.connect(self.go_elimina_monopattino)
        self.bottone_modifica_mezzo.clicked.connect(self.go_modifica_monopattino)
        self.back_button.clicked.connect(self.go_back)
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
        self.popola_lista_mezzi()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def popola_lista_mezzi(self):
        self.listWidget.clear()
        self.lista_monopattini = self.gestore_mezzi.get_all_mezzi()
        if len(self.lista_monopattini) > 0:
            self.listWidget.addItems(mezzo.__str__() for mezzo in self.lista_monopattini.values())
            self.listWidget.clicked.connect(self.seleziona_mezzo)

    # 1. preleva il numero di riga cliccata
    # 2. prelevo le chiavi dal dizionario self.lista_monopattini
    # 3. interccetto la chiave da cercare che si trova nella posizione "riga"
    # 4. prelevo i dati relativi al monopattino
    # 5. salvo l'id del monopattino selezionato
    def seleziona_mezzo(self):
        riga = self.listWidget.currentRow()
        keys = list(self.lista_monopattini.keys())
        da_cercare = keys[riga]
        monopattino = self.lista_monopattini.get(da_cercare)
        self.id_monopattino = monopattino.id

    def go_aggiungi_monopattino(self):
        self.gestore_mezzi.aggiungi_monopattino()
        self.popola_lista_mezzi()

    def go_elimina_monopattino(self):
        if self.id_monopattino is not None:
            res = self.gestore_mezzi.elimina_monopattino(self.id_monopattino)
            if res:
                self.print_messagebox("Monopattino eliminato con successo!")
            else:
                self.print_messagebox("Errore durante l'eliminazione!")
            self.id_monopattino = None
        self.popola_lista_mezzi()

    def go_modifica_monopattino(self):
        if self.id_monopattino is not None:
            monopattino = self.gestore_mezzi.ricerca_monopattino_id(self.id_monopattino)
            if monopattino is not None:
                self.gestore_mezzi.set_monopattino(monopattino)
                self.modifica_mezzo = VistaModificaMonopattino(self.gestore_mezzi)
                self.modifica_mezzo.closed.connect(self.popola_lista_mezzi)
                self.modifica_mezzo.show()
                self.id_monopattino = None

    def go_back(self):
        self.close()

    def print_messagebox(self, message):
        mb = QMessageBox()
        mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mb.setWindowTitle("Attenzione!")
        mb.setIcon(QMessageBox.Information)
        mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mb.setText(message)
        mb.exec()
