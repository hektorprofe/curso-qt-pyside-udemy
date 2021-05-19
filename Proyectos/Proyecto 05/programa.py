from PySide6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLCDNumber, QPushButton)
from functools import partial
from helpers import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(480)
        self.setFixedHeight(360)
        self.setWindowTitle("Calculadora")
        with open(absPath("Scalcula.qss")) as styles:
            self.setStyleSheet(styles.read())

        self.setLayout(QGridLayout())
        self.calculadora = QLCDNumber()
        self.layout().addWidget(self.calculadora, 0, 0)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()
