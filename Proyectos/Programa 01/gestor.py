import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ejemplo QTableView")
        self.resize(480, 320)

        # Creamos el modelo
        modelo = QSqlTableModel()
        modelo.setTable("contactos")
        modelo.select()

        modelo.setHeaderData(0, Qt.Horizontal, "ID")
        modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        modelo.setHeaderData(2, Qt.Horizontal, "Empleo")
        modelo.setHeaderData(3, Qt.Horizontal, "Email")

        # Creamos la vista
        vista = QTableView()
        vista.setModel(modelo)
        vista.resizeColumnsToContents()
        vista.setColumnHidden(0, True)

        self.setCentralWidget(vista)


def crearConexion():
    # Conexión a la base de datos
    conexion = QSqlDatabase.addDatabase("QSQLITE")
    conexion.setDatabaseName(absPath("contactos.db"))
    if not conexion.open():
        print("No se puede conectar a la base de datos")
        sys.exit(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    crearConexion()
    window = MainWindow()
    window.show()
    app.exec_()
