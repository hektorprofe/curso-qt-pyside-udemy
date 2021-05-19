from PySide6 import QtWidgets
from ui_monitor import Ui_MainWindow
from functools import partial
import pyqtgraph as pg  # pip install pyqtgraph
import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Datos iniciales
        self.sondas = [
            {"nombre": "Sonda 1", "valores": [], "color": "r", "simbolo": "o"},
            {"nombre": "Sonda 2", "valores": [], "color": "b", "simbolo": "o"},
            {"nombre": "Sonda 3", "valores": [], "color": "g", "simbolo": "o"},
        ]

        # Añadimos al combobox las sondas disponibles
        for sonda in self.sondas:
            self.comboBox.addItem(sonda["nombre"])

        # Construimos el gráfico
        self.construirGrafico()

        # Configuramos las señales (el botón tiene min/max en diseño)
        self.pushButton.clicked.connect(self.nuevaLectura)
        self.pushButton_2.clicked.connect(partial(self.nuevaLectura, True))

        # Documentación: http://pyqtgraph.org/
        # Simbolos: https://www.geeksforgeeks.org/pyqtgraph-symbols/
        # Ejemplos interactivos: python -m pyqtgraph.examples

    def construirGrafico(self):
        # configuración base
        self.widget.addLegend()

        # creamos un almacén para los gráficos (cada línea es un gráfico)
        self.graficos = []
        for sonda in self.sondas:
            plot = self.widget.plot(sonda["valores"], name=sonda["nombre"],
                                    pen=pg.mkPen(sonda["color"], width=3),
                                    symbol=sonda["simbolo"],
                                    symbolBrush=sonda["color"], symbolSize=12)
            self.graficos.append(plot)

        # estilos del gráfico
        self.widget.setBackground("w")
        self.widget.showGrid(x=True, y=True)
        self.widget.setYRange(-20, 30)  # self.widget.setXRange(0, 10)
        self.widget.setTitle("Monitor de temperaturas", size="24px")

        styles = {"color": "#000", "font-size": "20px"}
        self.widget.setLabel("left", "Temperaturas (ºC)", **styles)
        self.widget.setLabel("bottom", "Horas (H)", **styles)

    def nuevaLectura(self, autogenerar=False):
        if not autogenerar:
            # recuperamos la sonda y el valor
            indice = self.comboBox.currentIndex()
            temperatura = self.spinBox.value()
            # los añadimos a los datos y actualizamos el gráfico
            self.sondas[indice]["valores"].append(temperatura)
            # actualizamos el gráfico con los nuevos datos
            self.graficos[indice].setData(self.sondas[indice]["valores"])
        else:
            for indice, sonda in enumerate(self.sondas):
                temperatura = random.randint(-20, 30)
                sonda["valores"].append(temperatura)
                # actualizamos todos los gráficos con los nuevos datos
                self.graficos[indice].setData(sonda["valores"])


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
