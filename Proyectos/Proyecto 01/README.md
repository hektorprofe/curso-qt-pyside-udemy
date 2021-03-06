# Proyecto: Editor de registros en ficheros JSON con Pandas y QTableWidget

La meta de este proyecto es cargar los datos de un fichero en una tabla, poder modificarlos, añadir de nuevos o borrarlos y guardarlos de nuevo en el fichero. Para conseguirlo vamos a trabajar con los `DataFrames` del módulo Pandas y el componente `QTableWidget`.

## Estructura base

```python
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget)
from PySide6.QtCore import Qt
from pathlib import Path

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

if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()
```

## DataFrame

Los dataframes son las estructuras de datos gestionadas por el módulo Pandas, vamos a aprovechar su potencial para manejar los datos para rellenar nuestra tabla:

Para instalar pandas:

```bash
pip install pandas
```

Ahora creamos un `dataframe`:

```python
import pandas as pd

# Creamos un dataframe de pandas para almacenar una tabla
self.datos = pd.DataFrame(
    data=[
        ["Juan", 17, 6.3],
        ["María", 45, 8.2],
        ["Ana", 36, 9.6],
        ["Fernando", 25, 4.8]
    ],
    columns=["Nombre", "Edad", "Nota"]
)

print(self.datos)
```

Establecemos el tamaño de la tabla a partir de la forma del `DataFrame`, que devuelve las filas y columnas. También podemos establecer el título de las columnas:

```python
# Configuramos la tabla a partir de la información del dataframe
self.tabla.setRowCount(self.datos.shape[0])
self.tabla.setColumnCount(self.datos.shape[1])
self.tabla.setHorizontalHeaderLabels(self.datos.columns)
```

Ahora vamos a extraer la información del dataframe y la añadiremos a la tabla. Buscaremos el valor de un índice y lo añadiremos a la celda utilizando un objeto `QTableWidgetItem`:

```python
from PySide6.QtWidgets import QTableWidgetItem

# Añadimos la primera columna primera fila
item = QTableWidgetItem(self.datos.iat[0, 0])
self.tabla.setItem(0, 0, item)
```

Por defecto se establecen los campos como textos, pero si queremos añadir un valor de un tipo distinto tenemos que utilizar el método `setData` con la flag `EditRole` y el valor. Eso detectará automáticamente el tipo e incluso nos permitirá manejar el campo como un widget especial:

```python
from PySide6.QtCore import Qt

item = QTableWidgetItem()
item.setData(Qt.EditRole, self.datos.iat[0, 1])
self.tabla.setItem(0, 1, item)
```

Por defecto los datos de los dataframes son especiales del módulo `numpy` y `Qt` no es capaz de reconocerlos. Por suerte podemos pedirle a `Pandas` que utilice las clases básicas usando el campo `dtype` al crear el dataframe e indicándole el tipo para objetos básicos:

```python
dtype="object"
```

Con esto ya lo tenemos y podemos también añadir el campo decimal con la nota:

```python
item = QTableWidgetItem()
item.setData(Qt.EditRole, self.datos.iat[0, 1])
self.tabla.setItem(0, 1, item)

item = QTableWidgetItem()
item.setData(Qt.EditRole, self.datos.iat[0, 2])
self.tabla.setItem(0, 2, item)
```

¿Os habéis fijado que estamos repitiendo el mismo patrón para cada columna? Podemos recorrer dinámicamente el dataframe utilizando dos bucles `for` para automatizar el proceso:

```python
for fila in range(self.datos.shape[0]):
    for columna in range(self.datos.shape[1]):
        item = QTableWidgetItem()
        item.setData(Qt.EditRole, self.datos.iat[fila, columna])
        self.tabla.setItem(fila, columna, item)
```

## Guardardo y carga en fichero JSON

Lo mejor de todo viene ahora y es que Pandas nos permite guardar y recuperar `dataframes` de ficheros muy cómodamente. Vamos a guardar el nuestro en un fichero JSON, para ello empezaremos creando un botón en el layout:

```python
from PySide6.QtWidgets import QPushButton

boton_guardar = QPushButton("Guardar")
boton_guardar.clicked.connect(self.guardar_json)
self.layout().addWidget(boton_guardar)
```

Ahora vamos a hacer accesible el `dataframe` a nivel de clase para usar su método `to_json` y guardarlo en el disco duro. Además podemos mostrar unos mensajes con `QMessageBox`:

```python

from PySide6.QtWidgets import QMessageBox

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
```

Una vez tenemos el fichero JSON creado podemos cargar sus datos en lugar de escribirlos manualmente, o si hay algún fallo generar una estructura con una plantilla base:

```python
try:
    # dataframe cargado desde el fichero json
    self.datos = pd.read_json(absPath('datos.json'), orient="table")
except:
    # si ocurre algún error generamos una estructura base
    self.datos = pd.DataFrame(
        data=[['Nombre', 0, 0.0]], dtype="object",
        columns=["Nombre", "Edad", "Nota"])
```

¿Fácil verdad?

## Modificando los datos

Ahora viene el kit de la cuestión, modificar las celdas de la tabla y hacer que esos cambios se actualicen en el fichero.

Nuestro sistema funciona utilizando como base el `dataframe`, así que lo que vamos a hacer es intentar modificar el dataframe al modificar una celda. Digamos que reflejaremos los cambios en él. Para ello necesitamos saber si una celda se modifica, algo que podemos conseguir con la señal `itemChanged` de la tabla:

```python
# señales al final del constuctor
self.tabla.itemChanged.connect(self.evento_item_modificado)

def evento_item_modificado(self, item):
    print(item.text())
```

El objeto item contiene la referencia a la fila y columna del dato, que podemos usar para acceder al `dataframe` y modificarlo. Tendremos que establecerlo mediante el método `data` pasando la flag `Qt.EditRole`:

```python
def evento_item_modificado(self, item):
    # recuperamos la fila y columna del item seleccionado
    fila, columna = item.row(), item.column()
    # modificamos el mismo lugar del dataframe recuperando el dato con tipo
    self.datos.iat[fila, columna] = item.data(Qt.EditRole)
```

Con esto ya podemos editar los campos, estos se guardan en el dataframe y luego se escriben en el fichero perfectamente.

## Añadir registros

Para añadir un nuevo registro podemos presionar un botón `Nuevo registro`, esto generará una nueva fila en el `DataFrame` con unos datos de ejemplo:

```python
boton_nuevo = QPushButton("Nuevo")
boton_nuevo.clicked.connect(self.registro_nuevo)
self.layout().addWidget(boton_nuevo)
```

Ya que estamos empezando a tener varios botones podemos llevarnos estos códigos a un método `dibujar_botones` y añadirlos en un layout horizontal:

```python
from PySide6.QtWidgets import QHBoxLayout

self.dibujar_botones()  # new

def dibujar_botones(self):
    # creamos un layout horizontal para distribuir los botones
    botones = QHBoxLayout()
    self.layout().addLayout(botones)

    boton_nuevo = QPushButton("Nuevo")
    boton_nuevo.clicked.connect(self.registro_nuevo)
    botones.addWidget(boton_nuevo)

    boton_guardar = QPushButton("Guardar")
    boton_guardar.clicked.connect(self.guardar_json)
    botones.addWidget(boton_guardar)
```

Debemos tener en cuenta que si modificamos el `dataframe` hay que actualizar la tabla para reflejar los cambios. Como la función de dibujar la tabla la reutilizamos podemos crear un método común:

```python
self.dibujar_tabla()  # new
self.dibujar_botones()

def registro_nuevo(self):
    # Añadimos el registro en una nueva fila del dataframe
    self.datos.loc[len(self.datos)] = ['Nombre', 0, 0.0]
    # Recalculamos el tamaño de la tabla a partir del dataframe
    self.tabla.setRowCount(len(self.datos))
    # Dibujamos toda la información de nuevo (menos óptimo, más sencillo)
    self.dibujar_tabla()

def dibujar_tabla(self):
    for fila in range(self.datos.shape[0]):
        for columna in range(self.datos.shape[1]):
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, self.datos.iat[fila, columna])
            self.tabla.setItem(fila, columna, item)
```

## Borrar registros

Por último, para borrar un registro podemos hacerlo a partir de la celda seleccionada comprobando el índice de la fila y borrando esa fila del dataframe.

Por defecto la tablas permiten seleccionar más de una celda en varias filas, vamos a limitar la selección a una única fila usando una `flag` de configuración:

```python
from PySide6.QtWidgets import QAbstractItemView

# Configuramos la selección de una única celda a la vez
self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
```

Para consultar la celda seleccionada utilizaremos el método `selectedIndexes` de la tabla, que devuelve una lista. Si hay más de un elemento es que estamos seleccionando una celda, así que analizaremos el índice de la fila:

```python
def dibujar_botones(self):
    boton_borrar = QPushButton("Borrar")
    boton_borrar.clicked.connect(self.registro_borrar)
    botones.addWidget(boton_borrar)

def registro_borrar(self):
    seleccion = self.tabla.selectedIndexes()
    if len(seleccion) > 0:
        fila = seleccion[0].row()
        print("Fila", fila)
```

Este es el índice que tenemos que eliminar del `dataframe`, vamos a hacerlo después de pedir una confirmación:

```python
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
            self.tabla.setRowCount(self.datos.shape[0])
            # volvemos a dibujar la tabla
            self.dibujar_tabla()
```

Con esto ya tenemos acabado el proyecto, solo falta arreglar un pequeño bug que sucede si borramos todos los registros e intentemos añadir uno.

Cuando eso pasa el `dataframe` pierde su estructura así que debemos crearla de nuevo, en caso contrario podemos añadir de forma normal el nuevo registro:

```python
def registro_nuevo(self):
    if len(self.datos) == 0:
        # Si no hay ningún dato debemos recrear la estructura del dataframe
        self.datos = pd.DataFrame(
            data=[['Nombre', 0, 0.0]], dtype="object",
            columns=["Nombre", "Edad", "Nota"])
    else:
        # caso contrario añadimos el registro a la nueva fila del dataframe
        self.datos.loc[len(self.datos)] = ['Nombre', 0, 0.0]

    self.tabla.setRowCount(len(self.datos))
    self.dibujar_tabla()
```

Y con esto hemos acabado el proyecto.

Solo comentar que existe otra forma de gestionar las tablas mediantes vistas y modelos que proveen algunas funcionalidades interesantes, seguro que los utilizaremos en algún momento.
