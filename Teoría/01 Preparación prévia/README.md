# 1.1 Preparación prévia

- 1.1.0 Requisitos y equipo de pruebas
- 1.1.1 Instalación de Python
- 1.1.2 Instalación de VSC y extensiones
- 1.1.3 Añadir el software de Qt al Path

## 1.1.0 Requisitos y equipo de pruebas

- Conocimientos de Python básico hasta las clases y objetos.
- Saber manejar la terminal del sistema para ejecutar scripts.
- Python 3.8 o superior descargado de la web oficial `python.org` o con la versión de Miniconda/Anaconda añadidas al Path del sistema. No puedo asegurar el correcto funcionamiento de la herramienta `auto-py-to-exe` con versiones alternativas como las de la Store de Microsoft o del gestor de paquetes Chocolatey.

**Nota**: Si el comando `python` no funciona en la terminal, pero sí lo hace `py`, hay que desactivar los alias del sitema. Inicio > Escribir "Alias", abrir la ventana y desactivar python.exe y python3.exe, esto sucede si instalas Python desde la Store.

Este es el software utilizado durante el curso.

- `Sistema operativo`: Windows 10 Pro versión 20H2.
- `Intérprete de Python`: Versión 3.9 instalada desde `python.org`.
- `Terminal`: Windows Terminal instalada desde la Microsoft Store.
- `Editor`: Visual Studio Code desde `code.visualstudio.com`.

En cuanto a los paquetes, estas son las versiones utilizadas:

- `Pip`: (pip==21.0.1)
- `PySide6`: (pyside==6.0.1)
- `Auto PY to EXE`: (auto-py-to-exe==2.8.0)

Siempre que estéis usando la versión 6 o superior de Pyside deberíais poder realizar el curso sin problemas.

## 1.1.1 Instalación de Python

Instalar la versión oficial desde `python.org`, marcar la opción inicial de "Añadir al PATH" y la última para activar las rutas largas.

Comprobar si el intérprete funciona en una terminal ejecutando uno de estos comandos:

```bash
python --v
python -V
```

Si no funciona reiniciar la terminal, si siguie sin funcionar desinstalar Python y buscar otras posibles versiones de Python instaladas anteriormente y desinstalarlas.

## 1.1.2 Extensiones de VSC y demases

En caso de que alguien quiera utilizar VSC recomiendo las extensiones:

- `autopep8` para autoformatear código Python (automática)
- `pylint` para detectar errores en Python (automática)
- `Code Runner` para ejecutar script pulsando F1 + Enter

Otras configuraciones interesantes:

- Tema `Monokai Pro`
- Fuente `FiraCode` con ligatures

## 1.1.3 Instalación y configuración de PySide

Desde la terminal re/instalamos Pyside6:

```bash
pip install pyside6
```

Esto dará la ruta al directorio, la copiamos y abrimos:

```bash
c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages

explorer .
```

Buscamos la carpeta `PySide6`y dentro encontramos:

- `designer.exe`: Diseñador de interfaces gráficas.
- `uic.exe`: Compilador de interfaces de usuario.
- `rcc.exe`: Compilador de recursos.

Mi recomendación es añadir esta ruta al path del usuario para poder acceder cómodamente a al diseñador y las herramientas de compilación:

1. Clic derecho en Inicio > Sistema
2. Bajamos hasta encontrar "Configuración avanzada del sistema"
3. Variables de enterno > Editar variables de usuario > Path > Nuevo
4. Pegamos la carpeta de PySide6:

```
c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages\pyside6
```

Guardamos y reiniciamos las terminales y los editores.

Ahora podemos ejecutar desde cualquier lugar los ejecutables:

- `designer.exe`: Diseñador de interfaces gráficas.
- `uic.exe`: Compilador de interfaces de usuario.
- `rcc.exe`: Compilador de recursos.

Para configurar el compilador `uic` en Qt Designer

Abrimos el diseñador:

```bash
designer
```

- Fomulario > `View Python Code`

Nos indicará que se espera `uic` en el directorio `bin` del paquete `PySide6`:

```bash
cd c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages\pyside6

explorer .
```

Creamos una carpeta `bin` y copiamos el fichero `uic.exe` dentro.

Listo, ya podemos previsualizar diseños en código Python y exporarlos en ficheros.
