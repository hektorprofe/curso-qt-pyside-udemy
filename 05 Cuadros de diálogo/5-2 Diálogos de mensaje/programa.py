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
        # creamos un diálogo de mensaje con un título y un texto
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Título del diálogo")
        dialogo.setText("Esto es un diálogo de prueba")
        # añadimos unos botones y los traducimos
        dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialogo.button(QMessageBox.Ok).setText("Aceptar")
        dialogo.button(QMessageBox.Cancel).setText("Cancelar")
        # configuramos un icono
        dialogo.setIcon(QMessageBox.Question)

        # ejecutamos el diálogo y capturamos la respuesta
        respuesta = dialogo.exec_()
        # ahora debemos comprobar qué tipo de botón se ha clicado
        if respuesta == QMessageBox.Ok:
            print("Diálogo aceptado")
        else:
            print("Diálogo denegado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
