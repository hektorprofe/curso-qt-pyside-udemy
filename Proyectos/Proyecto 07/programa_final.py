from PySide6 import QtWidgets, QtCore
from ui_monitor import Ui_MainWindow
from functools import partial
from helpers import absPath
import random
import pyqtgraph as pg  # pip install pyqtgraph
import pyqtgraph.exporters
import pandas as pd  # pip install pandas
import jinja2  # pip install jinja2
import pdfkit  # pip install pdfkit (instalar binarios y reiniciar VSC)
import os

# Linux: sudo apt-get install wkhtmltopdf
# Windows: https://wkhtmltopdf.org/downloads.html#stable


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Datos iniciales
        self.sondas = [
            {"nombre": "Sonda 1", "valores": [], "color": "r", "simbolo": "o"},
            {"nombre": "Sonda 2", "valores": [], "color": "b", "simbolo": "s"},
            {"nombre": "Sonda 3", "valores": [], "color": "g", "simbolo": "t"},
            {"nombre": "Sonda 4", "valores": [], "color": "#ffa500", "simbolo": "p"},
        ]

        # Añadimos al combobox las sondas disponibles
        for sonda in self.sondas:
            self.comboBox.addItem(sonda["nombre"])

        # Construimos el gráfico
        self.construirGrafico()

        # Configuraciones estáticas de la tabla
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(len(self.sondas))
        self.tableWidget.setVerticalHeaderLabels(
            [sonda["nombre"] for sonda in self.sondas])

        # Configuramos las señales (el botón tiene min/max en diseño)
        self.pushButton.clicked.connect(self.nuevaLectura)
        self.pushButton_2.clicked.connect(partial(self.nuevaLectura, True))
        self.pushButton_3.clicked.connect(partial(self.generarReporte))
        self.pushButton_4.clicked.connect(self.exportarPDF)

    def construirGrafico(self):
        self.widget.addLegend()
        self.graficos = []
        for sonda in self.sondas:
            plot = self.widget.plot(sonda["valores"], name=sonda["nombre"],
                                    pen=pg.mkPen(sonda["color"], width=3),
                                    symbol=sonda["simbolo"],
                                    symbolBrush=sonda["color"], symbolSize=12)
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

        # Actualizamos y dibujamos la tabla después de añadir algún valor
        self.dibujarTabla()

    def dibujarTabla(self):
        # Adaptamos la tabla verticalmente a partir de la sonda con más valores
        n_columnas = max([len(sonda["valores"]) for sonda in self.sondas])
        self.tableWidget.setColumnCount(n_columnas)
        self.tableWidget.setHorizontalHeaderLabels([f"{h}" for h in range(0, n_columnas)])
        # Dibujamos las celdas de la tabla
        for i, sonda in enumerate(self.sondas):
            for j, temp in enumerate(sonda["valores"]):
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, temp)
                self.tableWidget.setItem(i, j, item)

    def generarReporte(self):
        try:
            # Exportamos la imagen del gráfico
            # https://pyqtgraph.readthedocs.io/en/latest/exporting.html
            exporter = pg.exporters.ImageExporter(self.widget.plotItem)
            exporter.export(absPath('plot.png'))
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
            df = pd.DataFrame([sonda["valores"] for sonda in self.sondas],       # n_columnas = max([len(sonda["valores"]) for sonda in self.sondas])
                              index=[sonda["nombre"] for sonda in self.sondas])  # columns=[f"{h}" for h in range(0, n_columnas)])
            # print(df)
            # Generamos el HTML usando Jinja
            env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=absPath('plantillas')))
            template = env.get_template('template_final.html')
            # html = template.render(tabla=df.style.render())
            # Estilos: https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html#Building-styles
            styler = df.style.applymap(lambda valor: 'color: red' if valor < 0 else 'color: black')
            html = template.render(tabla=styler.render())
            # Generamos el HTML
            with open(absPath('reporte.html'), 'w') as f:
                f.write(html)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ups", "Error generando HTML" f"\n\n{e}")
        else:
            self.statusBar.showMessage("Reporte HTML generado")

    def exportarPDF(self):
        # Generamos el reporte HTML
        self.generarReporte()
        try:
            # Lo transformamos a PDF
            options = {'enable-local-file-access': None}
            pdfkit.from_file(absPath('reporte.html'), absPath('reporte.pdf'), options=options)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ups", "Error generando PDF" f"\n\n{e}")
        else:
            self.statusBar.showMessage("Reporte PDF generado")
            # Abrimos el PDF con el programa por defecto del sistema
            os.startfile(absPath('reporte.pdf'), 'open')


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
