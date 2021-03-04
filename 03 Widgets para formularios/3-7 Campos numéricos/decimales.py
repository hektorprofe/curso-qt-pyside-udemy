from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox
from PySide6.QtCore import QSize, Qt, QLocale
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un campo numérico entero
        numero = QDoubleSpinBox()
        self.setCentralWidget(numero)

        # Probamos algunas opciones
        numero.setMinimum(0)
        numero.setMaximum(10)
        numero.setRange(0, 10)
        numero.setSingleStep(0.5)

        # Prefijos y sufijos
        numero.setPrefix("$")
        numero.setSuffix("%")

        # Probamos algunas señales
        numero.valueChanged.connect(self.valor_cambiado)

        # Establecer y recuperar el valor
        numero.setValue(3.14)
        print(numero.value())

    def valor_cambiado(self, numero):
        # al presionar enter recuperamos el texto a partir del widget central
        print("Valor cambiado ->", numero)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
