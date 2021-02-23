from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
from PySide6.QtGui import QIcon
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.setWindowIcon(QIcon(absPath("icon.png")))

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QMessageBox.about(
            self, "Acerca de", "<p>Información del programa</p><p>Segundo parágrado</p>")
        # podemos analizar el tipo de botón clicado para actuar en consecuencia
        print(dialogo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
