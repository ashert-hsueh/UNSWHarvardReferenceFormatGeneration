import sys

from myui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to functions
        self.convert.clicked.connect(self.onConvertClicked)
        self.copyButton.clicked.connect(self.onCopyClicked)

    def onConvertClicked(self):
        # For now, just show a message - conversion logic will be added later
        self.msg.setText("Conversion functionality will be implemented soon!")

    def onCopyClicked(self):
        # Copy the content of the output text area to clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(self.harvardTextBox.toPlainText())

        # Show a temporary message
        original_msg = self.msg.text()
        self.msg.setText("✓ Copied to clipboard!")

        # Reset message after 2 seconds
        from PySide6.QtCore import QTimer

        QTimer.singleShot(2000, lambda: self.msg.setText(original_msg))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
