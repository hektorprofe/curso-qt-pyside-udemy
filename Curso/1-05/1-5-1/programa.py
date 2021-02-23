from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QDialogButtonBox)
import sys


class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Hola")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Diálogo de prueba"))

        botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)

        botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")

        layout.addWidget(botones)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = Dialogo()
        respuesta = dialogo.exec_()
        if respuesta:
            print("Diálogo aceptado")
        else:
            print("Diálogo denegado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
