# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.openFile = QPushButton(Widget)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(0, 0, 75, 24))
        self.showData = QPushButton(Widget)
        self.showData.setObjectName(u"showData")
        self.showData.setGeometry(QRect(0, 220, 75, 24))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 0, 75, 24))
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 31, 256, 181))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.openFile.setText(QCoreApplication.translate("Widget", u"Open", None))
        self.showData.setText(QCoreApplication.translate("Widget", u"Show Data", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
    # retranslateUi

