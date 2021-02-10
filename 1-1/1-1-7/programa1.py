from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        self.setMinimumSize(QSize(480, 320))

        button = QPushButton("Hola")
        button.setCheckable(True)
        button.clicked.connect(self.boton_alternador)

        self.setCentralWidget(button)

        # me gusta crear los accesos alfinal
        self.button = button

    def boton_alternador(self, valor):
        if valor:
            self.button.setText("Estoy activado")
        else:
            self.button.setText("Estoy desactivado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
