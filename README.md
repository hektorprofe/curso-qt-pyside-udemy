# Índice del curso

El curso tiene dos bloques independientes para separar el aprendizaje de Pyside y el desarrollo de diferentes programas. Mi intención es extender el segundo bloque y con el tiempo crear colección de programas de ejemplo.

## 1: Fundamentos de Qt/PySide

### 1.1: [Preparación prévia](1-1/)

- 1.1.1 Requisitos para tomar el curso
- 1.1.2 Equipo de pruebas y versiones
- 1.1.3 Tip: Intérprete de Python
- 1.1.4 Tip: Software de Qt
- 1.1.5 Tip: Extensiones de VSC y demases

### 1.2: [Conceptos básicos](1-2/)

- 1.2.1 Qt, PySide y PyQt
- 1.2.2 Primera aplicación
- 1.2.3 Superclases y subclases
- 1.2.4 Lo mismo usando POO
- 1.2.5 Tamaño de los widgets
- 1.2.6 Señales y receptores
- 1.2.7 Componentes manipulables

### 1.3: [Widgets para formularios](1-3/)

- 1.3.1 Etiquetas
- 1.3.2 Casillas
- 1.3.3 Botones radiales
- 1.3.4 Desplegables
- 1.3.5 Listas
- 1.3.6 Campos de texto
- 1.3.7 Campos numéricos

### 1.4: [Formas de organización](1-4/)

- 1.4.1 Widget personalizado
- 1.4.2 Layouts básicos
- 1.4.3 Layouts anidados
- 1.4.4 Layout en cuadrícula
- 1.4.5 Layout en formulario
- 1.4.6 Layout apilado
- 1.4.7 Layout con pestañas

### 1.5: [Cuadros de diálogo](1-5/)

- 1.5.1 Diálogos personalizados
- 1.5.2 Diálogos de mensaje
- 1.5.3 Diálogos predeterminados
  - 1.5.3.1 Mensaje de cuestión
  - 1.5.3.2 Mensaje acerca de
  - 1.5.3.3 Mensaje crítico
  - 1.5.3.4 Mensaje informativo
  - 1.5.3.5 Mensaje de aviso
- 1.5.4 Activando las traducciones
- 1.5.5 Diálogos específicos
  - 1.5.5.1 Diálogos de fichero
  - 1.5.5.2 Diálogos de entrada de datos
  - 1.5.5.3 Diálogos de fuente y color

### 1.6: [Ventana principal](1-6/)

- 1.6.1 Menús, acciones y estado
- 1.6.2 Barra de herramientas
- 1.6.3 Docks flotantes

### 1.7: [Control de subventanas](1-7/)

- 1.7.1 Creación de subventanas
- 1.7.2 Subventanas persistentes

### 1.8: [Tematización](1-8/)

- 1.8.1 Estilos
- 1.8.2 Paletas
- 1.8.3 Iconos
- 1.8.4 Qt Style Sheets
- 1.8.5 Cargando ficheros QSS

### 1.9: [Qt Creator](1-9/)

- 1.9.1 Introducción práctica
- 1.9.2 Compilación del diseño
- 1.9.3 Añadiendo la lógica

## 1.10: [Introducción a Quick/QML]

QML ofrece un enfoque alternativo para crear interfaces de usuario, en comparación con los widgets, y originalmente fue motivado por el desarrollo de aplicaciones móviles. Junto con el módulo Qt Quick, brinda acceso para interactuar con el dispositivo móvil mediante acciones como toques, arrastrar y soltar, animaciones, estados, transiciones, menús de cajón, etc. Los elementos que puedes encontrar en las aplicaciones QML / Quick están enfocados a brindar una infraestructura de aplicaciones más dinámica con diferentes propiedades basadas en determinados comportamientos. Aunque QML tiene la motivación para proporcionar interfaces con dispositivos móviles, también puede usarlo para aplicaciones de escritorio. Además, puede aumentar su aplicación con JavaScript estándar, que en combinación con C ++ puede convertirse en una infraestructura atractiva.

https://doc.qt.io/qtforpython/tutorials/index.html#quick-qml-basic-tutorials
https://www.youtube.com/watch?v=pD0UeD7S27s&list=PLfQ7GQSrl0_v1T4Pe_NW4GLaynBfydFy-

### 1.11: [Distribución](1-10/)

A fecha de la realización del curso PySide6 es relativamente nuevo y aún no hay muchas opciones para generar ejecutables. Utilizaremos la forma más simple con `auto-py-to-exe` añadiendo las dependencias manualmente.

- 1.10.1 Generando un ejecutable
- 1.10.2 Recursos compilados

## 2: Desarrollo de programas

_Primero desarrollar todo el bloque 1 en este primer impulso, luego veremos los programas._

### Programa planeado

Uno de los programas debe ser crear un reloj con ejecución concurrente usando threads:

- Hilos y procesos
- Usando un thread pool
- Implementando un reloj (se puede con hilos)

### Programa planeado

Otro programa intentará explorar el concepto de arquitectura MVC:

- Arquitectura MVC
- Modelos y vistas
- Implementando un programa con crud
