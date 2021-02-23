from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QLabel, QVBoxLayout,
    QDialog, QDialogButtonBox)
import sys


class Dialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hola")
        self.resize(240, 120)

        # creamos un layout y lo establecemos en el widget
        layout = QVBoxLayout()
        self.setLayout(layout)

        # podemos añadir una etiqueta
        layout.addWidget(QLabel("Diálogo de prueba"))

        # creamos unos botones predeterminados
        botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # configuramos las señales predeterminadas
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)

        # traducción en tiempo real de los botones
        botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")

        # y los añadimos al layout
        layout.addWidget(botones)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = Dialogo(self)
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
