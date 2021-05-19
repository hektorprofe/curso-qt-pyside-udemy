import sys
import time
from PySide6 import QtWidgets, QtCore
from ui_interfaz import Ui_MainWindow
from pyquery import PyQuery as pq  # pip install pyquery


def horaISO():
    hora = QtCore.QTime.currentTime()
    return hora.toString(QtCore.Qt.ISODateWithMs)


class WorkerSignals(QtCore.QObject):
    # WorkerSignals contiene la estructura de las señales que se emitirán
    # Heredamos de QObject para pdoer conectar las señales
    finished = QtCore.Signal(str, object)
    error = QtCore.Signal(str, object)


class Worker(QtCore.QRunnable):
    # Worker es el encargado de ejecutar la tarea asíncrona
    # Emitirá señales que se mapearán a la interfaz
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.signals = WorkerSignals()

    @QtCore.Slot()
    def run(self):
        time.sleep(5)  # Simulación de bloqueo durante 5 segundos
        try:
            doc = pq(url=self.url)
            self.signals.finished.emit(self.url, doc)
        except Exception as error:
            self.signals.error.emit(self.url, error)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.scrappearWebConcurrente)

        # Configuramos la pool de hilos
        self.threadpool = QtCore.QThreadPool()
        print("Multithreading con un máximo de %d hilos" % self.threadpool.maxThreadCount())

    def reiniciar(self):
        self.title.setText("")
        self.language.setText("")
        self.viewport.setText("")
        self.author.setText("")
        self.description.setPlainText("")

    def scrappearWeb(self):
        url = self.url.text()
        print(f"{horaISO()} (Req) {url}")
        try:
            time.sleep(5)  # Simulación de bloqueo durante 5 segundos
            doc = pq(url=url)
        except Exception as error:
            self.scrapeoFallido(url, error)
        else:
            self.scrapeoCompletado(url, doc)

    def scrapeoFallido(self, url, error):
        self.reiniciar()
        print(f"{horaISO()} (Err) {url} {error}")

    def scrapeoCompletado(self, url, doc):
        self.reiniciar()
        self.title.setText(doc("title").text())
        self.language.setText(doc("html").attr("lang"))
        self.viewport.setText(doc("meta[name=viewport]").attr("content"))
        self.author.setText(doc("meta[name=author]").attr("content"))
        self.description.setPlainText(doc("meta[name=description]").attr("content"))
        print(f"{horaISO()} (Suc) {url}")

    def scrappearWebConcurrente(self):
        url = self.url.text()
        print(f"{horaISO()} (Req) {url}")
        # Instanicamos el trabajador y configuramos sus señales concurrentes
        worker = Worker(url=url)
        worker.signals.finished.connect(self.scrapeoCompletado)
        worker.signals.error.connect(self.scrapeoFallido)
        # Iniciamos el trabajador en la pool de hilos
        self.threadpool.start(worker)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# PyQuery: https://pythonhosted.org/pyquery/index.html
# QRunnable: https://doc.qt.io/qtforpython/PySide6/QtCore/QRunnable.html
# QThread: https://doc.qt.io/qtforpython/PySide6/QtCore/QThreadPool.html
# Signal: https://doc.qt.io/qtforpython/PySide6/QtCore/Signal.html
# QTime (Hora) https://doc.qt.io/qtforpython/PySide6/QtCore/QTime.html