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

        # cargamos el contenido del fichero
        with open(absPath("contactos.json")) as fichero:
            self.datos = json.load(fichero)

        # definimos la configuración de las columnas (claves del json)
        self.columnas = ["nombre", "empleo", "email"]

        # configuramos la tabla a partir de la información recuperada
        self.tabla.setRowCount(len(self.datos))
        # establecemos la longitud de las columnas
        self.tabla.setColumnCount(len(self.columnas))
        # establecemos las cabeceras de las columnas
        self.tabla.setHorizontalHeaderLabels(self.columnas)

        # dibujamos la tabla y los botones
        for i, fila in enumerate(self.datos):
            for j, columna in enumerate(self.columnas):
                item = QTableWidgetItem()
                # Con Qt.EditRole se establece el tipo de campo automáticamente
                item.setData(Qt.EditRole, fila[columna])
                self.tabla.setItem(i, j, item)

        # personalizamos y redimensionamos la tabla
        self.tabla.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
        self.tabla.setHorizontalHeaderItem(1, QTableWidgetItem("Empleo"))
        self.tabla.setHorizontalHeaderItem(2, QTableWidgetItem("Email"))
        self.tabla.resizeColumnsToContents()

        # configuramos las señales
        self.tabla.itemChanged.connect(self.celda_modificada)

    def celda_modificada(self, celda):
        # recuperamos la fila y la clave de la columna del item seleccionado
        fila, columna = celda.row(), self.columnas[celda.column()]
        # modificamos el mismo lugar del dataframe recuperando el dato con tipo
        self.datos[fila][columna] = celda.data(Qt.EditRole)
        # guardamos el fichero
        self.guardar_json()

    def guardar_json(self):
        with open(absPath("contactos.json"), "w") as fichero:
            json.dump(self.datos, fichero)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
