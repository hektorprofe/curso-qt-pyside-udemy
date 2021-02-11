from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos una casilla y la establecemos de widget central
        casilla = QCheckBox("Casilla de verificación")
        self.setCentralWidget(casilla)

        # establecemos el triestado por defecto, también funcionan los otros
        casilla.setCheckState(Qt.PartiallyChecked)

        # señal para detectar cambios en la casilla
        casilla.stateChanged.connect(self.estado_cambiado)

        # la podemos desactivar
        casilla.setEnabled(False)

        # consultamos el valor actual
        print("¿Activada?", casilla.isChecked())
        print("¿Neutra?", casilla.isTristate())

    def estado_cambiado(self, estado):
        if estado == Qt.Checked:
            print("Casilla marcada")
        if estado == Qt.Unchecked:
            print("Casilla desmarcada")
        if estado == Qt.PartiallyChecked:
            print("Casilla neutra")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
