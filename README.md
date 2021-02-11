# Índice del curso

El curso tiene dos bloques independientes para separar el aprendizaje de Pyside y el desarrollo de diferentes programas. Mi intención es extender el segundo bloque y con el tiempo crear colección de programas de ejemplo.

## 1: Fundamentos de Qt/PySide

### 1.1: [Preparación prévia](1-1/)

- 1.1.1 Requisitos para tomar el curso
- 1.1.2 Equipo de pruebas y versiones
- 1.1.3 Tip: Intérprete de Python
- 1.1.4 Tip: Software de Qt
- 1.1.5 Tip: Extensiones de VSC

### 1.2: [Conceptos básicos](1-2/README.md)

- 1.2.1 Qt, PySide y PyQt
- 1.2.2 Primera aplicación
- 1.2.3 Superclases y subclases
- 1.2.4 Lo mismo usando POO
- 1.2.5 Tamaño de los widgets
- 1.2.6 Señales y receptores
- 1.2.7 Componentes manipulables

### 1.3: [Widgets para formularios](1-3/README.md)

- 1.3.1 Etiquetas
- 1.3.2 Casillas
- 1.3.3 Desplegables
- 1.3.4 Listas
- 1.3.5 Campos de texto
- 1.3.6 Campos numéricos

### 1.4: [Formas de organización](1-4/README.md)

- 1.4.1 Widget personalizado
- 1.4.2 Layouts básicos
- 1.4.3 Layouts anidados
- 1.4.4 Layout en cuadrícula
- 1.4.5 Layout apilado
- 1.4.6 Layout con pestañas

### 1.5: [Cuadros de diálogo](1-5/README.md)

- 1.5.1 Diálogos personalizados
- 1.5.2 Diálogos de mensaje
- 1.5.3 Diálogos predeterminados
- 1.5.4 Activando las traducciones
- 1.5.5 Diálogos específicos

### 1.6: [Ventana principal](1-6/README.md)

- 1.6.1 Barras de menú
- 1.6.2 Barras de herramientas
- 1.6.3 Barra de estado
- 1.6.4 Docks flotantes

### 1.7: [Control de ventanas](1-7/README.md)

- 1.7.1 Creación de ventanas
- 1.7.2 Cierre de ventanas
- 1.7.3 Ventanas persistentes
- 1.7.4 Mostrar y ocultar ventanas
- 1.7.5 Señales entre ventanas

### 1.8: [Tematización](1-8/README.md)

- 1.8.1 Estilos
- 1.8.2 Paletas
- 1.8.3 Iconos
- 1.8.4 QSS

### 1.9: [Qt Designer](1-9/README.md)

- 1.9.1 Introducción práctica
- 1.9.2 Compilación del diseño
- 1.9.3 Añadiendo la lógica
- 1.9.4 Sistema de recursos (en qt designer, hacer la compilación de recursos)

### 1.10: [Distribución](1-10/README.md)

A fecha de la realización del curso PySide6 es relativamente nuevo y aún no hay muchas opciones para generar ejecutables. Utilizaremos la forma más simple con `auto-py-to-exe` añadiendo las dependencias manualmente.

- 1.10.1 Generando un ejecutable
- 1.10.2 Accediendo a los recursos

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
