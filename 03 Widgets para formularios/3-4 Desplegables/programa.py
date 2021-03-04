from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un desplegable
        desplegable = QComboBox()
        self.setCentralWidget(desplegable)

        # Añadimos algunas opciones
        desplegable.addItems(["", "Opción 1", "Opción 2", "Opción 3"])

        # Y algunas señales
        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_cambiado)

        # consultamos el valor actual
        print("Índice actual ->", desplegable.currentIndex())
        print("Texto actual ->", desplegable.currentText())

    def indice_cambiado(self, indice):
        print("Nuevo índice ->", indice)

    def texto_cambiado(self, texto):
        print("Nuevo texto ->", texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
