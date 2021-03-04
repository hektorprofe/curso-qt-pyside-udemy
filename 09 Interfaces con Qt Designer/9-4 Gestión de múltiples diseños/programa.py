from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from interfaces.mainwindow import Ui_MainWindow
from interfaces.subventana import Ui_Form  # el diseño de un widget es un form
import sys


class Subventana(QWidget, Ui_Form):
    def __init__(self):
        # Llamamos al constructor de la superclase
        super().__init__()
        # generamos la interfaz de la subventana
        self.setupUi(self)
        # señal para cerrar la subventana
        self.pushButton.clicked.connect(self.close)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionSalir.triggered.connect(self.close)

        # creamos la subventana pero no la mostramos
        self.subventana = Subventana()
        # señal para abrir la subventana enviándole el texto del campo
        self.pushButton.clicked.connect(self.mostrar_subventana)

    def mostrar_subventana(self):
        # establecemos el texto de la ventana principal en la subventana
        self.subventana.label.setText(self.lineEdit.text())
        # y mostramos la subventana
        self.subventana.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
