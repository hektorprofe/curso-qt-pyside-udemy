from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel)
import sys
import random


class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
        etiqueta = QLabel(f"Soy una subventana... {random.randint(0,100)}")
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

        self.subventana = Subventana()

        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(lambda: self.subventana.show())
        layout.addWidget(boton_mostrar)

        boton_ocultar = QPushButton("Ocultar subventana")
        boton_ocultar.clicked.connect(lambda: self.subventana.hide())
        layout.addWidget(boton_ocultar)

        boton_alternador = QPushButton("Alternar subventana")
        boton_alternador.clicked.connect(
            lambda: self.subventana.hide()
            if self.subventana.isVisible()
            else self.subventana.show())
        layout.addWidget(boton_alternador)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
