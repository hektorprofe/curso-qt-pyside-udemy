# Widget para gestionar barajas de cartas con animaciones
# https://doc.qt.io/qtforpython/PySide6/QtCore/QPropertyAnimation.html

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

    def posicionar(self, x, y):
        self.raise_()  # sobreponemos la carta
        self.move(x, y)

    def mover(self, x, y, duracion=1000, escalado=1):
        # Animación de movimiento
        self.raise_()  # sobreponemos la carta
        # self.posAnim = QtCore.QPropertyAnimation(self, b"pos")
        # self.posAnim.setEndValue(QtCore.QPoint(x, y))
        # self.posAnim.setDuration(duracion * 1000)
        # self.posAnim.start()
        pos = QtCore.QPropertyAnimation(self, b"pos")
        pos.setEndValue(QtCore.QPoint(x, y))
        pos.setDuration(duracion)
        self.animaciones.addAnimation(pos)

        # Animación de reescalado
        size = QtCore.QPropertyAnimation(self, b"size")
        size.setEndValue(QtCore.QSize(self.anchoBase * escalado, self.altoBase * escalado))
        size.setDuration(duracion)
        self.animaciones.addAnimation(size)

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
        self.preparar()

        # Botones y señales
        tomarBtn = QtWidgets.QPushButton("Tomar carta", self)
        tomarBtn.move(365, 15)
        tomarBtn.clicked.connect(self.tomar)

        reiniciarBtn = QtWidgets.QPushButton("Reiniciar juego", self)
        reiniciarBtn.move(250, 15)
        reiniciarBtn.clicked.connect(self.reiniciar)

    def preparar(self):
        offset = 0
        for carta in self.baraja.cartas:
            carta.posicionar(40 + offset, 60 + offset)
            offset += 0.25

    def tomar(self):
        carta = self.baraja.extraer()
        if carta:
            carta.mover(300, 110, 750, 0.75)
            carta.mostrar()

    def reiniciar(self):
        self.baraja.reiniciar()
        self.preparar()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # exec_() si PySide6 < 6.1.0 (pip install --upgrade pyside6)
    sys.exit(app.exec())
