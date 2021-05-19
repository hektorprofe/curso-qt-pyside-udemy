from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenu, QListWidgetItem, QInputDialog)
from PySide6.QtCore import Qt, QEvent
from ui_kanban import Ui_MainWindow
from helpers import *
import csv


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # creamos una lista de listas para manejarlas dinámicamente
        self.listas = [self.lista_Pendientes,
                       self.lista_EnProgreso,
                       self.lista_Completadas]

        for lista in self.listas:
            # Reseteamos los items de las tres listas
            lista.clear()
            # Configuramos las listas señales de doble clic en las listas
            lista.itemDoubleClicked.connect(self.actualizarTarea)
            # configuramos el menú contextual en las listas
            lista.installEventFilter(self)

        # Cargamos los datos del fichero de tareas
        if existsFile(absPath("tareas.csv")):
            with open(absPath("tareas.csv"), newline="\n") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for lista, nombre in reader:
                    item = QListWidgetItem(nombre)
                    item.setTextAlignment(Qt.AlignCenter)
                    self.listas[int(lista)].addItem(item)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.ContextMenu):
            # creamos un menu conextual sobre el item
            menu = QMenu()
            menu.addAction("Añadir tarea", self.nuevaTarea)
            # Recuperamos el item clicado
            item = source.itemAt(event.pos())
            menu.addAction("Borrar tarea", lambda: self.borrarTarea(item))
            # lo mostramos en la posición donde se ha hecho clic derecho
            if menu.exec_(event.globalPos()):
                return True
        return super().eventFilter(source, event)

    def actualizarTarea(self, item):
        # recuperamos la lista contenedora
        lista = item.listWidget()
        # recuperamos el indice del item
        item_index = lista.row(item)
        # lo borramos de la lista
        lista.takeItem(item_index)
        # dependiendo de si la lista es pendiente o en progreso
        # recreamos el item de nuevo
        if lista == self.lista_Pendientes:
            self.lista_EnProgreso.addItem(item)
        elif lista == self.lista_EnProgreso:
            self.lista_Completadas.addItem(item)

    def debugearTarea(self, item):
        if isinstance(item, QListWidgetItem):
            print(item.text())

    def nuevaTarea(self):
        tarea, _ = QInputDialog.getText(self, "Tareas", "¿Nombre de la tarea?")
        if tarea:
            item = QListWidgetItem(tarea)
            item.setTextAlignment(Qt.AlignCenter)
            self.lista_Pendientes.addItem(item)

    def borrarTarea(self, item):
        if isinstance(item, QListWidgetItem):
            item_index = item.listWidget().row(item)
            item.listWidget().takeItem(item_index)

    def closeEvent(self, event):
        # recuperamos lo que hay en las listas y lo guardamos en una lista
        tareas = []
        for i, lista in enumerate(self.listas):
            for j in range(lista.count()):
                tareas.append([i, lista.item(j).text()])
        # escribimos las tareas en el fichero csv
        with open(absPath("tareas.csv"), "w", newline="\n") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerows(tareas)
        # procedemos con el cierre
        event.accept()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
