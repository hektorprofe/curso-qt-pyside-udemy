from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from pathlib import Path
from main_ui import *
from widget_ui import *
import recursos_rc
import sys

# exportar de ui a py desde el editor:
# Formulario > View Python code > conbiurar en directorio de pyside6/bin rcc.exe
# y magia, ahi tienes los ficheros transformados xD

# creas los recursos en el designer y los compilas, los importas arriba y lito
# rcc.exe -g python -o recursos_rc.py recursos.qrc

# pdemos abrir un directorio de VSC en la terminal, clic derecho open in terminal
# uic.exe -g python interfaces/widget.ui -o widget_ui.py


class Widget(QWidget, Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.widget = Widget()
        self.pushButton.clicked.connect(lambda: window.widget.show())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
