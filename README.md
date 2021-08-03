# Desarrollo de programas gráficos en Python con Qt/PySide6

Bienvenido a mi curso sobre desarrollo de programas gráficos en Python con Qt y PySide. Si tienes conocimientos básicos sobre este lenguaje y te interesa añadir atractivas interfaces a tus scripts, [este curso](https://www.hektorprofe.net/cupon/pyside) es para ti.

- A través de sencillos ejemplos te introduciré en el desarrollo de interfaces de forma progresiva.
- Te enseñaré a utilizar los componentes gráficos esenciales y a organizarlos mediante diferentes tipos de layouts.
- Profundizaremos en el manejo de la ventana principal, el control de subventanas y los cuadros de diálogo.
- Veremos cómo tematizar los diseños, modificando la apariencia con estilos y paletas de colores.
- También te enseñaré las claves para crear diseños con Qt Designer y a utilizarlos en Python.
- Finalmente generaremos unos ejecutables en Windows para que puedas distribuir tus programas.

Al acabar el curso sabrás lo suficiente para añadir interfaces gráficas a cualquier programa que se te ocurra, pero mi intención es seguir actualizando el curso en el futuro. Periódicamente publicaré el proceso de creación de pequeños proyectos para poner en práctica los conocimientos adquiridos y también para enseñaros como integrar diferentes tecnologías con PySide.

Para saber más sobre el temario y mi didáctica, echa un vistazo a las lecciones gratuitas.

Sin más, nos vemos [en Udemy](https://www.udemy.com/course/python-desarrollo-interfaces-graficas-qt-pyside/?referralCode=9EAE0CB94440E8F97435).

## 1: Introducción a Qt/PySide6 con ejemplos sencillos

### 1.1: [Preparación prévia](Teoría/01%20Preparación%20prévia/)

Para tomar este curso es indispensable contar con conocimientos prévios de Python hasta las clases y objetos, así como tener preparado un sistema con Python 3.8 o superior accesible desde la terminal. He grabado un par de tutoriales configurando mi máquina con Windows 10, si tenéis la vuestra lista saltad a la lección de instalación de PySide.

- 1.1.0 Requisitos y equipo de pruebas
- 1.1.1 Instalación de Python
- 1.1.2 Instalación de VSC y extensiones
- 1.1.3 Instalación y configuración de PySide

### 1.2: [Conceptos básicos](Teoría/02%20Conceptos%20básicos/)

En esta unidad aprenderemos sobre "cute " (en español Qt), PySide y PyQt. Desarrollaremos la estructura básica de un programa en PySide extendiendo sus componentes básicos mediante la herencia de clases. Finalmente realizaremos algunos ejemplos para aprender cómo interactuar con los widgets utilizando sus señales y a manipularlos a través de sus métodos.

- 1.2.1 Qt, PySide y PyQt
- 1.2.2 Primera aplicación
- 1.2.3 Superclases y subclases
- 1.2.4 Lo mismo usando POO
- 1.2.5 Tamaño de los widgets
- 1.2.6 Señales y receptores
- 1.2.7 Componentes manipulables

### 1.3: [Widgets para formularios](Teoría/03%20Widgets%20para%20formularios/)

Ahora que tenemos sabemos manejar la estructura básica de un programa, el siguiente paso es aprender a utilizar los widgets más comunes en los formularios. Aprenderemos sobre las etiquetas, las casillas, los botones radiales, los desplegables, las listas y los campos para introducir textos y números desde el teclado.

- 1.3.1 Etiquetas
- 1.3.2 Casillas
- 1.3.3 Botones radiales
- 1.3.4 Desplegables
- 1.3.5 Listas
- 1.3.6 Campos de texto
- 1.3.7 Campos numéricos

### 1.4: [Formas de organización](Teoría/04%20Formas%20de%20organización/)

En esta unidad aprenderemos a organizar el espacio de las ventanas mediante layouts. Para ayudarnos a visualizar el espacio desarrollaremos nuestro propio widget personalizado que utilizaremos en los diferentes layouts. Empezaremos con los más básicos y luego daremos paso a otros más sofisticados, como las cuadrículas y las pestañas.

- 1.4.1 Widget personalizado
- 1.4.2 Layouts básicos
- 1.4.3 Layouts anidados
- 1.4.4 Layout en cuadrícula
- 1.4.5 Layout en formulario
- 1.4.6 Layout apilado
- 1.4.7 Layout con pestañas

### 1.5: [Cuadros de diálogo](Teoría/05%20Cuadros%20de%20diálogo/)

Las ventanas emergentes, cuadros de diálogo o simplemente popups son unos de los elementos más importantes de las interfaces gráficas porque permiten comunicarnos con el usuario de forma explícita. En esta unidad empezaremos desarrollando nuestro propio cuadro de diálogo y luego exploraremos algunas opciones predefinidas que nos facilita Qt.

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

### 1.6: [Ventana principal](Teoría/06%20Ventana%20principal/)

En esta unidad nos vamos a centrar en la ventana principal y su personalización. Aprenderemos a crear las barras de menú y de herramientas, añadiendo en ellas diferentes acciones con iconos y atajos de teclado. Por el camino activaremos la barra de estado para mostrar mensajes de ayuda y exploraremos una de sus funcionalidades más flexibles, los docks flotantes.

- 1.6.1 Menús, acciones y estado
- 1.6.2 Barra de herramientas
- 1.6.3 Docks flotantes

### 1.7: [Control de subventanas](Teoría/07%20Control%20de%20subventanas/)

A veces un programa con una única ventana no es suficiente, por eso esta unidad está dedicado al control de subventanas. En ella aprenderemos a crear nuestras propias subventanas utilizando como base la clase QWidget. Veremos cómo almacenarlas en la memoria de forma persistente y cómo acceder a sus métodos e información desde la ventana principal.

- 1.7.1 Creación de subventanas
- 1.7.2 Subventanas persistentes

### 1.8: [Tematización](Teoría/08%20Tematización/)

Esta unidad está dedicada a estudiar las diferentes formas de tematizar las aplicaciones. Aprenderemos a utilizar el tema fusión, a configurar las paletas de colores y a utilizar los iconos predeterminados. También veremos instalaremos algunos paquetes de terceros con temas e iconos alternativos e introduciremos las hojas de estilo de Qt, parecidas a las CSS de la programación web.

- 1.8.1 Estilos
- 1.8.2 Paletas
- 1.8.3 Iconos
- 1.8.4 Qt Style Sheets
- 1.8.5 Cargando ficheros QSS

### 1.9: [Diseño de interfaces con Qt Designer](Teoría/09%20Interfaces%20con%20Qt%20Designer/)

Ahora que ya sabemos un montón sobre PySide y sus componentes es el momento ideal para empezar a utilizar el diseñador de interfaces de Qt. En esta unidad os daré cuatro nociones básicas sobre el programa, aprenderemos a compilar los diseños y los recursos y os enseñaré a utilizarlos en vuestros programas creados con Python de la forma más sencilla posible.

- 1.9.1 Nuestro primer diseño
- 1.9.2 Compilación y uso de diseños con recursos
- 1.9.3 Añadiendo funcionalidades al diseño
- 1.9.4 Gestión de múltiples diseños

### 1.10 [Creación de ejecutables para Windows](Teoría/10%20Ejecutables%20para%20Windows/)

Los sistemas operativos Linux y MAC suelen tener Python instalado y ejecutar un programa con PySide es tan sencillo como instalar sus dependencias desde la terminal y ejecutar el script. Pero ese no es el caso de Windows y por eso en esta unidad prenderemos a generar distribuibles con Python integrado utilizando `auto-py-to-exe` y veremos cómo reducir su tamaño con `7-Zip`.

- 1.10.1 Ejecutables con auto-py-to-exe (dependencias manuales)
- 1.10.2 Comprensión del distribuible con 7-Zip

## 2: Desarrollo de programas gráficos con Qt/PySide6

Los proyectos los enseño a crear [en el curso de Udemy](https://www.hektorprofe.net/cupon/pyside) y son los siguientes:

* Editor de registros JSON y SQL con arquitectura Modelo-Vista
* Gestor CRUD de registros SQL con formularios
* Tablero Kanban en CSV con listas y un menú contextual
* Calculadora generada dinámicamente
* Gráficos dinámicos con PyQtGraph
* Reportes en HTML/PDF con gráficos y tablas
* Web scrapper concurrente usando PyQuery y QThreadPool
* Widget para barajas de cartas con animaciones
* Videojuego Blackjack usando el widget de barajas
