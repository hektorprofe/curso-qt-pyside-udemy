import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #     with open(absPath("contactos.json")) as fichero:
    #         self.datos = json.load(fichero)

    #     self.columnas = ["nombre", "empleo", "email"]

    #     self.tabla.setRowCount(len(self.datos))
    #     self.tabla.setColumnCount(len(self.columnas))
    #     self.tabla.setHorizontalHeaderLabels(self.columnas)

    #     for i, fila in enumerate(self.datos):
    #         for j, columna in enumerate(self.columnas):
    #             item = QTableWidgetItem()
    #             item.setData(Qt.EditRole, fila[columna])
    #             self.tabla.setItem(i, j, item)

    #     self.tabla.resizeColumnsToContents()
    #     self.tabla.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
    #     self.tabla.setHorizontalHeaderItem(1, QTableWidgetItem("Empleo"))
    #     self.tabla.setHorizontalHeaderItem(2, QTableWidgetItem("Email"))

    #     self.tabla.itemChanged.connect(self.celda_modificada)

    # def celda_modificada(self, item):
    #     fila, campo = item.row(), self.columnas[item.column()]
    #     self.datos[fila][campo] = item.data(Qt.EditRole)
    #     with open(absPath("contactos.json"), "w") as fichero:
    #         json.dump(self.datos, fichero)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
