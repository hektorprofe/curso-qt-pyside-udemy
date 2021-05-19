import sys
import time
from PySide6 import QtWidgets, QtCore
from ui_interfaz import Ui_MainWindow
from pyquery import PyQuery as pq  # pip install pyquery


def horaISO():
    hora = QtCore.QTime.currentTime()
    return hora.toString(QtCore.Qt.ISODateWithMs)


class WorkerSignals(QtCore.QObject):
    finished = QtCore.Signal(str, object)
    error = QtCore.Signal(str, object)


class Worker(QtCore.QRunnable):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.signals = WorkerSignals()

    @QtCore.Slot()
    def run(self):
        time.sleep(5)
        try:
            doc = pq(url=self.url)
        except Exception as error:
            self.signals.error.emit(self.url, error)
        else:
            self.signals.finished.emit(self.url, doc)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.scrappearWebConcurrente)
        self.threadPool = QtCore.QThreadPool()
        print(f"Multithreading con máximo {self.threadPool.maxThreadCount()}")

    def reiniciar(self):
        self.title.setText("")
        self.language.setText("")
        self.viewport.setText("")
        self.author.setText("")
        self.description.setPlainText("")

    def scrappearWeb(self):
        url = self.url.text()
        print(f"{horaISO()} (Req) {url}")
        time.sleep(5)
        try:
            doc = pq(url=url)
        except Exception as error:
            self.scrapeoFallido(url, error)
        else:
            self.scrapeoCompletado(url, doc)

    def scrappearWebConcurrente(self):
        url = self.url.text()
        print(f"{horaISO()} (Req) {url}")
        # viene la logica del scrapeo concurrente
        worker = Worker(url=url)
        worker.signals.finished.connect(self.scrapeoCompletado)
        worker.signals.error.connect(self.scrapeoFallido)
        # enviar el trabajador worker al threadpool
        self.threadPool.start(worker)

    def scrapeoFallido(self, url, error):
        self.reiniciar()
        print(f"{horaISO()} (Err) {url} {error}")

    def scrapeoCompletado(self, url, doc):
        self.reiniciar()
        print(f"{horaISO()} (Suc) {url}")
        self.title.setText(doc("title").text())
        self.language.setText(doc("html").attr("lang"))
        self.viewport.setText(doc("meta[name=viewport]").attr("content"))
        self.author.setText(doc("meta[name=author]").attr("content"))
        self.description.setPlainText(doc("meta[name=description]").attr("content"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
