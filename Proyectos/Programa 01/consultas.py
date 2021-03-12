import sys
from pathlib import Path
from PySide6.QtSql import QSqlDatabase, QSqlQuery


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


# Crea la conexión
conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))

# Abra la conexión
if not conexion.open():
    print("No se puede conectar a la base de datos")
    sys.exit(True)

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

# Ejecución de consultas dinámicas: formato de cadena
nombre, empleo, email = "Héctor", "Instructor", "hector@ejemplo.com"

consulta.exec_(f"""
    INSERT INTO contactos (nombre, empleo, email)
    VALUES ('{nombre}', '{empleo}', '{email}')""")

# Ejecución de consultas dinámicas: parámetros de marcador de posición
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

# Consultar registros
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


# Cerrar y eliminar conexiones de bases de datos
conexion.close()
print("Conexión abierta?", conexion.isOpen())
