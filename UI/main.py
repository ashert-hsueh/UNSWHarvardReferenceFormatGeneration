import sys

from myui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

from FormatConvert.BibTex2Harvard import convert_to_harvard, parse_bibtex_from_text


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.convert.clicked.connect(self.handle_convert)

    def handle_convert(self):
        bib_text = self.bibTexBox.toPlainText()
        entries = parse_bibtex_from_text(bib_text)
        harvard_text = convert_to_harvard(entries)
        self.harvardTextBox.setPlainText(harvard_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
