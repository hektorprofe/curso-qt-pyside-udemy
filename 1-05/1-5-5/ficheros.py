from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog)
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
        #fichero, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", ".")
        fichero, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
        print(fichero)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
