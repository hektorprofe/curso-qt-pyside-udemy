from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar)
from PySide6.QtGui import QIcon, QAction
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.setWindowIcon(QIcon(absPath("icon.png")))
        self.setStatusBar(QStatusBar(self))
        self.construir_menu()

        self.construir_herramientas()

    def construir_herramientas(self):
        herramientas = QToolBar("Barra de herramientas")
        herramientas.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close)
        herramientas.addAction(self.accion_info)

        self.addToolBar(herramientas)

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

        self.accion_info = accion_info

    def mostrar_info(self):
        QMessageBox.about(self, "Información",
                                "Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
