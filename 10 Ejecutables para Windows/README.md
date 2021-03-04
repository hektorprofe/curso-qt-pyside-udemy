# 1.10 Creación de ejecutables para Windows

- 1.10.1 Ejecutables con auto-py-to-exe (dependencias manuales)
- 1.10.2 Comprensión del distribuible con 7-Zip

## 1.10.1 Ejecutables con auto-py-to-exe (dependencias manuales)

Empezamos instalando `pyside6` y `auto-py-to-exe` en un entorno virtual dentro del directorio del programa (en VSC clic derecho `Open in terminal`).

Este paso es optativo, pero si no lo hacemos el ejecutable incluirá todas las dependencias instaladas en Python. Al crear un entorno virtual con los módulos mínimos el tamaño final del ejecutable se verá reducido drásticamente:

```bash
pip install pipenv
pipenv install pyside6 auto-py-to-exe            # sin intérprete
python -m pipenv install pyside6 auto-py-to-exe  # con intérprete
```

Iniciamos la interfaz de compilación:

```bash
pipenv run auto-py-to-exe
pipenv run auto-py-to-exe            # sin intérprete
python -m pipenv run auto-py-to-exe  # con intérprete
```

En los ajustes:

- `Script Location`: Fichero principal del programa
- `Onefile`: One Directory
- `Console Window`: Window Based (hide console)
- `Additional Files/Folders`: Aquí debemos incluir todos los recursos externos no compilados y dependencias de Qt, que debemos buscar en el entorno virtual. Este paso es imprescindible dado que estamos utilizando `PySide6` y `auto-py-to-exe` no incluye automáticamente las dependencias de Qt. Para `PySide2` sí que las incluye así que con suerte en futuras actualizaciones podríamos saltarnos este paso.

Pipenv crea los entornos virtuales en el directorio del usuario, vamos a buscar las siguiente dependencias de Qt ahí, si tenemos dificultados para encontrar el directorio podemos ayudanros de Pipenv:

```bash
pipenv --venv
cd path/del/entorno
explorer .
```

Navegaremos a las dependencias de PySide6:

- `Lib/site-packages/PySide6`

Y copiamos lo siguiente al directorio output del ejecutable:

<img src="docs/01.png">

- Una vez configurado todo pulamos `CONVERT .PY TO .EXE` y en un rato deberíamos tener nuestro programa compilado en la carpeta `output`.

## 1.10.2 Comprensión del distribuible con 7-Zip

Los ejecutables son bastante pesados porque incluyen el intérprete de `Python` y todas las dependencias de `Qt`.

El directorio de un programa básico ocupa unos 80MB, pero tranquilos, podemos reducir mucho el tamaño a la hora de compartir nuestro programa utilizando un compresor como [7-Zip](https://www.7-zip.org/) y el formato `7z`.

Este compresor es software libre y por lo tanto gratuito, a diferencia de Winzip o Winrar así que os lo recomiendo encarecidamente. Además el formato `7z` es de los que comprimen mejor, si establecemos el nivel de comprensión de la carpeta en `Ultra` podemos reducir el tamaño del distribuible hasta cuatro veces.

<img src="docs/02.png">

Otros modos de compresión como el clásico `zip` o `tar.gz` no reducen tanto el tamaño:

<img src="docs/03.png">
