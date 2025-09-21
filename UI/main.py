import sys

from myui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
