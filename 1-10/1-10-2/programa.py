from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class Window():
    def __init__(self, ui_file):
        self.window = QUiLoader().load(absPath(ui_file))
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window("main.ui")
    sys.exit(app.exec_())
