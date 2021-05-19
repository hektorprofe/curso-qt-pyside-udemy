import sys
import time
from PySide6 import QtWidgets, QtCore
from ui_interfaz import Ui_MainWindow
from pyquery import PyQuery as pq  # pip install pyquery


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# PyQuery: https://pythonhosted.org/pyquery/index.html
# QRunnable: https://doc.qt.io/qtforpython/PySide6/QtCore/QRunnable.html
# QThread: https://doc.qt.io/qtforpython/PySide6/QtCore/QThreadPool.html
# Signal: https://doc.qt.io/qtforpython/PySide6/QtCore/Signal.html
# QTime (Hora) https://doc.qt.io/qtforpython/PySide6/QtCore/QTime.html
