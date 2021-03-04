from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # empezamos creando un layout vertical
        layout = QHBoxLayout()

        # le añadimos unas cuantas cajas
        layout.addWidget(Caja("green"))
        layout.addWidget(Caja("blue"))
        layout.addWidget(Caja("red"))

        # modificamos los márgenes
        layout.setContentsMargins(0, 0, 0, 0)

        # modificamos el espaciado
        layout.setSpacing(0)

        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
