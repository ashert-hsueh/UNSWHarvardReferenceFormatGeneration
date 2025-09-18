import re
import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.input_label = QtWidgets.QLabel("APA Format Input:")
        self.input_box = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Generate Reference")
        self.text = QtWidgets.QLabel(
            "Generated Reference will appear here", alignment=QtCore.Qt.AlignCenter
        )

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.generate_reference)

    @QtCore.Slot()
    def generate_reference(self):
        apa_text = self.input_box.text()
        # A simple regex for Author, A. (Year). Title.
        pattern = re.compile(r"^[A-Za-z\s,]+\s[A-Z]\.\s\(\d{4}\)\.\s.+")
        if pattern.match(apa_text):
            self.text.setText(apa_text)
        else:
            self.text.setText("Invalid APA format.")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
