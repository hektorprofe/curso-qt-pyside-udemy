from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path
import sys


def absPath(file):
    # Devuelve la ruta absoluta a un fichero desde el propio script
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))

        etiqueta = QLabel("Soy una etiqueta")
        self.setCentralWidget(etiqueta)

        # Creamos la imagen
        imagen = QPixmap(absPath("naturaleza.jpg"))
        # la asginamos a la etiqueta
        etiqueta.setPixmap(imagen)
        # hacemos que se escale con la ventana
        etiqueta.setScaledContents(True)

        # establecemos unas flags de alineamiento
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
