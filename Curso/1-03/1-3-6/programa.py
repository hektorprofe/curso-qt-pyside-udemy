from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        texto = QLineEdit()
        texto.setMaxLength(10)
        texto.setPlaceholderText("Escribe máximo 10 caracteres")
        texto.textChanged.connect(self.texto_cambiado)
        texto.returnPressed.connect(self.enter_presionado)

        self.setCentralWidget(texto)

    def texto_cambiado(self, texto):
        print("Texto cambiado:", texto)

    def enter_presionado(self):
        texto = self.centralWidget().text()
        print("Enter presionado, texto:", texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
