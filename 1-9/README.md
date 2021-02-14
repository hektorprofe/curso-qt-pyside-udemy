# 1.9 Interfaces clásicas con QtDesigner

- 1.9.1 Nuestro primer diseño
- 1.9.2 Compilación y uso de diseños con recursos
- 1.9.3 Añadiendo la programación al diseño
- 1.9.4 Manejo de subventanas compiladas

En esta unidad se da por hecho que se tiene en el path el designer, rcc y uic.

## 1.9.1 Nuestro primer diseño (layout, elementos, tamaños, expandir, recursos, experimentar...)

Muy bien, pues vamos a diseñar nuestra primera interfaz. Si tenemos el directorio de PySide6 en el PATH del sistema podemos abrir el programa escribiendo:

```bash
designer
```

### Primer formulario

Lo primero es seleccionar qué tipo de formulario crear, vamos a crear una ventana principal `Main Window`.

- En el centro tenemos la vista de diseño con la ventana principal.
- A la izquierda tenemos la caja de Widgets.
- Arriba el control de elementos y disposiciones.
- A la derecha encontramos de arriba a abajo:
  - El inspector de objetos en una vista jerárquica.
  - El editor de propiedades del componente seleccionado.
  - Y el navegador de recursos del programa.

### Personalizar la ventana

Vamos a empezar a personalizar la ventana usando algunas propiedades:

- `geometry`: 480 ancho y 320 alto
- `windowTitle`: Primer diseño

Ahora vamos a crear un conjunto de recursos para utilizarlos en el programa.

- Hacemos clic en el `lápiz` del navegador de recursos.
- En la columna izquierda clic derecho > `Nuevo`.
- En el directorio de la aplicación guardamos el fichero con el nombre `recursos`.
- Con `recursos.qrc` seleccionado, clic derecho en la columna derecha > Nuevo prefijo.
- Le damos por ejemplo el nombre `iconos`, clic derecho `Añadir archivos`.
- Buscamos un icono png para ponerlo en nuestra ventan, lo añadimos y aceptamos.

<img src="docs/01.png">

- `windowIcon`: Desplegamos, "Elija recurso" y seleccionamos el icono.

* Guardamos el diseño `Control+S` con nombre `mainwindow.ui` en un directorio llamado, por ejemplo `interfaces`.

- Presionamos `Control+R` para ver una previsualización de la ventana principal.

### Componentes y disposiciones

Vamos a añadir algunos elementos:

- `Label`: Introduce un texto
- `LineEdit`
- `PushButton`: Enviar

Veréis que no quedan muy bien dispuestos, eso es porque nuestra ventana no tiene un layout establecido.

<img src="docs/02.png">

Con la ventana seleccionada hacemos clic en el layout vertical de la barra superior, automáticamente los elementos se posicionarán siguiendo esta disposición:

<img src="docs/03.png">

Automáticamente se creará un dummy widget con un layout para el `centralWidget` y los componentes se posicionarán automáticamente. Además ahora encontraremos un nuevo apartado `Layout`en las propiedades del objeto `centralWidget` donde podemos cambiar su configuración.

Sin embargo veréis que nuestros elementos se posicionan raro porque la etiqueta se expande por defecto.

Para solucionar esto vamos a añadir abajo del todo un widget `Vertical Spacer`:

<img src="docs/04.png">

Como podéis suponer los `Spacers` rellenan automáticamente el espacio sobrante de un layout.

Podemos probar otras disposiciones hasta encontrar una que nos guste y utilizar el botón `Ajuste de tamaño` para redimensionar el tamaño de la ventana acordemente a su contenido:

<img src="docs/05.png">

Otra cosa importante es que las ventanas principales vienen con su `menuBar` y `statusBar` ya creadas.

Podemos agregar campos al menú superior simplemente escribiendo ahí. Luego podemos gestionar las acciones mediante el inspector de objetos y de propiedades. Cualquier cosa que debáis configurar de un widget la encontraréis ahí, por ejemplo podemos añadir un acceso directo al botón de &Salir del menú:

<img src="docs/06.png">

Y añadir una imagen al botón de salir, siempre que préviamente la añadamos a nuestros recursos:

<img src="docs/07.png">

Si añadimos `statusTips` a nuestros componentes, se mostrarán automáticamente en el previsualizador:

<img src="docs/08.png">

También podemos cambiar los estilos del programa haciendo clic derecho en el objeto `MainWindow` del inspector y con la opción `Cambiar Hoja de Estilos`.

Se abrirá un formulario donde podemos pegar todo el contenido de nuestro fichero QSS tradicional:

<img src="docs/09.png">

Y creo que ya hemos visto todos los conceptos clave. Sí que haremos algunos diseños de proramas en el segundo bloque del curso, pero el mejor maestro es la práctica. Os aconsejo perderos un rato probando layouts, widgets y cambiando sus propiedades para aprender por vuestra cuenta.

En la próxima lección vamos a transformar este diseño en un fichero Python donde podremos programar en él.

## 1.9.2 Compilación y uso de diseños con recursos

Para importar nuestros diseños en Python debemos transformarlos a código Python, eso se consigue compilando los diseños.

Para este fin se requiere de un programa intermediario de la Suite Qt llamado `uic`: User Interface Compiler.

Si añadimos el directorio de `PySide6` al path deberíamos poder acceder a él desde la terminal:

```bash
uic -h
```

El comando para compilar un diseño es:

```bash
cd 1-9-1/interfaces
uic.exe -g python mainwindow.ui -o mainwindow.py
```

Así habremos generado un fichero `python` dentro de la carpeta interfaces. Si lo analizamos encontraremos varias importaciones y todo el código para generar la ventana:

```python
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import recursos_rc
```

Quiero que os fijéis en la línea `import recursos_rc`. Esta línea es la que va a cargar los recursos compilados del diseño. Esos recursos deberán estar en el módulo `recursos_rc` de la propia carpeta, así que necesitamos crearlos.

Compilar los recursos es un proceso calcado a compilar los diseños, pero esta vez se utiliza otra herramienta de Qt llamada `rcc`: Resource Compiler.

El comando para compilar los recursos es:

```bash
cd 1-9-1
rcc.exe -g python -o recursos_rc.py recursos.qrc  # mismo directorio
```

Esto tomará el fichero `recursos.qrc` que habíamos creado en `Qt Designer` y lo compilará. Fijaros como el nombre debe concordar con el módulo que espera encontrar la ventana principal.

Ahora los iconos del programa se encuentran compilados en el fichero `recursos_rc.py`. Nuestro programa los tomará de ahí en lugar de utilizar las imágenes del directorio `recursos/`.

Llegados a este punto es hora de crear un programa con PySide e importar el diseño. La lógica de creación de la ventana principal es la siguiente:

```python
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.mainwindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor explícito de QMainWindow
        QMainWindow.__init__(self)

        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Vamos a ejecutar el programa a ver si todo funciona bien:

- Widgets -> Ok
- Estilos -> Ok
- Recursos -> Ok
- Tips -> Ok

Ya lo véis, fácil, rápido y para toda la familia.

En la próxima lección vamos a ver cómo programar este cascarón para que los widgets tengan alguna funcionalidad.

## 1.9.3 Añadiendo la programación al diseño
