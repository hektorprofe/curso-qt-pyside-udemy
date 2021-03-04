from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QGridLayout, QWidget)
import sys
import random


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en cuadrícula
        cuadricula = QGridLayout()

        # bucles for para generar una cuadrícula
        for fila in range(5):
            for columna in range(5):
                # añadimos una caja de color aleatorio
                color = str(hex(random.randint(0, 16777215)))  # int(0xFFFFFF)
                cuadricula.addWidget(Caja(f"#{color[2:]}"), fila, columna)

        # cremos el widget dummy y le asignamos el layout horizontal
        widget = QWidget()
        widget.setLayout(cuadricula)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
