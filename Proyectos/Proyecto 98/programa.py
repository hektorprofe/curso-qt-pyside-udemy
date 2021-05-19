import sys
from PySide6 import QtWidgets, QtSql, QtCore, QtGui
from helpers import absPath
from ui_tabla import Ui_MainWindow
from functools import partial

# Buscador con filtros en vivo de registros SQL en TableView


class NumericDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, tipo, parent=None):
        super().__init__(parent)
        self.tipo = tipo

    def createEditor(self, parent, option, index):
        if self.tipo == "Entero":
            return QtWidgets.QSpinBox(parent, maximum=9999999)
        elif self.tipo == "Flotante":
            return QtWidgets.QDoubleSpinBox(parent, singleStep=0.01)


class ComboboxDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, opciones, ancho, parent=None):
        super().__init__(parent)
        self.opciones = opciones
        self.ancho = ancho

    # Creación de la estructura base del widget (sin establecer nada)
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        for opcion in self.opciones:
            editor.addItem(opcion['texto'], opcion['id'])
        return editor

    # Dibujar permanentemente
    def paint(self, painter, option, index):
        # Trabajamos a partir del id de la base de datos oculto en el combobox
        opcion_id = index.data()
        for opcion in self.opciones:
            if opcion["id"] == opcion_id:
                option.text = opcion["texto"]
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ItemViewItem, option, painter)

    # Redimensionamos la anchura del campo
    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        size.setWidth(self.ancho)
        return size

    # Valor por defecto en el editor (al hacer doble clic en el desplegable)
    def setEditorData(self, editor, index):
        # Trabajamos a partir del id de la base de datos oculto en el combobox
        opcion_id = index.data()
        for opcion in self.opciones:
            if opcion["id"] == opcion_id:
                # Aquí modificamos el índice de visualización del combobox
                for i in range(editor.count()):
                    if editor.itemText(i) == opcion["texto"]:
                        editor.setCurrentIndex(i)

    # Establecer en modelo
    def setModelData(self, editor, model, index):
        # Trabajamos a partir del texto mostrado en el combobox
        opcion_texto = editor.currentText()
        for opcion in self.opciones:
            if opcion["texto"] == opcion_texto:
                # actualizamos el modelo con el id de la base de datos
                model.setData(index, opcion["id"])
                # Aquí modificamos el índice de visualización del combobox
                for i in range(editor.count()):
                    if editor.itemText(i) == opcion_texto:
                        editor.setCurrentIndex(i)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(620, 480)

        # Conexión a la base de datos
        conexion = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("chinook.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        # Configuración del modelo
        self.modeloTabla = QtSql.QSqlTableModel()
        self.modeloTabla.setTable("Track")
        self.modeloTabla.select()

        # Enlazamos el modelo a la vista de la tabla
        self.vistaTabla.setModel(self.modeloTabla)

        # Almacenamos todas las columnas y escondemos las no deseadas
        cabeceras = []
        for i in range(self.modeloTabla.columnCount()):
            cabeceras.append(self.modeloTabla.headerData(i, QtCore.Qt.Horizontal))
            # Escondemos las que no nos interesan
            if cabeceras[-1] in ["TrackId", "AlbumId", "MediaTypeId", "Composer", "Bytes"]:
                self.vistaTabla.setColumnHidden(i, True)

        # Delegamos los campos numéricos
        self.vistaTabla.setItemDelegateForColumn(cabeceras.index("Milliseconds"), NumericDelegate("Entero", self))
        self.vistaTabla.setItemDelegateForColumn(cabeceras.index("UnitPrice"), NumericDelegate("Flotante", self))

        # Personalizamos el nombre de las cabeceras (optativo)
        self.modeloTabla.setHeaderData(cabeceras.index("Name"), QtCore.Qt.Horizontal, "Título")
        self.modeloTabla.setHeaderData(cabeceras.index("GenreId"), QtCore.Qt.Horizontal, "Género")
        self.modeloTabla.setHeaderData(cabeceras.index("Milliseconds"), QtCore.Qt.Horizontal, "Duración")
        self.modeloTabla.setHeaderData(cabeceras.index("UnitPrice"), QtCore.Qt.Horizontal, "Precio")

        # Creamos los datos dinámicos para los desplegables
        consulta = QtSql.QSqlQuery()
        self.generos = []
        consulta.exec_("SELECT GenreId, Name from Genre ORDER BY Name")
        while consulta.next():
            self.generos.append({'id': consulta.value("GenreId"), 'texto': consulta.value("Name")})

        # Creamos los datos para los desplegables de filtros
        self.comboBox.addItem("Todos", None)
        for item in self.generos:
            self.comboBox.addItem(item['texto'], item['id'])

        # Delegamos los desplegables de género y álbum
        self.vistaTabla.setItemDelegateForColumn(cabeceras.index("GenreId"), ComboboxDelegate(self.generos, 125, self))

        # Redimensionamos, activamos ordenamiento y ordenamos por defecto
        self.vistaTabla.resizeColumnsToContents()
        self.vistaTabla.setSortingEnabled(True)
        self.vistaTabla.sortByColumn(1, QtCore.Qt.AscendingOrder)

        # Finalmente configuramos las señales
        self.lineEdit.textChanged.connect(self.buscarTitulo)
        self.comboBox.currentTextChanged.connect(self.filtrarGenero)
        self.pushButton.clicked.connect(self.limpiarTodo)

    def buscarTitulo(self):
        # Reiniciamos los filtros y aplicamos la búsqueda
        self.modeloTabla.setFilter(None)
        titulo = self.lineEdit.text()
        self.modeloTabla.setFilter(f"Name like '%%{titulo}%%'")

    def buscarAutor(self):
        # Reiniciamos los filtros y aplicamos la búsqueda
        self.modeloTabla.setFilter(None)
        autor = self.lineEdit_2.text()
        self.modeloTabla.setFilter(f"Composer like '%%{autor}%%'")

    def filtrarGenero(self):
        # Reiniciamos los filtros
        self.modeloTabla.setFilter(None)
        # diferenciamos tres cosas en el combobox
        print(self.comboBox.currentIndex(), self.comboBox.currentText(), self.comboBox.currentData())
        # la que nos interesa es el índice en la base de datos
        generoId = self.comboBox.currentData()
        if generoId:
            # filtramos por la id del genero
            self.modeloTabla.setFilter(f"GenreId == {generoId}")

    def limpiarTodo(self):
        self.modeloTabla.setFilter(None)
        self.lineEdit.setText(None)
        self.comboBox.setCurrentIndex(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
