from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.construir_menu()

        # construimos las herramientas
        self.construir_herramientas()

    def construir_menu(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Menú")
        menu_archivo.addAction("&Prueba")
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
        menu_archivo.addSeparator()
        menu_archivo.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")
        menu_ayuda = menu.addMenu("Ay&uda")
        accion_info = QAction("&Información", self)
        accion_info.setIcon(QIcon(absPath("info.png")))
        accion_info.setShortcut("Ctrl+I")
        accion_info.triggered.connect(self.mostrar_info)
        accion_info.setStatusTip("Muestra información irrelevante")
        menu_ayuda.addAction(accion_info)
        self.setStatusBar(QStatusBar(self))

        # accesores de clase
        self.accion_info = accion_info

    def construir_herramientas(self):
        # Creamos una barra de herramientas
        herramientas = QToolBar("Barra de herramientas principal")
        # Podemos agregar la acción salir implícitamente
        herramientas.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close)
        # O añadir una acción ya creada para reutilizar código
        herramientas.addAction(self.accion_info)
        # La añadimos a la ventana principal
        self.addToolBar(herramientas)

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
