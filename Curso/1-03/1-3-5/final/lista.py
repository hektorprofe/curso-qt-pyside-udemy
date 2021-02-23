from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos una lista
        lista = QListWidget()
        self.setCentralWidget(lista)

        # Añadimos algunas opciones
        lista.addItems(["Opción 1", "Opción 2", "Opción 3"])

        # Y algunas señales
        lista.currentItemChanged.connect(self.item_cambiado)

        # Comprobar el item actual
        print(lista.currentItem())

    def item_cambiado(self, item):
        # Conseguimos el texto del ítem con su método text()
        print("Nuevo ítem ->", item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
