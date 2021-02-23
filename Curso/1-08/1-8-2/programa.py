from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        formulario = QFormLayout()
        formulario.addRow("QCheckBox", QCheckBox())
        formulario.addRow("QRadioButton", QRadioButton())
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QDateEdit", QDateEdit())
        formulario.addRow("QDateTimeEdit", QDateTimeEdit())
        formulario.addRow("QSpinBox", QSpinBox())
        formulario.addRow("QDoubleSpinBox", QDoubleSpinBox())
        formulario.addRow("QComboBox", QComboBox())
        formulario.addRow("QFontComboBox", QFontComboBox())
        formulario.addRow("QProgressBar", QProgressBar())
        formulario.addRow("QLCDNumber", QLCDNumber())
        formulario.addRow("QSlider", QSlider(Qt.Horizontal))
        formulario.addRow("QDial", QDial())
        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
