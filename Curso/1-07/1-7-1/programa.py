from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel)
import sys


class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
        etiqueta = QLabel("Soy una subventana")
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.setWindowTitle("Ventana principal")
        # dummy widget para un layout
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # botón para abrir la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

    def mostrar_subventana(self):
        self.subventana = Subventana()
        self.subventana.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
