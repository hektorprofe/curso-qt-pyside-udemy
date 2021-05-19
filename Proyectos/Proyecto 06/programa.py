from PySide6 import QtWidgets
from ui_monitor import Ui_MainWindow
from functools import partial
import pyqtgraph as pg  # pip install pyqtgraph
import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
