from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QStackedLayout, QWidget)
from PySide6.QtCore import Qt
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout apilado
        layout = QStackedLayout()

        # Añadimos varios widgets unos sobre otros
        layout.addWidget(Caja("orange"))
        layout.addWidget(Caja("magenta"))
        layout.addWidget(Caja("purple"))
        layout.addWidget(Caja("red"))

        # creamos el widget dummy y le asignamos el layout apilado
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # necesitamos crear un accesor para usar el layout desde el evento
        self.layout = layout

    def keyPressEvent(self, event):
        # recuperamos el índice
        indice = self.layout.currentIndex()
        # buscamos el indice máximo del layout contando cuantos widgets tiene
        indice_maximo = self.layout.count() - 1

        # dependiendo de la flecha presionada sumamos o restamos
        if event.key() == Qt.Key_Right:
            indice += 1
        elif event.key() == Qt.Key_Left:
            indice -= 1

        # rectificamos el índice para generar el efecto infinito
        if indice > indice_maximo:
            indice = 0
        if indice < 0:
            indice = indice_maximo

        # finalmenteestablecemos el nuevo índice
        self.layout.setCurrentIndex(indice)

        # continuamos con el evento por defecto
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
