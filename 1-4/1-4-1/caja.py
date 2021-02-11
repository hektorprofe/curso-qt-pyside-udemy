from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class Contenedor(QColor):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        contenedor = Contenedor("red")
        self.setCentralWidget(contenedor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
