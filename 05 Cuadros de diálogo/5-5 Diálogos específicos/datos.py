from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QInputDialog)
from PySide6.QtCore import QTranslator, QLibraryInfo
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        # dialogo = QInputDialog.getText(self, "Título", "Texto")
        # dialogo = QInputDialog.getInt(self, "Título", "Entero")
        # dialogo = QInputDialog.getDouble(self, "Título", "Decimal")
        # dialogo = QInputDialog.getItem(self, "Título",  "Colores", ["Rojo", "Azul", "Blanco", "Verde"])
        color, confirmado = QInputDialog.getItem(
            self, "Título",  "Colores", ["Rojo", "Azul", "Blanco", "Verde"])
        if confirmado:
            print(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
