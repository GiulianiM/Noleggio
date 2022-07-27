from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Corsa import Corsa
from Servizio.Mezzo import Mezzo
from Servizio.Monopattino import Monopattino


class VistaCorsa(QDialog):
    def __init__(self, cliente):
        super(VistaCorsa, self).__init__()
        loadUi("viste/cliente/gui/corsa.ui", self)
        self.cliente = cliente

        self.bottone_inizia_corsa.clicked.connect(self.go_avvia_corsa)
        self.bottone_termina_corsa.clicked.connect(self.go_termina_corsa)
        self.back_button.clicked.connect(self.go_indietro)
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

    # mostra una lista di mezzi disponibili (i loro codici)
    def popola_lista_mezzi(self):
        mezzi = Mezzo().get_mezzi_disponibili()
        if mezzi is not None:
            self.listWidget.clear()
            self.listWidget.addItems([mezzo.codice for mezzo in mezzi])
            self.listWidget.clicked.connect(self.seleziona_mezzo)

    # rilevo il mezzo selezionato dalla lista
    def seleziona_mezzo(self):
        self.codice_mezzo_selezionato = self.listWidget.currentItem()
        if self.bottone_termina_corsa.isEnabled():
            self.bottone_inizia_corsa.setEnabled(False)
        else:
            self.bottone_inizia_corsa.setEnabled(True)

    # controllo che il saldo sia sufficiente (minimo 1€ che garantisce almeno 5 minuti di viaggio)
    # se il saldo è sufficiente:
    #   - disabilita il bottone di inizio corsa
    #   - abilita il bottone di fine corsa
    #   - avvio la corsa
    #   - aggiorno la lista dei mezzi disponibili
    def go_avvia_corsa(self):
        mezzo_selezionato = Mezzo().ricerca_mezzo_codice(self.codice_mezzo_selezionato.text())
        if isinstance(mezzo_selezionato, Monopattino):
            if float(self.cliente.portafoglio.get_saldo()) >= (mezzo_selezionato.costo_minuto * Mezzo().MINIMO_MINUTI):
                self.bottone_inizia_corsa.setEnabled(False)
                self.bottone_termina_corsa.setEnabled(True)
                self.corsa = Corsa(self.cliente)
                self.corsa.avvia_corsa(self.codice_mezzo_selezionato.text())
                self.popola_lista_mezzi()
                QMessageBox.information(self, "Attenzione!", '<p style=color:white>La corsa è iniziata!</p>')
            else:
                QMessageBox.warning(self, "Attenzione!", "<p style=color:white>Saldo insufficiente")

    # questo metodo può essere chiamato solo se c'è una corsa in corso
    # in quel caso:
    #  - disabilita il bottone di fine corsa
    #  - abilita il bottone di inizio corsa
    #  - termino la corsa
    #  - aggiorno la lista dei mezzi disponibili
    def go_termina_corsa(self):
        self.bottone_termina_corsa.setEnabled(False)
        message = self.corsa.termina_corsa().split("\n")
        message_to_print = '<p style= color:white>' + message[0] + '</p>' + '<p style= color:white>' + message[1] + \
                           '</p>' + '<p style= color:white>' + message[2] + '</p>' + \
                           '<p style= color:white>' + message[3] + '</p>' + '<p style= color:white>' + message[4]
        QMessageBox.information(self, "Ricevuta", message_to_print)
        self.popola_lista_mezzi()

    def go_indietro(self):
        self.close()
