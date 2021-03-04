from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit  # editado
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        self.setMinimumSize(QSize(480, 320))

        # widget input de texto
        texto = QLineEdit()
        # capturamos la señal de texto cambiado
        texto.textChanged.connect(self.texto_modificado)

        # establecemos el widget central
        self.setCentralWidget(texto)

        # creamos el puntero
        self.texto = texto

    def texto_modificado(self):
        # recuperasmo el texto del input
        texto_recuperado = self.texto.text()
        # modificamos el título de la ventana al vuelo
        self.setWindowTitle(texto_recuperado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
