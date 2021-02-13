from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from pathlib import Path
import recursos_rc
import sys

# creas los recursos en el designer y los compilas, los importas arriba y lito
# rcc.exe -g python -o recursos_rc.py recursos.qrc

# pdemos abrir un directorio de VSC en la terminal, clic derecho open in terminal
# uic.exe -g python interfaces/widget.ui -o widget.py

# exportar de ui a py desde el editor:
# Formulario > View Python code > conbiurar en directorio de pyside6/bin rcc.exe
# y magia, ahi tienes los ficheros transformados xD

# estilos -> clic derecho Cambiar hojas de estilos, pegar contenido QSS, listo

# tamaño central widget -> hacer servir el centralWidget como un layout directamente, cambiar distribucionusando botones de arriba con rectangulos, grid y tal


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


def loadUi(file):
    return QUiLoader().load(absPath(file))


def MainWindow(file):
    window = loadUi(file)
    window.widget = loadUi("interfaces/widget.ui")
    window.pushButton.clicked.connect(lambda: window.widget.show())
    return window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow("interfaces/main.ui")
    window.show()
    sys.exit(app.exec_())
