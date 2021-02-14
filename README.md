# Índice del curso

El curso tiene dos bloques independientes para separar el aprendizaje de Pyside y el desarrollo de diferentes programas. Mi intención es extender el segundo bloque y con el tiempo crear colección de programas de ejemplo.

## 1: Fundamentos de Qt/PySide

### 1.1: [Preparación prévia](1-1/)

- 1.1.1 Requisitos para tomar el curso
- 1.1.2 Equipo de pruebas y versiones
- 1.1.3 Tip: Extensiones de VSC y demases
- 1.1.4 Tip: Añadir el software de Qt al Path
- 1.1.5 Tip: Encontrar el intérprete de Python

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

### 1.9: [Interfaces clásicas con QtDesigner](1-9/)

- 1.9.1 Nuestro primer diseño
- 1.9.2 Compilación y uso de diseños con recursos
- 1.9.3 Añadiendo la programación al diseño
- 1.9.4 Manejo de subventanas compiladas

### 1.10 [Interfaces modernas con QtCreator y QtQuick](1-10/)

Esto es interesante, copiar un poco el tutorial. que es QML y que es Qtick

- Que es QT Quick y QML
- tutorial completo con Qt Creator
  https://www.youtube.com/watch?v=pD0UeD7S27s&list=PLfQ7GQSrl0_v1T4Pe_NW4GLaynBfydFy-

### 1.11 Creación de ejecutables en Windows](1-11/)

- 1.11.1 Ejecutables con auto-py-to-exe (dependencias manuales)
- 1.11.2 Comprensión del distribuible con 7-Zip

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
