from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QMessageBox.warning(
            self, "Diálogo de aviso", "¿Estás seguro de aplicar los cambios?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel)

        if dialogo == QMessageBox.Apply:
            print("Realizar algo importante")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
