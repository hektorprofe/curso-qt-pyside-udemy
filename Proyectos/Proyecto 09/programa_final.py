# Widget para gestionar barajas de cartas con animaciones
# https://doc.qt.io/qtforpython/PySide6/QtCore/QPropertyAnimation.html

# Juego Blackjack usando nuestro widget de barajas de cartas
# https://en.wikipedia.org/wiki/Blackjack

from PySide6 import QtCore, QtGui, QtWidgets
from helpers import absPath
import random
import sys


class Carta(QtWidgets.QLabel):
    def __init__(self, imagenPath, numero, nombre, palo, parent=None):
        super().__init__(parent)
        self.imagenPath = imagenPath
        self.numero = numero
        self.nombre = nombre
        self.palo = palo
        self.visible = False

        # Gestión de la imagen
        self.imagen = QtGui.QPixmap(absPath("images/Reverso.png"))
        self.setPixmap(self.imagen)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Fix Alpha
        self.setScaledContents(True)  # Escalar el pixmap al widget

        self.anchoBase = self.sizeHint().width()
        self.altoBase = self.sizeHint().height()

        # grupo de animaciones
        self.animaciones = QtCore.QSequentialAnimationGroup()  # con esperas
        self.animaciones = QtCore.QParallelAnimationGroup()  # parelelas

    def mostrar(self):
        self.imagen = QtGui.QPixmap(absPath(f"images/{self.imagenPath}.png"))
        self.setPixmap(self.imagen)
        self.visible = True

    def esconder(self):
        self.imagen = QtGui.QPixmap(absPath("images/Reverso.png"))
        self.setPixmap(self.imagen)
        self.visible = False

    def sobreponer(self):
        self.raise_()

    def moverAnimado(self, x, y, duracion=1000, escalado=1):
        # Animación de movimiento
        # self.posAnim = QtCore.QPropertyAnimation(self, b"pos")
        # self.posAnim.setEndValue(QtCore.QPoint(x, y))
        # self.posAnim.setDuration(duracion * 1000)
        # self.posAnim.start()
        mover = QtCore.QPropertyAnimation(self, b"pos")
        mover.setEndValue(QtCore.QPoint(x, y))
        mover.setDuration(duracion)
        self.animaciones.addAnimation(mover)

        # Animación de reescalado
        escalar = QtCore.QPropertyAnimation(self, b"size")
        escalar.setEndValue(QtCore.QSize(self.anchoBase * escalado, self.altoBase * escalado))
        escalar.setDuration(duracion)
        self.animaciones.addAnimation(escalar)

        # Iniciamos las animaciones
        self.animaciones.start()

    def reestablecer(self):
        # Finalizamos las animaciones actuales
        # self.posAnim.stop()
        self.animaciones.stop()
        # Reiniciamos el grupo de animaciones
        self.animaciones = QtCore.QParallelAnimationGroup()
        # Y restauramos los tamaños
        self.resize(self.anchoBase, self.altoBase)

    def mousePressEvent(self, event):  # Debug
        if self.visible:
            print(f"{self.nombre} de {self.palo}")


class Baraja(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        nombres = ["As", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Jota", "Reina", "Rey"]
        palos = ["Tréboles", "Diamantes", "Corazones", "Picas"]
        self.cartas = []   # Lista de cartas en la pila
        self.jugadas = []  # Lista de cartas fuera de la pila
        for palo in palos:
            for i, nombre in enumerate(nombres):
                carta = Carta(f"{i+1}{palo[0]}", i+1, nombre, palo, self)
                self.cartas.append(carta)  # La añadimos a la lista
        self.mezclar()  # Mezclamos las cartas

    def mezclar(self):
        random.shuffle(self.cartas)

    def extraer(self):
        if len(self.cartas) > 0:
            carta = self.cartas.pop()  # sacamos la última carta (la de arriba)
            self.jugadas.append(carta)  # la añadimos a la lista de cartas jugadas
            return carta
        return None

    def reiniciar(self):
        for carta in self.jugadas:
            carta.esconder()  # escondemos las cartas jugadas
            carta.reestablecer()  # reestablecemos los tamaños y animaciones
            self.cartas.append(carta)  # recuperamos las cartas jugadas
        self.jugadas = []  # Borramos todas las cartas jugadas
        self.mezclar()  # Mezclamos la baraja


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(480, 320)
        self.setStyleSheet("QMainWindow {background-color: #144b12}")

        self.baraja = Baraja(self)
        self.setCentralWidget(self.baraja)
        self.posicionarBaraja()

        # Botones y señales
        tomar = QtWidgets.QPushButton("Tomar carta", self)
        tomar.move(365, 15)
        tomar.clicked.connect(self.tomarCarta)

        reiniciar = QtWidgets.QPushButton("Reiniciar juego", self)
        reiniciar.move(250, 15)
        reiniciar.clicked.connect(self.reiniciarJuego)

    def posicionarBaraja(self):
        offset = 0
        for carta in self.baraja.cartas:
            carta.move(40 + offset, 60 + offset)
            carta.sobreponer()  # upd: traemos las cartas al frente por orden
            offset += 0.25

    def tomarCarta(self):
        carta = self.baraja.extraer()
        if carta:
            carta.moverAnimado(300, 110, 750, 0.75)
            carta.sobreponer()  # raise trae al frente el widget
            carta.mostrar()

    def reiniciarJuego(self):
        self.baraja.reiniciar()
        self.posicionarBaraja()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
