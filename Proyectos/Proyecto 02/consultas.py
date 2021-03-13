import sys
from helpers import absPath
from PySide6.QtSql import QSqlDatabase, QSqlQuery


# Crea la conexión
conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))

# Abra la conexión
if not conexion.open():
    print("No se puede conectar a la base de datos")
    sys.exit(True)
else:
    print("¿Conexión establecida?", conexion.isOpen())

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
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

consulta = QSqlQuery()
consulta.prepare("""
    INSERT INTO contactos (nombre, empleo, email) VALUES (?, ?, ?)""")

# usamos .addBindValue () para insertar datos
for nombre, empleo, email in contactos:
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


# Cerrar conexión a la base de datos
conexion.close()
print("¿Conexión cerrada?", not conexion.isOpen())
