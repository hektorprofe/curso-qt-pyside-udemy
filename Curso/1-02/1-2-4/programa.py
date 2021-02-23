from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        boton = QPushButton("Soy un botón")
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
