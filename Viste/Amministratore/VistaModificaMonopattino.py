from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Utils.Const.PathViste import PATH_VISTA_MODIFICA_MEZZO


class VistaModificaMonopattino(QDialog):
    closed = pyqtSignal()

    def __init__(self, gestore_mezzi):
        super().__init__()
        loadUi(PATH_VISTA_MODIFICA_MEZZO, self)
        self.gestore_mezzi = gestore_mezzi
        self.setup_ui()

    def setup_ui(self):
        self.disponibile_button.clicked.connect(self.go_disponibile)
        self.non_disponibile_button.clicked.connect(self.go_non_disponibile)
        self.back_button.clicked.connect(self.go_back)
        self.id_label_to_edit.setText(str(self.gestore_mezzi.monopattino.id))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        if self.gestore_mezzi.monopattino.get_disponibilita():
            self.disponibile_label_to_edit.setText("Disponibile")
            self.disponibile_button.setChecked(False)
            self.non_disponibile_button.setChecked(True)
        else:
            self.disponibile_label_to_edit.setText("Non Disponibile")
            self.disponibile_button.setChecked(True)
            self.non_disponibile_button.setChecked(False)

    def go_disponibile(self):
        self.gestore_mezzi.set_disponibilita_monopattino(True)
        self.disponibile_label_to_edit.setText("Disponibile")
        self.disponibile_button.setChecked(False)
        self.non_disponibile_button.setChecked(True)

    def go_non_disponibile(self):
        self.gestore_mezzi.set_disponibilita_monopattino(False)
        self.disponibile_label_to_edit.setText("Non Disponibile")
        self.disponibile_button.setChecked(True)
        self.non_disponibile_button.setChecked(False)

    def go_back(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
