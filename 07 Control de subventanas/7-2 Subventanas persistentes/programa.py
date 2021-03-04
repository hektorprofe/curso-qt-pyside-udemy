from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)
import sys
import random


class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Subventana")

        # creamos una etiqueta con texto aleatorio
        etiqueta = QLabel(f"Soy una subventana... {random.randint(0, 100)}")

        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # creamos una instancia de la subventana al principio
        self.subventana = Subventana()

        # botón para mostrar la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.subventana.show)
        layout.addWidget(boton_mostrar)

        # botón para ocultar la subventana
        boton_ocultar = QPushButton("Ocultar subventana")
        boton_ocultar.clicked.connect(self.subventana.hide)
        layout.addWidget(boton_ocultar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
