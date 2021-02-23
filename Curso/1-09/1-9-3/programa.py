from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.mainwindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.mostrar_mensaje)
        self.actionSalir.triggered.connect(self.close)

    def mostrar_mensaje(self):
        QMessageBox.information(
            self, "Hola", f"El contenido del texto es: {self.lineEdit.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
