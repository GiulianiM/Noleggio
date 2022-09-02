import sys

from PyQt5.QtWidgets import QApplication

from Viste.Accesso.Autenticazione import Login
import ctypes

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Login()
    myappid = u'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    mainwindow.show()
    sys.exit(app.exec())