from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):

    """
    Creamos nuestra propia clase MainWindow heredando de QMainWindow
    """

    # Creamos la ventana en el constructor a partir de una QMainWindow
    def __init__(self):

        # Con super ejecutamos su propio constructor
        # Así se crea la ventana en su propia instancia self
        super().__init__()

        # Damos un título al programa
        self.setWindowTitle("Hola mundo")

        # Guardamos el botón en una variable
        button = QPushButton("Hola")

        # Establecemos el botón como widget central de la ventana principal
        self.setCentralWidget(button)


# Si ejecutamos el propio script como programa principal
if __name__ == "__main__":
    # Creamos la aplicación
    app = QApplication(sys.argv)
    # Creamos nuestra ventana principal
    window = MainWindow()
    # Mostramos la ventana
    window.show()
    # Iniciamos el bucle del programa
    sys.exit(app.exec_())
