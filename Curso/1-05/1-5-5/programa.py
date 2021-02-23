from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFontDialog, QColorDialog)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

        self.boton = boton

    def boton_clicado(self):
        confirmado, fuente = QFontDialog.getFont(self)
        if confirmado:
            self.boton.setFont(fuente)
        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f"background-color:{color.name()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
