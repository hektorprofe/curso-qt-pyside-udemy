from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        # construimos nuestro menú
        self.construir_menu()

    def construir_menu(self):
        # Recuperamos la barra de menú
        menu = self.menuBar()

        # Añadimos un menú de archivo
        menu_archivo = menu.addMenu("&Menú")
        # Añadimos una acción de prueba
        menu_archivo.addAction("&Prueba")
        # Añadimos un submenú
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        # Añadimos una acción de prueba
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
        # Añadimos un separador
        menu_archivo.addSeparator()
        # Añadimos una acción completa
        menu_archivo.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")

        # Añadimos un menú de ayuda
        menu_ayuda = menu.addMenu("Ay&uda")
        # Creamos una acción específica para mostrar información
        accion_info = QAction("&Información", self)
        # Podemos configurar un icono en la acción
        accion_info.setIcon(QIcon(absPath("info.png")))
        # También podemos especificar un accesor
        accion_info.setShortcut("Ctrl+I")
        # Le configuramos una señal para ejecutar un método
        accion_info.triggered.connect(self.mostrar_info)
        # Añadimos un texto de ayuda
        accion_info.setStatusTip("Muestra información irrelevante")
        # Añadimos la acción al menú
        menu_ayuda.addAction(accion_info)

        # Añadimos una barra de estado
        self.setStatusBar(QStatusBar(self))

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
