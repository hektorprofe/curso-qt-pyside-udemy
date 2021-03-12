import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QMenu
from PySide6.QtCore import QEvent


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        lista = QListWidget()
        lista.addItems(["Opción 1", "Opción 2", "Opción 3"])
        lista.installEventFilter(self)

        self.setCentralWidget(lista)

        self.lista = lista

    def eventFilter(self, source, event):
        if (event.type() == QEvent.ContextMenu and
                source is self.lista):
            menu = QMenu()
            menu.addAction("Debugear QListItem")
            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                print(item.text())
            return True
        return super().eventFilter(source, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
