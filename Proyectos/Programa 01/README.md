# Editor de registros SQL usando arquitectura Modelo-Vista

Documentación QtSQL: https://doc.qt.io/qtforpython/PySide6/QtSql/index.html

`consultas.py`

## Parte 1: Consultas a bases de datos con QtSql

## Conexión a la base de datos

```python
import sys
from pathlib import Path
from PySide6.QtSql import QSqlDatabase

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))
print(conexion.databaseName(), conexion.connectionName())
```

Drivers SQL: https://doc.qt.io/qt-6/sql-driver.html

## Apertura de la base de datos

```python
# Abra la conexión
if not conexion.open():
    print("No se puede conectar a la base de datos")
    sys.exit(True)
```

## Consultas SQL estáticas

```python
# Cree una consulta y ejecútela de inmediato usando .exec ()
consulta = QSqlQuery()
consulta.exec_("DROP TABLE IF EXISTS contactos")
consulta.exec_("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nombre VARCHAR(40) NOT NULL,
        empleo VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )""")
print(conexion.tables())
```

## Inserción simple

```python
nombre, empleo, email = "Héctor", "Instructor", "hector@ejemplo.com"

consulta.exec_(f"""
    INSERT INTO contactos (nombre, empleo, email)
    VALUES ('{nombre}', '{empleo}', '{email}')
""")
```

## Inserción múltiple

```python
datos = [
    ("Manuel", "Desarrollador Web", "manuel@example.com"),
    ("Lorena", "Gestora de proyectos", "lorena@example.com"),
    ("Javier", "Analista de datos", "javier@example.com"),
    ("Marta", "Experta en Python", "marta@example.com")
]

consulta = QSqlQuery()
consulta.prepare("""
    INSERT INTO contactos (nombre, empleo, email) VALUES (?, ?, ?)""")

# usamos .addBindValue () para insertar datos
for nombre, empleo, email in datos:
    consulta.addBindValue(nombre)
    consulta.addBindValue(empleo)
    consulta.addBindValue(email)
    consulta.exec_()
```

## Consulta de registros

```python
consulta.exec_("SELECT nombre, empleo, email FROM contactos")
# ponemos el cursor en el primer registro
if consulta.first():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))
# Automatizmaos el cursor hasta el final
while consulta.next():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))
```

## Cerrar la conexión

```python
conexion.close()
print("Conexión abierta?", conexion.isOpen())
```

# Parte 2: Edición en tabla usando arquitectura Modelo-Vista

https://doc.qt.io/qtforpython/PySide6/QtSql/QSqlTableModel.html
https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableView.html

`gestor.py`

```python
import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent)
        self.setWindowTitle("Ejemplo QTableView")
        self.resize(480, 320)

        # Creamos el modelo
        modelo = QSqlTableModel()
        modelo.setTable("contactos")
        modelo.select()

        # Creamos la vista
        vista = QTableView()
        vista.setModel(modelo)
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
```

Algunas opciones para afinar:

```python
# Nombre de las columnas
modelo.setHeaderData(0, Qt.Horizontal, "ID")
modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
modelo.setHeaderData(2, Qt.Horizontal, "Empleo")
modelo.setHeaderData(3, Qt.Horizontal, "Email")

# Establecer automáticamente el ancho
vista.resizeColumnsToContents()

# Esconder la primera columna para no duplicar los ID
vista.setColumnHidden(0, True)
```
