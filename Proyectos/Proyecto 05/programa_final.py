from PySide6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLCDNumber, QPushButton)
from functools import partial
from helpers import *

# https://doc.qt.io/qt-6/qlcdnumber.html
# https://docs.python.org/3/library/functools.html#functools.partial


class Calculadora(QLCDNumber):
    def __init__(self):
        # definimos unos dígitos y un estilo por defecto al panel LCD
        super().__init__(digitCount=12, segmentStyle=QLCDNumber.Flat)
        self.texto = '0'
        self.reiniciar = False
        # deberíamos definir también operación inicalmente
        self.operacion = None

    def escribir(self, caracter):
        # La función escribir añade caracteres al panel LCD

        # después de un cálculo comprobamos si debemos limpiar el panel LCD
        if self.reiniciar:
            self.limpiar()

        # no permitiremos que se pueda añadir más de una coma para decimales
        if caracter == "." and self.texto.count('.') == 1:
            return

        # si la longitud del texto no se ha superado añadimos el caracter
        if len(self.texto) <= 12:
            self.texto += caracter
            # borraremos los posibles 0 a la izquierda del número
            self.display(self.texto.lstrip("0"))

    def preparar(self, operacion):
        # La función preparar almacena en memoria el número y la operación
        self.operacion = operacion
        self.memoria = float(self.texto)
        self.limpiar()

    def calcular(self):
        # La función calcular utiliza la operación y el número en memoria
        # para operarlo en conjunto al número actual del LCD

        resultado = 0.0

        if self.operacion == "+":
            resultado = self.memoria + float(self.texto)
        elif self.operacion == "-":
            resultado = self.memoria - float(self.texto)
        elif self.operacion == "×":
            resultado = self.memoria * float(self.texto)
        elif self.operacion == "÷":
            resultado = self.memoria / float(self.texto)

        # es muy importante redondear los decimales
        self.texto = str(round(resultado, 2))

        # si el resultado no cabe en el panel LCD mostamos un error
        if len(self.texto) > 12:
            self.texto = 'Error'

        # mostramos el texto en el panel
        self.display(self.texto)

        # reiniciamos
        self.reiniciar = True

    def limpiar(self):
        # La función limpiar establece el texto del panel a cero
        self.texto = '0'
        self.display(self.texto)
        self.reiniciar = False


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(480)
        self.setFixedHeight(360)
        self.setWindowTitle("Calculadora")
        with open(absPath("Scalcula.qss")) as styles:
            self.setStyleSheet(styles.read())

        # Creamos un layout cuadricular y añadimos la calduladora LCD arriba
        self.setLayout(QGridLayout())
        self.calculadora = Calculadora()
        self.layout().addWidget(self.calculadora, 0, 0, 1, 0)

        # Definimos todos los botones de la calculadora
        simbolos = [['7', '8', '9', '÷'], ['4', '5', '6', '×'],
                    ['1', '2', '3', '-'], ['.', '0', '=', '+']]

        # Recreamos los botones usando un par de bucles anidados
        for i, fila in enumerate(simbolos):
            for j, simbolo in enumerate(fila):
                boton = QPushButton(simbolo)
                boton.setStyleSheet("height:50px;font-size:25px")
                # pasamos el simbolo al boton usando un objeto parcial
                boton.clicked.connect(partial(self.boton_clicado, simbolo))
                # Sumamos 1 al offset de las filas para dejar espacio al LCD
                self.layout().addWidget(boton, i + 1, j)

    def boton_clicado(self, simbolo):
        if simbolo.isdigit() or simbolo == '.':
            self.calculadora.escribir(simbolo)
        elif simbolo == '=':
            self.calculadora.calcular()
        else:
            self.calculadora.preparar(simbolo)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()
