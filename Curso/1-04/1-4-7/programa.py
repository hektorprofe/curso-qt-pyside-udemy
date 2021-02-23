from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTabWidget
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tabs = QTabWidget()

        tabs.addTab(Caja("orange"), "Naranja")
        tabs.addTab(Caja("magenta"), "Magenta")
        tabs.addTab(Caja("purple"), "Morado")
        tabs.addTab(Caja("red"), "Rojo")

        tabs.setTabPosition(QTabWidget.East)
        tabs.setMovable(True)

        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
