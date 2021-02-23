from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# Creamos una aplicación para gestionar la interfaz
app = QApplication(sys.argv)

# Ahora la ventana la gestiona el widget de ventana principal
window = QMainWindow()

# Damos un título al programa
window.setWindowTitle("Hola mundo")

# Guardamos el botón en una variable
button = QPushButton("Soy un botón")

# Establecemos el botón como widget central de la ventana principal
window.setCentralWidget(button)

# Mostramos la ventana, se encuentra oculta por defecto
window.show()

# Iniciamos el bucle del programa
sys.exit(app.exec_())
