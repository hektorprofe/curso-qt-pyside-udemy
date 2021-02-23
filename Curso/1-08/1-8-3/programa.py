from PySide2.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStyle)
import sys
import qtawesome as qta


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        icono = qta.icon("fa5.save", color="green")
        boton = QPushButton(icono, "Botón guardar")
        self.setCentralWidget(boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
