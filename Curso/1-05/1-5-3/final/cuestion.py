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
        # creamos un diálogo de tipo cuestión
        dialogo = QMessageBox.question(
            self, "Diálogo de cuestión", "Esta es una pregunta de prueba")

        # ahora debemos comprobar qué tipo de botón se devuelve
        if dialogo == QMessageBox.Yes:
            print("Sí")
        else:
            print("No")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
