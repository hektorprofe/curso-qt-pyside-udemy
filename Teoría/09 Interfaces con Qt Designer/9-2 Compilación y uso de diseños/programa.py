from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.mainwindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor de la superclase
        super().__init__()

        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
