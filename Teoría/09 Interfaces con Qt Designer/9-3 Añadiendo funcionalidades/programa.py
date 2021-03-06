from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.mainwindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # configuramos una señal para el botón
        self.pushButton.clicked.connect(self.mostrar_mensaje)

        # configuramos la señal de la acción para salir del programa
        self.actionSalir.triggered.connect(self.close)

    def mostrar_mensaje(self):
        QMessageBox.information(
            self, "Diálogo", f"El contenido del campo de de texto es:\n\n{self.lineEdit.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
