from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from interfaces.mainwindow import Ui_MainWindow
from interfaces.subventana import Ui_Form
import sys


class Subventana(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.mostrar_subventana)
        self.actionSalir.triggered.connect(self.close)

        self.subventana = Subventana()

    def mostrar_subventana(self):
        self.subventana.label.setText(self.lineEdit.text())
        self.subventana.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
