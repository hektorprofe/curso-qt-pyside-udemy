from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Título de ejemplo")
        dialogo.setText("Esto es un diálogo de prueba")

        dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialogo.button(QMessageBox.Ok).setText("Aceptar")
        dialogo.button(QMessageBox.Cancel).setText("Cancelar")

        dialogo.setIcon(QMessageBox.Question)

        respuesta = dialogo.exec_()
        if respuesta == QMessageBox.Ok:
            print("Diálogo aceptado")
        else:
            print("Diálogo denegado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
