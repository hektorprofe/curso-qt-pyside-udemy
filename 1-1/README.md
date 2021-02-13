# 1.1 Preparación prévia

- 1.1.1 Requisitos recomendados
- 1.1.2 Equipo de pruebas y versiones
- 1.1.3 Tip: Extensiones de VSC y demases
- 1.1.4 Tip: Añadir el software de Qt al Path
- 1.1.5 Tip: Encontrar el intérprete de Python

## 1.1.1 Requisitos recomendados

- Conocimientos de Python básico hasta las clases y objetos.
- Saber manejar la terminal del sistema para ejecutar scripts.
- Python 3.8 o superior descargado de la web oficial `python.org` o con la versión de Miniconda/Anaconda añadidas al Path del sistema. No puedo asegurar el correcto funcionamiento de la herramienta `auto-py-to-exe` con versiones alternativas como las de la Store de Microsoft o del gestor de paquetes Chocolatey.

Nota: Si el comando `python` no funciona en la terminal, pero sí lo hace `py`, hay que desactivar los alias del sitema. Inicio > Escribir "Alias", abrir la ventana y desactivar python.exe y python3.exe, esto sucede si instalas Python desde la Store.

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

## 1.1.4 Tip: Añadir el software de Qt al Path

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

## 1.1.5 Tip: Encontrar el intérprete de Python

Si queremos encontrar donde está instalado `python.exe`, abrimos una terminal como administrador, clic derecho **Ejecutar como administrador**:

```bash
python
>>> import sys
>>> print(sys.path)
```

Copiamos la ruta a los `site-packages`, seleccionamos y clic derecho en la selección para copiar la ruta:

```
c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages
```

Accedemos a ella (clic derecho en la línea de comandos para pegar), siendo administradores, y abrimos el explorador en ese directorio:

```bash
cd c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages

cd ../..

explorer .
```

Ahí tenemos el ejecutable de Python del sistema.
