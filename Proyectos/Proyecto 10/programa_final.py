import sys
from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial
from helpers import absPath
from cartas import *


class Jugador:
    def __init__(self, nombre):
        self.mano = []
        self.puntos = 0
        self.nombre = nombre
        self.plantado = False

    def sumar(self, carta):
        self.mano.append(carta)
        self.calcular()

    def calcular(self):
        self.puntos = 0
        # Primero sumamos las cartas visibles que no son ases
        for carta in self.mano:
            if carta.visible:
                if carta.nombre not in ["As", "Jota", "Reina", "Rey"]:
                    self.puntos += carta.numero
                elif carta.nombre in ["Jota", "Reina", "Rey"]:
                    self.puntos += 10

        # Luego sumamos los ases visibles para adaptarlos a las necesidades
        for carta in self.mano:
            if carta.visible:
                if carta.nombre == "As":
                    # Sumamos el as como 11 siempre que sumemos 21 puntos o menos
                    if self.puntos + 11 <= 21:
                        self.puntos += 11
                    # Si superamos los 21 puntos lo sumamos valiendo 1
                    else:
                        self.puntos += 1

    def consultar(self):
        print(f"{self.nombre}: {[f'{c.nombre} de {c.palo}' for c in self.mano if c.visible]} ({self.puntos})")


class Blackjack:
    def __init__(self, baraja):
        self.baraja = baraja
        self.humano = Jugador("Héctor")
        self.banca = Jugador("Banca")

    def repartir(self, jugador, voltear=True):
        carta = self.baraja.extraer()
        if carta:
            if voltear:
                carta.mostrar()  # si no le damos la vuelta no se ve el número
            jugador.sumar(carta)
        return carta

    def ganador(self):
        # Primero comprobamos si gana la banca porque se pasa el humano
        if self.humano.puntos > 21:
            return 2
        # Luego comprobamos si gana el humano porque se pasa la banca
        if self.banca.puntos > 21:
            return 1
        # Finalmente comprobamos quien se acerca más a 21
        if self.humano.puntos > self.banca.puntos:
            return 1
        elif self.humano.puntos < self.banca.puntos:
            return 2
        else:
            return 0

    def reiniciar(self):
        self.baraja.reiniciar()
        self.humano = Jugador("Héctor")
        self.banca = Jugador("Banca")

    def consultarGanador(self):
        ganador = self.ganador()
        if ganador == 2:
            print(f"Gana la banca")
        elif ganador == 1:
            print(f"Gana el humano")
        else:
            print(f"Empate")


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     # Pruebas de juego sin interfaz gráfica
#     baraja = Baraja()
#     bj = Blackjack(baraja)
#     # Repartimos dos cartas a la banca, la segunda sin voltear
#     bj.repartir(bj.banca)
#     bj.repartir(bj.banca, False)
#     bj.banca.consultar()
#     # Repartimos dos cartas al humano
#     bj.repartir(bj.humano)
#     bj.repartir(bj.humano)
#     bj.humano.consultar()
#     # Volteamos la carta de la banca y recalculamos
#     bj.banca.mano[1].mostrar()
#     bj.banca.calcular()
#     bj.banca.consultar()
#     # Comprobamos si hay un ganador
#     bj.consultarGanador()
#     # Finalizamos el script
#     sys.exit(0)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuramos la ventana y el fondo
        self.setWindowTitle("Blackjack sin apuestas")
        self.setFixedSize(900, 630)
        # Configuración de la baraja
        self.baraja = Baraja(self)
        self.setCentralWidget(self.baraja)
        # Interfaz (después de asignar el widget central para sobreponerla)
        self.setupUi()
        # Creamos el juego del blackjack
        self.bj = Blackjack(self.baraja)
        # Posicionamos las cartas y hacemos el reparto inicial de cartas
        self.preparar()
        # Creamos las señales
        self.btnPedir.clicked.connect(self.pedir)
        self.btnPlantar.clicked.connect(self.plantar)
        self.btnReiniciar.clicked.connect(self.reiniciar)

    def preparar(self):
        """ Posiciona la baraja inicial y ejecuta los primeros repartos"""
        # Posicionamos las cartas
        offset = 0
        for carta in self.baraja.cartas:
            carta.posicionar(45 + offset, 205 + offset)
            offset += 0.25
        # Bloqueamos los botones de acción
        self.btnPedir.setEnabled(False)
        self.btnPlantar.setEnabled(False)
        self.btnReiniciar.setEnabled(False)
        # Repartimos dos cartas al jugador
        QtCore.QTimer.singleShot(500, partial(self.repartir, self.bj.humano))
        QtCore.QTimer.singleShot(750, partial(self.repartir, self.bj.humano))
        # Repartimos dos cartas a la banca, una se dejará oculta
        QtCore.QTimer.singleShot(1250, partial(self.repartir, self.bj.banca))
        QtCore.QTimer.singleShot(1500, partial(self.repartir, self.bj.banca, False))
        # Comprobamos la mano del jugador
        QtCore.QTimer.singleShot(2500, self.comprobar)
        # Empieza el juego
        self.registro.append(f"== Empieza Blackjack ==")

    def reiniciar(self):
        """ Reinicia los marcadores, el registro y prepara un nuevo juego """
        # añadimos las cartas de las manos del jugador y la banca a la baraja
        self.marcadorJugador.setText("0")
        self.marcadorBanca.setText("0")
        self.registro.setText("")
        self.bj.reiniciar()
        self.preparar()

    def repartir(self, jugador, voltear=True):
        """ Reparte una carta de blackjack y la posiciona en la pantalla """
        carta = self.bj.repartir(jugador, voltear)
        if jugador == self.bj.humano:
            offset_x = len(self.bj.humano.mano) * 40
            carta.mover(195+offset_x, 320, 750)
        elif jugador == self.bj.banca:
            offset_x = len(self.bj.banca.mano) * 25
            carta.mover(251+offset_x, 110, 750, 0.8)
        self.marcadores()

    def marcadores(self):
        """ Actualiza los marcadores y determinar si ha finalizado el juego """
        self.marcadorJugador.setText(f"{self.bj.humano.puntos}")
        self.marcadorBanca.setText(f"{self.bj.banca.puntos}")
        # Actualizamos el registro inicialmente
        self.registro.append(f"{self.bj.humano.nombre} [{self.bj.humano.puntos}], {self.bj.banca.nombre} [{self.bj.banca.puntos}]")
        # Hacemos un scroll abajo del todo del registro automáticamente
        self.registro.verticalScrollBar().setValue(self.registro.verticalScrollBar().maximum())
        # Determinar si el juego ha finalizado y mostrar el mensaje
        if self.bj.humano.plantado and self.bj.banca.plantado:
            if self.bj.ganador() == 1:
                self.registro.append(f"== Ganador: {self.bj.humano.nombre} ==")
            elif self.bj.ganador() == 2:
                self.registro.append(f"== Ganador: {self.bj.banca.nombre} ==")
            else:
                self.registro.append(f"====== Empate ======")

    def comprobar(self):
        """ Comprueba la mano del jugador """
        # Activamos el botón reiniciar
        self.btnReiniciar.setEnabled(True)
        # Si tenemos menos de 21 puntos permitimos pedir o plantarse
        if self.bj.humano.puntos < 21:
            self.btnPedir.setEnabled(True)
            self.btnPlantar.setEnabled(True)
        # Si tenemos 21 puntos o mas plantamos al jugador y pasamos a la banca
        elif self.bj.humano.puntos >= 21:
            self.bj.humano.plantado = True
            # Iniciamos la jugada de la banca
            self.jugarBanca()

    def pedir(self):
        """ Desactiva los botones de la interfaz y pide una carta """
        # Bloqueamos los botones de acción
        self.btnPedir.setEnabled(False)
        self.btnPlantar.setEnabled(False)
        self.btnReiniciar.setEnabled(False)
        # Repartimos una carta al jugador
        QtCore.QTimer.singleShot(500, partial(self.repartir, self.bj.humano))
        # Comprobamos los puntos del jugador
        QtCore.QTimer.singleShot(1500, self.comprobar)

    def plantar(self):
        """ Planta al usuario e inicia la jugada de la banca """
        # Bloqueamos los botones de pedir y plantar
        self.btnPedir.setEnabled(False)
        self.btnPlantar.setEnabled(False)
        # Plantamos al jugador
        self.bj.humano.plantado = True
        # Iniciamos la jugada de la banca
        self.jugarBanca()

    def jugarBanca(self):
        """ Voltea la carta oculta y determina si la banca sigue jugando """
        # La banca jugará solamente cuando el jugador no haya perdido
        if self.bj.humano.puntos > 21:
            # Si el humano ha perdido plantaremos a la banca
            self.bj.banca.plantado = True
        # Si el jugador no ha perdido entonces...
        else:
            # Si la banca tiene dos cartas volteamos la segunda y calculamos
            if len(self.bj.banca.mano) == 2:
                self.bj.banca.mano[1].mostrar()
                self.bj.banca.calcular()
            # Si la banca tiene >= 17 puntos o más que el jugador la plantamos
            if self.bj.banca.puntos >= 17 or self.bj.banca.puntos > self.bj.humano.puntos:
                self.bj.banca.plantado = True
            # Si la banca no se ha plantado le damos una carta
            if not self.bj.banca.plantado:
                QtCore.QTimer.singleShot(1500, partial(self.repartir, self.bj.banca))
                # Y programamos una posible siguiente jugada recursivamente
                QtCore.QTimer.singleShot(2500, self.jugarBanca)
        # Finalmente actualizamos el marcador
        self.marcadores()

    def setupUi(self):
        self.setStyleSheet("""
            QTextEdit {background-color: #ddd; font-size:13px }
            QLabel { color: white; font-size: 40px; font-weight: 500 }
            QPushButton { background-color: #20581e; color: white;font-size: 15px }
            QPushButton:disabled { background-color: #163914 }""")
        # Configuración del fondo
        tablero = QtGui.QImage(absPath("images/Tablero.png"))
        paleta = QtGui.QPalette()
        paleta.setBrush(QtGui.QPalette.Window, QtGui.QBrush(tablero))
        self.setPalette(paleta)
        # Marcadores
        self.marcadorBanca = QtWidgets.QLabel("0", self)
        self.marcadorBanca.resize(50, 50)
        self.marcadorBanca.move(342, 19)
        self.marcadorJugador = QtWidgets.QLabel("0", self)
        self.marcadorJugador.resize(50, 50)
        self.marcadorJugador.move(355, 557)
        # Botones
        self.btnPedir = QtWidgets.QPushButton("Pedir carta", self)
        self.btnPedir.resize(175, 32)
        self.btnPedir.move(692, 495)
        self.btnPlantar = QtWidgets.QPushButton("Plantarse", self)
        self.btnPlantar.resize(175, 32)
        self.btnPlantar.move(692, 535)
        self.btnReiniciar = QtWidgets.QPushButton("Reiniciar", self)
        self.btnReiniciar.resize(175, 32)
        self.btnReiniciar.move(692, 575)
        # Texto para el registro
        self.registro = QtWidgets.QTextEdit(self)
        self.registro.setReadOnly(True)
        self.registro.move(692, 285)
        self.registro.resize(175, 185)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # exec_() si PySide6 < 6.1.0 (pip install --upgrade pyside6)
    sys.exit(app.exec())
