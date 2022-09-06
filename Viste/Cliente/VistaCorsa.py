from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestoreCorse import GestoreCorse
from Utils.Const.PathViste import PATH_VISTA_CORSE


class VistaCorsa(QDialog):
    def __init__(self):
        super(VistaCorsa, self).__init__()
        loadUi(PATH_VISTA_CORSE, self)
        self.gestore_corse = GestoreCorse()
        self.setup_ui()

    def setup_ui(self):
        self.bottone_inizia_corsa.clicked.connect(self.go_avvia_corsa)
        self.bottone_termina_corsa.clicked.connect(self.go_termina_corsa)
        self.back_button.clicked.connect(self.go_back)
        self.bottone_inizia_corsa.setEnabled(False)
        self.bottone_termina_corsa.setEnabled(False)
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

    # mostra una lista di monopattini disponibili (i loro codici)
    def popola_lista_mezzi(self):
        self.listWidget.clear()
        mezzi = self.gestore_corse.gestore_mezzi.get_mezzi_disponibili()
        if len(mezzi) > 0:
            self.listWidget.addItems([mezzo.id for mezzo in mezzi])
            self.listWidget.clicked.connect(self.seleziona_mezzo)

    # rilevo il monopattino selezionato dalla lista
    def seleziona_mezzo(self):
        self.id_monopattino_selezionato = self.listWidget.currentItem()
        if self.bottone_termina_corsa.isEnabled():
            self.bottone_inizia_corsa.setEnabled(False)
        else:
            self.bottone_inizia_corsa.setEnabled(True)

    def go_avvia_corsa(self):
        is_avviata = self.gestore_corse.avvia_corsa(self.id_monopattino_selezionato.text())
        if is_avviata:
            self.bottone_inizia_corsa.setEnabled(False)
            self.bottone_termina_corsa.setEnabled(True)
            self.print_messagebox("Attenzione", "Corsa avviata con successo")
            self.popola_lista_mezzi()
        else:
            self.print_messagebox("Attenzione!", "Corsa non avviata, saldo insufficiente!")

    def go_termina_corsa(self):
        is_terminata, ricevuta = self.gestore_corse.termina_corsa()
        if is_terminata:
            self.bottone_inizia_corsa.setEnabled(True)
            self.bottone_termina_corsa.setEnabled(False)
            self.popola_lista_mezzi()
            self.print_messagebox("Ricevuta", ricevuta.__str__())

    def go_back(self):
        self.go_termina_corsa()
        self.close()

    def print_messagebox(self, title, message):
        mb = QMessageBox()
        mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mb.setWindowTitle(title)
        mb.setIcon(QMessageBox.Information)
        mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mb.setText(message)
        mb.exec()
