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
        dialogo = QMessageBox.warning(
            self, "Aviso", "¿Seguro que deseas aplicar los cambios?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel)

        if dialogo == QMessageBox.Apply:
            print("Aplicamos los cambios")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
