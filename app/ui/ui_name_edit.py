# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'name_edit_input.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_NameEdit(object):
    def setupUi(self, NameEdit):
        if not NameEdit.objectName():
            NameEdit.setObjectName(u"NameEdit")
        NameEdit.resize(1110, 64)
        NameEdit.setStyleSheet(u"* {\n"
"	background: #fff;\n"
"	color: black;\n"
"}")
        self.horizontalLayout = QHBoxLayout(NameEdit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_label = QLabel(NameEdit)
        self.name_label.setObjectName(u"name_label")
        font = QFont()
        font.setPointSize(18)
        self.name_label.setFont(font)

        self.horizontalLayout.addWidget(self.name_label)

        self.name_input = QLineEdit(NameEdit)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(510, 0))
        self.name_input.setMaximumSize(QSize(510, 16777215))
        self.name_input.setFont(font)

        self.horizontalLayout.addWidget(self.name_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_name_button = QPushButton(NameEdit)
        self.update_name_button.setObjectName(u"update_name_button")
        self.update_name_button.setFont(font)

        self.horizontalLayout.addWidget(self.update_name_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.horizontalLayout.setStretch(3, 1)

        self.retranslateUi(NameEdit)

        QMetaObject.connectSlotsByName(NameEdit)
    # setupUi

    def retranslateUi(self, NameEdit):
        NameEdit.setWindowTitle(QCoreApplication.translate("NameEdit", u"Form", None))
        self.name_label.setText(QCoreApplication.translate("NameEdit", u"Name:", None))
        self.update_name_button.setText(QCoreApplication.translate("NameEdit", u"Update Name", None))
    # retranslateUi
