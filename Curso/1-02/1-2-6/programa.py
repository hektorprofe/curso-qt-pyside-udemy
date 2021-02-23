from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        self.resize(480, 320)

        boton = QPushButton("Hola")
        # boton.clicked.connect(self.boton_clicado)
        # boton.pressed.connect(self.boton_pulsado)
        # boton.released.connect(self.boton_liberado)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        print("Botón clicado")

    def boton_pulsado(self):
        print("Botón pulsado")

    def boton_liberado(self):
        print("Botón liberado")

    def boton_alternado(self, valor):
        print("Botón alternado?", valor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
