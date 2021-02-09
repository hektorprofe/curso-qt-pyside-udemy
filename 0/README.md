# Preparación prévia

## Requisitos para tomar el curso

- Python 3.8 o superior listo para trabajar.
- Conocimientos de Python básico hasta las clases y objetos.
- Saber manejar la terminal del sistema para ejecutar scripts.

## Equipo de pruebas y versiones

Este es el software utilizado durante el curso.

- `Sistema operativo`: Windows 10
- `Intérprete de Python`: Versión 3.9 instalada desde Microsoft Store
- `Terminal`: Windows Terminal instalada desde la Microsoft Store
- `Editor`: Visual Studio Code

Sentíos libres de usar el sistema, intérprete 3.8 o superior, terminal y editor que vosotros prefiráis.

En cuanto a los paquetes, estas son las versiones utilizadas:

- `Pip`: (pip==21.0.1)
- `PySide6`: (pyside==6.0.1)
- `Auto PY to EXE`: (auto-py-to-exe==2.8.0)

Siempre que estéis usando la versión 6 de Pyside deberíais poder realizar el curso sin problemas.

Por último, a modo de recordatorio, para ejecutar algunos binarios, como `auto-py-to-exe`, si la terminal no lo detecta directamente se puede llamar escribiendo:

```bash
pip install auto-py-to-exe
python -m auto_py_to_exe
```

## Tips

### Encontrar el software de Qt

Desde la terminal re/instalamos Pyside6:

```bash
pip install pyside6
```

Esto dará la ruta al directorio, la copiamos y abrimos:

```bash
cd c:\users\hcost\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages

explorer .
```

Buscamos la carpeta `PySide6` y creamos un acceso directo a ella. Dentro encontramos:

- `designer.exe`: Diseñador de interfaces gráficas.
- `uic.exe`: Compilador de interfaces de usuario.
- `rcc.exe`: Compilador de recursos.

### Encontrar el intérprete de Python

Si queremos encontrar donde está instalado `python.exe`, abrimos una terminal como administrador, clic derecho **Ejecutar como administrador**:

```bash
python
>>> import sys
>>> print(sys.path)
```

Copiamos la ruta a los `site-packages`, seleccionamos y clic derecho en la selección para copiar la ruta:

```
C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.496.0_x64__qbz5n2kfra8p0\\lib\\site-packages
```

Accedemos a ella (clic derecho en la línea de comandos para pegar), siendo administradores, y abrimos el explorador en ese directorio:

```bash
cd C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.496.0_x64__qbz5n2kfra8p0\\lib\\site-packages

cd ../..

explorer .
```

Ahí tenemos el ejecutable de Python del sistema.

### Extensiones de VSC

En caso de que alguien quiera utilizar mi editor:

- Extensión para ejecutar script pulsando F1 + Enter: `Code Runner`
- Extensión para autoformatear código Python: `autopep8`
- Extensión para detectar errores en Python: `pylint`

## Qt, PySide y PyQt

`Qt` es un framework ámpliamente utilizado para desarrollar programas con interfaces gráficas de usuario:

- Está programado en C++, por tanto es muy rápido.
- Es multiplataforma, funciona en diferentes sistema operativos.
- Es orientado a objetos, fácil de empezar a utilizar y aprender.
- Es software libre y código abierto, por tanto su uso es seguro.
- Ofrece licencias públicas, permitiendo su uso de forma gratuita.

`PySide` y `PyQt` son bindings o puentes que permiten utilizar Qt, programado en C++, a través de Python.

PySide es el binding oficial desarrollado por `The Qt Company` con una licencia pública, en cambio PyQt está desarrollado por la firma `Riverbank Computing` y tiene una licencia comercial de $550.

Antiguamente `PySide` estaba por detrás de `PyQt` en características, razón por la cuál se extendió el uso de la segunda alternativa, pero gracias al auge de Python y al apoyo de `The Qt Company`, la suite de `PySide` contiene todo lo necesario para desarrollar programas completos con Python con las ventajas de una licencia pública.
