from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel, QRadioButton,
    QCheckBox, QLineEdit, QSpinBox, QPushButton, QPlainTextEdit, QVBoxLayout)
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class EditorQSS(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.resize(480, 320)
        self.setWindowTitle("Editor QSS en vivo")

        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet("""
            background-color: #212121;
            color: #e9e9e9;
            font-family: Consolas;
            font-size: 16px;
        """)
        self.editor.textChanged.connect(self.actualizar_estilos)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.show()

    def actualizar_estilos(self):
        qss = self.editor.toPlainText()
        try:
            self.parent.setStyleSheet(qss)
        except:
            pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()
        formulario.addRow("QCheckBox", QCheckBox())
        formulario.addRow("QRadioButton", QRadioButton())

        etiqueta = QLabel("QLabel")
        etiqueta.setObjectName("etiqueta")
        formulario.addRow(etiqueta)
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QSpinBox", QSpinBox())

        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)

        self.editorQSS = EditorQSS(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
