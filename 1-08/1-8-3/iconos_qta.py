from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton)  # edited PySide2
import sys
import qtawesome as qta


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # recuperamos el icono de qta y lo añadimos a un botón
        icono = qta.icon('fa5b.github')
        boton = QPushButton(icono, "Github")

        self.setCentralWidget(boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
