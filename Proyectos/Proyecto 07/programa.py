from PySide6 import QtWidgets, QtCore
from ui_monitor import Ui_MainWindow
from functools import partial
from helpers import absPath
import os
import random
# Instalar todas las dependencias
# pip install pyqtgraph pandas jinja2 pdfkit
import pyqtgraph as pg
import pyqtgraph.exporters
import pandas as pd
import jinja2
import pdfkit
# Binarios para pdfkit (instalar y reiniciar VSC)
# Linux: sudo apt-get install wkhtmltopdf
# Windows: https://wkhtmltopdf.org/downloads.html#stable
# En Windows hay qñadir directorio /bin al PATH


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Datos iniciales
        self.sondas = [
            {"nombre": "Sonda 1", "valores": [], "col": "#ff2e00", "sim": "o"},
            {"nombre": "Sonda 2", "valores": [], "col": "#3498db", "sim": "s"},
            {"nombre": "Sonda 3", "valores": [], "col": "#00ff08", "sim": "t"},
            {"nombre": "Sonda 4", "valores": [], "col": "#ffa500", "sim": "p"},
        ]

        # Añadimos al combobox las sondas disponibles
        for sonda in self.sondas:
            self.comboBox.addItem(sonda["nombre"])

        # Construimos el gráfico
        self.construirGrafico()

        # Configuramos las señales (el botón tiene min/max en diseño)
        self.pushButton.clicked.connect(self.nuevaLectura)
        self.pushButton_2.clicked.connect(partial(self.nuevaLectura, True))

    def construirGrafico(self):
        self.widget.addLegend()
        self.graficos = []
        for sonda in self.sondas:
            plot = self.widget.plot(sonda["valores"], name=sonda["nombre"], pen=pg.mkPen(sonda["col"], width=3),
                                    symbol=sonda["sim"], symbolBrush=sonda["col"], symbolSize=12)
            self.graficos.append(plot)
        self.widget.setBackground("w")
        self.widget.showGrid(x=True, y=True)
        self.widget.setYRange(-20, 30)  # self.widget.setXRange(0, 10)
        self.widget.setTitle("Gráfico de temperaturas", size="20px")
        styles = {"color": "#000", "font-size": "16px"}
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
