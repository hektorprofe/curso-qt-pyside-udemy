# Tablero Kanban en CSV usando listas y un menú contextual

https://doc.qt.io/qtforpython/PySide6/QtWidgets/QListWidget
https://doc.qt.io/qtforpython/PySide6/QtWidgets/QListWidgetItem.html
https://doc.qt.io/qtforpython/PySide6/QtCore/QObject.html#PySide6.QtCore.PySide6.QtCore.QObject.eventFilter

Debugeando menú contextual y elemento de lista:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QListWidgetItem
from PySide6.QtCore import Qt, QEvent
from helpers import absPath
from ui_kanban import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Reseteamos los items de las tres listas
        self.lista_Pendientes.clear()
        self.lista_EnProgreso.clear()
        self.lista_Completadas.clear()

        # Creamos alguna tareas propias para trastear
        pendientes = ["Tarea de prueba 1",
                      "Tarea de prueba 2",
                      "Tarea de prueba 3"]
        for pendiente in pendientes:
            item = QListWidgetItem(pendiente)
            item.setTextAlignment(Qt.AlignCenter)
            self.lista_Pendientes.addItem(item)

        # Conifiguramos las señales de doble clic en las listas
        self.lista_Pendientes.itemDoubleClicked.connect(self.actualizarTarea)
        self.lista_EnProgreso.itemDoubleClicked.connect(self.actualizarTarea)
        self.lista_Completadas.itemDoubleClicked.connect(self.actualizarTarea)

        # Configuramos el menú contextual en las listas
        self.lista_Pendientes.installEventFilter(self)
        self.lista_EnProgreso.installEventFilter(self)
        self.lista_Completadas.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.ContextMenu):
            # Recuperamos el item clicado
            item = source.itemAt(event.pos())
            # mostrar menu sobre el item
            menu = QMenu()
            menu.addAction("Debugear", lambda: self.debugearTarea(item))
            if menu.exec_(event.globalPos()):
                return True
        return super().eventFilter(source, event)

    def actualizarTarea(self, item):
        print(item.text())

    def debugearTarea(self, item):
        if isinstance(item, QListWidgetItem):
            print(item.text())
```
