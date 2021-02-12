# 1.1 Preparación prévia

- 1.1.1 Requisitos para tomar el curso
- 1.1.2 Equipo de pruebas y versiones
- 1.1.3 Tip: Extensiones de VSC y demases
- 1.1.4 Tip: Encontrar el software de Qt
- 1.1.5 Tip: Encontrar el intérprete de Python

## 1.1.1 Requisitos para tomar el curso

- Python 3.8 o superior listo para trabajar.
- Conocimientos de Python básico hasta las clases y objetos.
- Saber manejar la terminal del sistema para ejecutar scripts.

## 1.1.2 Equipo de pruebas y versiones

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

## 1.1.3 Tip: Extensiones de VSC y demases

En caso de que alguien quiera utilizar VSC recomiendo las extensiones:

- `autopep8` para autoformatear código Python (automática)
- `pylint` para detectar errores en Python (automática)
- `Code Runner` para ejecutar script pulsando F1 + Enter

Otras configuraciones interesantes:

- Tema `Monokai Pro`
- Fuente `FiraCode` con ligatures

## 1.1.4 Tip: Encontrar el software de Qt

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

## 1.1.5 Tip: Encontrar el intérprete de Python

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
