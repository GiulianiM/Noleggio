from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Servizio.Mezzo import Mezzo


class CUDMezzo(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Viste/Amministratore/GUI/cud_mezzo.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_crea_mezzo.clicked.connect(self.go_crea_mezzo)
        self.bottone_elimina_mezzo.clicked.connect(self.go_elimina_mezzo)
        self.bottone_modifica_mezzo.clicked.connect(self.go_modifica_mezzo)
        self.back_button.clicked.connect(self.go_back)
        self.codice_mezzo_selezionato = None
        self.popola_lista_mezzi()

    def go_back(self):
        self.close()

    def popola_lista_mezzi(self):
        mezzi = Mezzo().get_mezzi()
        if mezzi is not None:
            self.listWidget.clear()
            self.listWidget.addItems(mezzo.get_mezzo_to_string() for mezzo in mezzi.values())
            self.listWidget.clicked.connect(self.seleziona_mezzo)

    def seleziona_mezzo(self):
        self.codice_mezzo_selezionato = self.listWidget.currentItem()

    def go_crea_mezzo(self):
        mezzo = Mezzo()
        mezzo.inserisci_mezzo()
        self.popola_lista_mezzi()

    def go_elimina_mezzo(self):
        if self.codice_mezzo_selezionato is not None:
            mezzo = Mezzo().ricerca_mezzo_codice(self.codice_mezzo_selezionato.text().split("-")[0].split(" ")[1])
            mezzo.rimuovi_mezzo(self.codice_mezzo_selezionato.text().split("-")[0].split(" ")[1])
            self.popola_lista_mezzi()
            self.codice_mezzo_selezionato = None

    def go_modifica_mezzo(self):
        if self.codice_mezzo_selezionato is not None:
            mezzo = Mezzo().ricerca_mezzo_codice(self.codice_mezzo_selezionato.text().split("-")[0].split(" ")[1])
            self.modifica_mezzo = ModificaMezzo(mezzo)
            self.modifica_mezzo.closed.connect(self.popola_lista_mezzi)
            self.modifica_mezzo.show()
            self.codice_mezzo_selezionato = None


class ModificaMezzo(QDialog):
    closed = pyqtSignal()

    def __init__(self, mezzo):
        super().__init__()
        loadUi("Viste/Amministratore/GUI/modifica_mezzo.ui", self)
        self.mezzo = mezzo
        self.disponibile_button.clicked.connect(self.go_disponibile)
        self.non_disponibile_button.clicked.connect(self.go_non_disponibile)
        self.back_button.clicked.connect(self.go_back)
        self.id_label_to_edit.setText(str(mezzo.codice))
        if mezzo.disponibile:
            self.disponibile_label_to_edit.setText("Disponibile")
            self.disponibile_button.setChecked(False)
            self.non_disponibile_button.setChecked(True)
        else:
            self.disponibile_label_to_edit.setText("Non Disponibile")
            self.disponibile_button.setChecked(True)
            self.non_disponibile_button.setChecked(False)

    def go_back(self):
        self.close()

    def go_disponibile(self):
        self.mezzo.set_disponibilita(self.mezzo.codice, True)
        self.disponibile_label_to_edit.setText("Disponibile")
        self.disponibile_button.setChecked(False)
        self.non_disponibile_button.setChecked(True)

    def go_non_disponibile(self):
        self.mezzo.set_disponibilita(self.mezzo.codice, False)
        self.disponibile_label_to_edit.setText("Non Disponibile")
        self.disponibile_button.setChecked(True)
        self.non_disponibile_button.setChecked(False)


    def closeEvent(self, event):
        self.closed.emit()

