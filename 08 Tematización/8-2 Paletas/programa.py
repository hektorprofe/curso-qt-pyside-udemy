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

    # dark fusion https://gist.github.com/lschmierer/443b8e21ad93e2a2d7eb
    app.setStyle("Fusion")
    dark_fusion = QPalette()
    dark_fusion.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.WindowText, Qt.white)
    dark_fusion.setColor(QPalette.Base, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    dark_fusion.setColor(QPalette.ToolTipText, Qt.white)
    dark_fusion.setColor(QPalette.Text, Qt.white)
    dark_fusion.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ButtonText, Qt.white)
    dark_fusion.setColor(QPalette.BrightText, Qt.red)
    dark_fusion.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_fusion.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_fusion.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    dark_fusion.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
    dark_fusion.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    dark_fusion.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))

    # activamos la paleta en la aplicación
    app.setPalette(dark_fusion)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
