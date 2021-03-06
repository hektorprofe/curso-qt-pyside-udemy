from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos diferentes layouts para mezclar
        layoutHor = QHBoxLayout()
        layoutVer1 = QVBoxLayout()
        layoutVer2 = QVBoxLayout()

        # añadimos una caja al principio del layaout 1
        layoutHor.addWidget(Caja("green"))
        # luego anidamos dos layouts verticales
        layoutHor.addLayout(layoutVer1)
        layoutHor.addLayout(layoutVer2)

        # en el primer layout vertical añadimos dos cajas
        layoutVer1.addWidget(Caja("blue"))
        layoutVer1.addWidget(Caja("red"))

        # en el segundo layout vertical añadimos tres cajas
        layoutVer2.addWidget(Caja("orange"))
        layoutVer2.addWidget(Caja("magenta"))
        layoutVer2.addWidget(Caja("purple"))

        # cremos el widget dummy y le asignamos el layout horizontal
        widget = QWidget()
        widget.setLayout(layoutHor)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
