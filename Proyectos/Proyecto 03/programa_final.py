import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # nos conectamos a la base de datos
        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("contactos.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        # creamos el modelo
        self.modelo = QSqlTableModel()
        self.modelo.setTable("contactos")
        self.modelo.select()
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Empleo")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Email")

        # configuramos la tabla
        self.tabla.setModel(self.modelo)
        self.tabla.resizeColumnsToContents()
        # escondemos la primera columna
        self.tabla.setColumnHidden(0, True)

        # tabla no editable directamente
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # selección de una única fila en lugar de celdas por defecto
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # señales
        self.tabla.selectionModel().selectionChanged.connect(self.seleccionar_fila)
        self.boton_modificar.clicked.connect(self.modificar_fila)
        self.boton_nuevo.clicked.connect(self.nueva_fila)
        self.boton_borrar.clicked.connect(self.borrar_fila)

        # fila inicial editable
        self.fila = -1

    def seleccionar_fila(self, seleccion):
        # la seleccion incluye todas las celdas de la fila, consultamos una
        if seleccion.indexes():
            self.fila = seleccion.indexes()[0].row()
            # recuperamos los valores del registro
            nombre = self.modelo.index(self.fila, 1).data()
            empleo = self.modelo.index(self.fila, 2).data()
            email = self.modelo.index(self.fila, 3).data()
            # establecemos los campos con los valores seleccionados
            self.line_nombre.setText(nombre)
            self.line_empleo.setText(empleo)
            self.line_email.setText(email)
        else:
            self.fila = -1

    def modificar_fila(self):
        if self.fila >= 0:
            # recuperamos el contenido de los lineEdit
            nombre = self.line_nombre.text()
            empleo = self.line_empleo.text()
            email = self.line_email.text()
            # actualizamos los registros del modelo
            self.modelo.setData(self.modelo.index(self.fila, 1), nombre)
            self.modelo.setData(self.modelo.index(self.fila, 2), empleo)
            self.modelo.setData(self.modelo.index(self.fila, 3), email)
            # confirmamos los cambios del modelo a la base de datos
            self.modelo.submit()

    def nueva_fila(self):
        # recuperamos el contenido de los lineEdit
        nombre = self.line_nombre.text()
        empleo = self.line_empleo.text()
        email = self.line_email.text()
        # si todos los campos tienen algo
        if len(nombre) > 0 and len(empleo) > 0 and len(email) > 0:
            # contamos las filas y añadimos una nueva
            nueva_fila = self.modelo.rowCount()
            self.modelo.insertRow(nueva_fila)
            # definimos los campos de la nueva fila
            self.modelo.setData(self.modelo.index(nueva_fila, 1), nombre)
            self.modelo.setData(self.modelo.index(nueva_fila, 2), empleo)
            self.modelo.setData(self.modelo.index(nueva_fila, 3), email)
            # confirmamos los cambios del modelo
            self.modelo.submit()
            # si queremos reseteamos los campos
            self.line_nombre.setText("")
            self.line_empleo.setText("")
            self.line_email.setText("")
            # y limpiamos la selección actual
            self.tabla.clearSelection()

    def borrar_fila(self):
        if self.fila >= 0:
            # borramos la fila
            self.modelo.removeRow(self.fila)
            # actualizamos la tabla para mostrarla sin el registro borrado
            self.modelo.select()
            # y establecemos la fila a -1
            self.fila = -1
            # si queremos resetear los campos
            self.line_nombre.setText("")
            self.line_empleo.setText("")
            self.line_email.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
