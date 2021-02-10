from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        self.setMinimumSize(QSize(480, 320))

        button = QPushButton("Hola")

        # Creamos un slot para conectar la señal clicked a un método
        button.clicked.connect(self.boton_clicado)

        # Pulsación y liberación
        button.pressed.connect(self.boton_pulsado)
        button.released.connect(self.boton_liberado)

        # Establecemos un botón alternador true/salse
        button.setCheckable(True)
        button.clicked.connect(self.boton_alternador)

        self.setCentralWidget(button)

    def boton_clicado(self):
        print("¡Me has clicado!")

    def boton_alternador(self, valor):
        print("¿Alternado?", valor)

    def boton_pulsado(self):
        print("¡Me has pulsado!")

    def boton_liberado(self):
        print("¡Me has liberado!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
