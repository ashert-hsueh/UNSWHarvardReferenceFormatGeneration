# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(800, 500))

        # Center the window on screen
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = MainWindow.geometry()
        MainWindow.move(
            (screen_geometry.width() - window_geometry.width()) // 2,
            (screen_geometry.height() - window_geometry.height()) // 2,
        )

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(15)

        # Horizontal layout for the two text areas
        self.textAreasLayout = QHBoxLayout()
        self.textAreasLayout.setObjectName("textAreasLayout")
        self.textAreasLayout.setSpacing(15)

        # Left side: BibTeX input area with layout
        self.inputGroup = QWidget()
        self.inputGroup.setObjectName("inputGroup")
        self.inputLayout = QVBoxLayout(self.inputGroup)
        self.inputLayout.setObjectName("inputLayout")
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.setSpacing(5)

        self.label_2 = QLabel(self.inputGroup)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inputLayout.addWidget(self.label_2)

        self.bibTexBox = QTextEdit(self.inputGroup)
        self.bibTexBox.setObjectName("bibTexBox")
        self.inputLayout.addWidget(self.bibTexBox)

        self.textAreasLayout.addWidget(self.inputGroup)

        # Right side: Harvard output area with layout and copy button
        self.outputGroup = QWidget()
        self.outputGroup.setObjectName("outputGroup")
        self.outputLayout = QVBoxLayout(self.outputGroup)
        self.outputLayout.setObjectName("outputLayout")
        self.outputLayout.setContentsMargins(0, 0, 0, 0)
        self.outputLayout.setSpacing(5)

        self.label_3 = QLabel(self.outputGroup)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.outputLayout.addWidget(self.label_3)

        # Output text area with copy button container
        self.outputTextContainer = QWidget()
        self.outputTextContainer.setObjectName("outputTextContainer")
        self.outputTextLayout = QVBoxLayout(self.outputTextContainer)
        self.outputTextLayout.setObjectName("outputTextLayout")
        self.outputTextLayout.setContentsMargins(0, 0, 0, 0)
        self.outputTextLayout.setSpacing(5)

        self.harvardTextBox = QTextEdit(self.outputTextContainer)
        self.harvardTextBox.setObjectName("harvardTextBox")
        self.harvardTextBox.setReadOnly(True)  # Make output read-only
        self.outputTextLayout.addWidget(self.harvardTextBox)

        # Copy button at bottom-right
        self.copyButtonLayout = QHBoxLayout()
        self.copyButtonLayout.setObjectName("copyButtonLayout")
        self.copyButtonLayout.addStretch()  # Push button to right

        self.copyButton = QPushButton(self.outputTextContainer)
        self.copyButton.setObjectName("copyButton")
        self.copyButtonLayout.addWidget(self.copyButton)

        self.outputTextLayout.addLayout(self.copyButtonLayout)
        self.outputLayout.addWidget(self.outputTextContainer)

        self.textAreasLayout.addWidget(self.outputGroup)
        self.mainLayout.addLayout(self.textAreasLayout)

        # Convert button centered at the bottom
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.buttonLayout.addStretch()

        self.convert = QPushButton(self.centralwidget)
        self.convert.setObjectName("convert")
        self.buttonLayout.addWidget(self.convert)

        self.buttonLayout.addStretch()
        self.mainLayout.addLayout(self.buttonLayout)

        # Message label
        self.msg = QLabel(self.centralwidget)
        self.msg.setObjectName("msg")
        self.msg.setMinimumSize(QSize(0, 30))
        self.msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.msg)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Apply UNSW branding colors
        self.applyUNSWBranding(MainWindow)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def applyUNSWBranding(self, MainWindow):
        # UNSW official brand colors (updated)
        unsw_yellow = QColor("#FFE600")  # Primary: UNSW Yellow
        unsw_charcoal = QColor("#231F20")  # Secondary: Charcoal
        unsw_light_grey = QColor("#F5F5F5")  # Light background for read-only

        # Set window title bar color (Windows only)
        try:
            MainWindow.setStyleSheet(
                f"""
                QMainWindow {{
                    background-color: #FFFFFF;
                }}
                QLabel {{
                    font-weight: 500;
                    color: {unsw_charcoal.name()};
                }}
                QPushButton {{
                    background-color: {unsw_yellow.name()};
                    color: {unsw_charcoal.name()};
                    border: 2px solid {unsw_charcoal.name()};
                    padding: 8px 24px;
                    font-weight: 600;
                    border-radius: 4px;
                }}
                QPushButton:hover {{
                    background-color: {unsw_charcoal.name()};
                    color: {unsw_yellow.name()};
                }}
                QPushButton:pressed {{
                    background-color: #{int(unsw_charcoal.rgb() & 0xFFFFFF) - 0x222222:06x};
                }}
                QTextEdit {{
                    border: 2px solid {unsw_charcoal.name()};
                    border-radius: 4px;
                    padding: 8px;
                    font-family: 'Courier New', monospace;
                    font-size: 10pt;
                }}
                QTextEdit:focus {{
                    border-color: {unsw_yellow.name()};
                    outline: none;
                }}
            """
            )
        except (TypeError, ValueError, AttributeError) as e:
            # Log style sheet errors but continue execution
            print(f"Warning: Could not apply complete styling: {e}", file=sys.stderr)

        # Set placeholder text for input text area
        self.bibTexBox.setPlaceholderText("Paste BibTeX Here")

        # Set read-only appearance for output text area
        palette = self.harvardTextBox.palette()
        palette.setColor(QPalette.ColorRole.Base, unsw_light_grey)
        self.harvardTextBox.setPalette(palette)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "UNSW Harvard Reference Generator", None
            )
        )
        self.msg.setText("")
        self.convert.setText(QCoreApplication.translate("MainWindow", "Convert", None))
        self.copyButton.setText(QCoreApplication.translate("MainWindow", "Copy", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "BibTeX Input", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow", "Harvard Reference (UNSW Style)", None
            )
        )

    # retranslateUi
