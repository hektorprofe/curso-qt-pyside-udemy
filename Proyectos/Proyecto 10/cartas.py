from PySide6 import QtCore, QtGui, QtWidgets
from helpers import absPath
import random


class Carta(QtWidgets.QLabel):
    def __init__(self, imagenPath, numero, nombre, palo, parent=None):
        super().__init__(parent)
        self.imagenPath = imagenPath
        self.numero = numero
        self.nombre = nombre
        self.palo = palo
        self.visible = False

        self.imagen = QtGui.QPixmap(absPath("images/Reverso.png"))
        self.setPixmap(self.imagen)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Fix Alpha
        self.setScaledContents(True)  # Escalar el pixmap al widget

        self.anchoBase = self.sizeHint().width()
        self.altoBase = self.sizeHint().height()

        # grupo de animaciones
        self.animaciones = QtCore.QParallelAnimationGroup()

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
        mover = QtCore.QPropertyAnimation(self, b"pos")
        mover.setEndValue(QtCore.QPoint(x, y))
        mover.setDuration(duracion)
        self.animaciones.addAnimation(mover)
        escalar = QtCore.QPropertyAnimation(self, b"size")
        escalar.setEndValue(QtCore.QSize(self.anchoBase * escalado, self.altoBase * escalado))
        escalar.setDuration(duracion)
        self.animaciones.addAnimation(escalar)
        self.animaciones.start()

    def reestablecer(self):
        self.animaciones.stop()
        self.animaciones = QtCore.QParallelAnimationGroup()
        self.resize(self.anchoBase, self.altoBase)

    def mousePressEvent(self, event):  # Debug
        if self.visible:
            print(f"{self.nombre} de {self.palo}")


class Baraja(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        nombres = ["As", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Jota", "Reina", "Rey"]
        palos = ["Tréboles", "Diamantes", "Corazones", "Picas"]
        self.cartas = []
        self.jugadas = []
        for palo in palos:
            for i, nombre in enumerate(nombres):
                carta = Carta(f"{i+1}{palo[0]}", i+1, nombre, palo, self)
                self.cartas.append(carta)
        self.mezclar()

    def mezclar(self):
        random.shuffle(self.cartas)

    def extraer(self):
        if len(self.cartas) > 0:
            carta = self.cartas.pop()
            self.jugadas.append(carta)
            return carta
        return None

    def reiniciar(self):
        for carta in self.jugadas:
            carta.esconder()
            carta.reestablecer()
            self.cartas.append(carta)
        self.jugadas = []
        self.mezclar()
