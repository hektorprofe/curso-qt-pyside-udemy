from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox, QAbstractItemView, QHBoxLayout)
from PySide6.QtCore import Qt
from pathlib import Path
import pandas as pd


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("Editor de registros")
        self.setLayout(QVBoxLayout())

        # Creamos una tabla y la añadimos al layout
        self.tabla = QTableWidget(2, 2)
        self.layout().addWidget(self.tabla)

        try:
            # dataframe cargado desde el fichero json
            self.datos = pd.read_json(absPath('datos.json'), orient="table")
        except:
            # si ocurre algún error generamos una estructura base
            self.datos = pd.DataFrame(
                data=[['Nombre', 0, 0.0]], dtype="object",
                columns=["Nombre", "Edad", "Nota"])

        # Configuramos la tabla a partir de la información del dataframe
        self.tabla.setRowCount(self.datos.shape[0])
        self.tabla.setColumnCount(self.datos.shape[1])
        self.tabla.setHorizontalHeaderLabels(self.datos.columns)

        # Configuramos la selección de una única celda a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # dibujamos la tabla y los botones
        self.dibujar_tabla()
        self.dibujar_botones()

        # configuramos las señales
        self.tabla.itemChanged.connect(self.evento_item_modificado)

    def guardar_json(self):
        try:
            # guardamos sin índices en la primera columna pues no los usamos
            self.datos.to_json(
                absPath('datos.json'), orient="table", index=False)
            QMessageBox.information(
                self, "Guardado", "JSON guardado correctamente")
        except:
            QMessageBox.critical(
                self, "Error", "No se ha podido guardar el fichero")

    def evento_item_modificado(self, item):
        # recuperamos la fila y columna del item seleccionado
        fila, columna = item.row(), item.column()
        # modificamos el mismo lugar del dataframe recuperando el dato con tipo
        self.datos.iat[fila, columna] = item.data(Qt.EditRole)

    def dibujar_botones(self):
        # creamos un layout horizontal para distribuir los botones
        botones = QHBoxLayout()
        self.layout().addLayout(botones)

        boton_guardar = QPushButton("Guardar")
        boton_guardar.clicked.connect(self.guardar_json)
        botones.addWidget(boton_guardar)

        boton_borrar = QPushButton("Borrar")
        boton_borrar.clicked.connect(self.registro_borrar)
        botones.addWidget(boton_borrar)

        boton_nuevo = QPushButton("Nuevo")
        boton_nuevo.clicked.connect(self.registro_nuevo)
        botones.addWidget(boton_nuevo)

    def registro_nuevo(self):
        if len(self.datos) == 0:
            # Si no hay ningún dato debemos recrear la estructura del dataframe
            self.datos = pd.DataFrame(
                data=[['Nombre', 0, 0.0]], dtype="object",
                columns=["Nombre", "Edad", "Nota"])
        else:
            # caso contrario añadimos el registro a la nueva fila del dataframe
            self.datos.loc[len(self.datos)] = ['Nombre', 0, 0.0]

        # Recalculamos el tamaño de la tabla a partir del dataframe
        self.tabla.setRowCount(len(self.datos))
        # Dibujamos la tabla de nuevo
        self.dibujar_tabla()

    def registro_borrar(self):
        seleccion = self.tabla.selectedIndexes()
        if len(seleccion) > 0:
            fila = seleccion[0].row()

            # confirmamos si el usuario quiere borrar el registro
            confirmacion = QMessageBox.question(
                self, "", f"¿Borrar [{fila+1}] {self.datos.iat[fila, 0]}?")

            if confirmacion == QMessageBox.Yes:
                # borramos la fila, in_place lo hace en el propio dataframe
                self.datos.drop(fila, inplace=True)
                # actualizamos los índices del dataframe después del borrado
                self.datos.reset_index(drop=True, inplace=True)
                # Recalculamos el tamaño de la tabla a partir del dataframe
                self.tabla.setRowCount(len(self.datos))
                # volvemos a dibujar la tabla
                self.dibujar_tabla()

    def dibujar_tabla(self):
        for fila in range(self.datos.shape[0]):
            for columna in range(self.datos.shape[1]):
                item = QTableWidgetItem()
                item.setData(Qt.EditRole, self.datos.iat[fila, columna])
                self.tabla.setItem(fila, columna, item)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()
