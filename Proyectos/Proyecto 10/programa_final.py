# Juego Blackjack usando nuestro widget de barajas de cartas
# https://en.wikipedia.org/wiki/Blackjack

from PySide6 import QtCore, QtGui, QtWidgets
from helpers import absPath
from cartas import *
from functools import partial
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana y el fondo
        self.setWindowTitle("Blackjack sin apuestas")
        self.setFixedSize(900, 630)

        # Configuración de la baraja
        self.baraja = Baraja(self)
        self.setCentralWidget(self.baraja)
        self.posicionarBaraja()

        # Interfaz (importante: después de asignar el widget central)
        self.setupUi()

        # Creamos las señales
        # self.btnPlantar.clicked.connect(self.plantar)
        self.btnReiniciar.clicked.connect(self.reiniciar)
        self.btnPedir.clicked.connect(self.pedir)

        # Hacer el reparto inicial de cartas
        self.repartoInicial()

    def posicionarBaraja(self):
        offset = 0
        for carta in self.baraja.cartas:
            carta.move(45 + offset, 205 + offset)
            carta.sobreponer()  # upd: traemos las cartas al frente por orden
            offset += 0.25

    def reiniciar(self):
        # añadimos las cartas de las manos del jugador y la banca a la baraja
        self.marcadorJugador.setText("0")
        self.marcadorBanca.setText("0")
        self.registro.setText("")
        self.baraja.reiniciar()
        self.posicionarBaraja()
        self.repartoInicial()

    def repartoInicial(self):
        self.puntosJugador = []
        self.manoJugador = []

        self.manoBanca = []
        self.puntosBanca = []

        # Bloqueamos los botones de acción
        self.btnPedir.setEnabled(False)
        self.btnPlantar.setEnabled(False)
        self.btnReiniciar.setEnabled(False)

        # Repartimos dos cartas al jugador
        QtCore.QTimer.singleShot(500, partial(self.repartirCarta, "jugador"))
        QtCore.QTimer.singleShot(750, partial(self.repartirCarta, "jugador"))
        # Repartimos dos cartas a la banca, una se dejará oculta
        QtCore.QTimer.singleShot(1250, partial(self.repartirCarta, "banca"))
        QtCore.QTimer.singleShot(1500, partial(self.repartirCarta, "banca", False))

        # Reactivamos los botones de acción
        QtCore.QTimer.singleShot(2500, partial(self.btnPedir.setEnabled, True))
        QtCore.QTimer.singleShot(2500, partial(self.btnPlantar.setEnabled, True))
        QtCore.QTimer.singleShot(2500, partial(self.btnReiniciar.setEnabled, True))

        self.registro.append(f"= Empieza el Blackjack =")

    def repartirCarta(self, mano, voltear=True):
        carta = self.baraja.extraer()
        if carta:
            if mano == "jugador":
                self.manoJugador.append(carta)
                offset_x = len(self.manoJugador) * 40
                carta.moverAnimado(200+offset_x, 320, 750)
            elif mano == "banca":
                self.manoBanca.append(carta)
                offset_x = len(self.manoBanca) * 25
                carta.moverAnimado(255+offset_x, 110, 750, 0.8)
            carta.sobreponer()
            if voltear:
                carta.mostrar()
        self.computarMarcador()

    def computarMarcador(self):
        self.puntosJugador = self.calcularMarcador(self.manoJugador)
        self.marcadorJugador.setText(f"{self.puntosJugador}")
        self.puntosBanca = self.calcularMarcador(self.manoBanca)
        self.marcadorBanca.setText(f"{self.puntosBanca}")

        # Actualizamos el registro inicialmente
        self.registro.append(f"Jugador [{self.puntosJugador}], Banca [{self.puntosBanca}]")
        self.registro.verticalScrollBar().setValue(self.registro.verticalScrollBar().maximum())  # Scroll abajo del todo automático

    def calcularMarcador(self, mano):
        puntos = 0
        # Primero sumamos las cartas visibles que no son ases
        for carta in mano:
            if carta.visible:
                if carta.nombre not in ["As", "Jota", "Reina", "Rey"]:
                    puntos += carta.numero
                elif carta.nombre in ["Jota", "Reina", "Rey"]:
                    puntos += 10

        # Luego sumamos los ases visibles para adaptarlos a las necesidades
        for carta in mano:
            if carta.visible:
                if carta.nombre == "As":
                    # Sumamos el as como 11 siempre que sumemos 21 puntos o menos
                    if puntos + 11 <= 21:
                        puntos += 11
                    # Si superamos los 21 puntos lo sumamos valiendo 1
                    else:
                        puntos += 1
        return puntos

    def pedir(self):
        pass

    def plantar(self):
        pass

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
    sys.exit(app.exec_())
