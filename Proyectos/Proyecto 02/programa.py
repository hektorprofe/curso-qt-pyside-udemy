import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # conexion = QSqlDatabase.addDatabase("QSQLITE")
        # conexion.setDatabaseName(absPath("Contactos.db"))
        # if not conexion.open():
        #     print("No se puede conectar a la base de datos")
        #     sys.exit(True)

        # modelo = QSqlTableModel()
        # modelo.setTable("contactos")
        # modelo.select()

        # modelo.setHeaderData(0, Qt.Horizontal, "Id")
        # modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        # modelo.setHeaderData(2, Qt.Horizontal, "Empleo")
        # modelo.setHeaderData(3, Qt.Horizontal, "Email")

        # self.tabla.setModel(modelo)
        # self.tabla.setColumnHidden(0, True)
        # self.tabla.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
