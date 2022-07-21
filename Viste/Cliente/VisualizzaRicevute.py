from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Attivita.Ricevuta import Ricevuta


class VisualizzaRicevute(QDialog):
    def __init__(self, cliente):
        super(VisualizzaRicevute, self).__init__()
        loadUi("viste/cliente/gui/visualizza_ricevute.ui", self)
        self.cliente = cliente
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_indietro)
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
        self.popola_lista_ricevute()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def go_indietro(self):
        self.close()

    def popola_lista_ricevute(self):
        ricevute = Ricevuta().get_ricevute_cliente(self.cliente.codice)
        if ricevute is not None:
            self.listWidget.clear()
            self.listWidget.addItems(ricevuta.get_ricevuta_to_string() for ricevuta in ricevute)
