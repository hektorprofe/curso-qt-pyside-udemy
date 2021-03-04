from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar, QLabel, QDockWidget)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.construir_menu()
        self.construir_herramientas()
        # añadimos los docks
        self.construir_docks()
        # creamos una caja como widget central de la ventana principal
        self.setCentralWidget(Caja("gray"))

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
        self.accion_info = accion_info

    def construir_herramientas(self):
        herramientas = QToolBar("Barra de herramientas principal")
        herramientas.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close)
        herramientas.addAction(self.accion_info)
        self.addToolBar(herramientas)

    def construir_docks(self):
        # creamos un dock
        dock1 = QDockWidget()
        # le damos un título (optativo)
        dock1.setWindowTitle("DOCK 1")
        # establecemos el widget que contendrá
        dock1.setWidget(Caja("green"))
        # algunas características
        dock1.setFeatures(
            QDockWidget.NoDockWidgetFeatures | QDockWidget.DockWidgetFloatable |
            QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable)
        # tamaño mínimo (optativo)
        dock1.setMinimumWidth(125)
        dock1.setMinimumHeight(100)
        dock1.setMinimumSize(125, 100)
        # lo añadimos en una posición de la ventana principal
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        # creamos más docks para jugar con ellos
        dock2 = QDockWidget()
        dock2.setWindowTitle("DOCK 2")
        dock2.setWidget(Caja("yellow"))
        dock2.setMinimumSize(125, 100)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        dock3 = QDockWidget()
        dock3.setWindowTitle("DOCK 3")
        dock3.setWidget(Caja("blue"))
        dock3.setMinimumSize(125, 100)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
