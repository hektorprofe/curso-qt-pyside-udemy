from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        icono = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        boton = QPushButton(icono, "Botón guardar")
        self.setCentralWidget(boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
