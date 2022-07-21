from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Attivita.Cliente import Cliente
from Viste.Cliente.ModificaProfilo import ModificaProfilo


class CUDCliente(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Viste/Amministratore/GUI/cud_cliente.ui", self)
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_crea_cliente.clicked.connect(self.go_crea_cliente)
        self.bottone_elimina_cliente.clicked.connect(self.go_elimina_cliente)
        self.bottone_modifica_cliente.clicked.connect(self.go_modifica_cliente)
        self.back_button.clicked.connect(self.go_back)
        self.codice_cliente_selezionato = None
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
        self.crea_account = CreaAccount()
        self.crea_account.closed.connect(self.popola_lista_clienti)
        self.crea_account.show()

    def go_elimina_cliente(self):
        if self.codice_cliente_selezionato is not None:
            cliente = Cliente().ricerca_cliente_codice(self.codice_cliente_selezionato.text().split("\n")[0].split(" ")[1])
            cliente.rimuovi_cliente_codice(self.codice_cliente_selezionato.text().split("\n")[0].split(" ")[1])
            self.popola_lista_clienti()
            self.codice_cliente_selezionato = None

    def go_modifica_cliente(self):
        if self.codice_cliente_selezionato is not None:
            cliente = Cliente().ricerca_cliente_codice(self.codice_cliente_selezionato.text().split("\n")[0].split(" ")[1])
            self.modifica_profilo = ModificaProfilo(cliente)
            self.modifica_profilo.closed.connect(self.popola_lista_clienti)
            self.modifica_profilo.show()
            self.codice_cliente_selezionato = None

    def go_back(self):
        self.close()


class CreaAccount(QDialog):
    closed = pyqtSignal()

    def __init__(self):
        super(CreaAccount, self).__init__()
        loadUi("Viste/Accesso/GUI/createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def createaccfunction(self):
        # if self.check_campi():
        cliente = Cliente()
        nome = self.nome.text().capitalize().strip()
        cognome = self.cognome.text().capitalize().strip()
        cf = self.cf.text().upper().strip()
        telefono = self.telefono.text().strip()
        password = self.password.text().strip()
        if CreaAccount.check_campi(self):
            cliente, message = cliente.crea_cliente(nome=nome, cognome=cognome, telefono=telefono, codicefiscale=cf,
                                                    password=password)
            if cliente is not None:
                QMessageBox.information(self, "Attenzione!", message + "codice: " + str(cliente.codice) + " password: " + str(cliente.password))
                self.close()
            else:
                QMessageBox.warning(self, "Attenzione!", message)

    def closeEvent(self, event):
        self.closed.emit()

    def check_campi(self):
        # il nome deve avere minimo 3 caratteri
        if len(self.nome.text()) > 2:
            # il cognome deve avere minimo 3 caratteri
            if len(self.cognome.text()) > 2:
                # il codice fiscale deve essere esattamente di 16 caratteri
                if len(self.cf.text()) == 16 and self.cf.text().isalnum():
                    # il numero di telefono puo avere solo 10 cifre
                    if len(self.telefono.text()) == 10 and str(self.telefono.text()).isnumeric():
                        return True
                    else:
                        QMessageBox.warning(self, "Attenzione!", "Il numero di telefono puo contenere solo 10 cifre")
                else:
                    QMessageBox.warning(self, "Attenzione!", "Il codice fiscale puo contenere solo 16 caratteri")
            else:
                QMessageBox.warning(self, "Attenzione!", "Il cognome deve avere almeno 3 caratteri")
        else:
            QMessageBox.warning(self, "Attenzione!", "Il nome deve avere almeno 3 caratteri")
        return False