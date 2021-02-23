from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Hola mundo")
boton = QPushButton("Soy un botón")

window.setCentralWidget(boton)

window.show()
sys.exit(app.exec_())
