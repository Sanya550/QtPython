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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QTableView,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.openFile = QPushButton(Widget)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(0, 0, 131, 24))
        self.showData = QPushButton(Widget)
        self.showData.setObjectName(u"showData")
        self.showData.setGeometry(QRect(0, 250, 75, 24))
        self.graphDiagramRozkid = QPushButton(Widget)
        self.graphDiagramRozkid.setObjectName(u"graphDiagramRozkid")
        self.graphDiagramRozkid.setGeometry(QRect(330, 60, 181, 24))
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 30, 281, 211))
        self.showSummaryStatistics = QPushButton(Widget)
        self.showSummaryStatistics.setObjectName(u"showSummaryStatistics")
        self.showSummaryStatistics.setGeometry(QRect(80, 250, 141, 24))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 10, 171, 16))
        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(530, 30, 42, 22))
        self.spinBox.setMinimum(1)
        self.graphHystograma = QPushButton(Widget)
        self.graphHystograma.setObjectName(u"graphHystograma")
        self.graphHystograma.setGeometry(QRect(330, 30, 181, 24))
        self.openImage = QPushButton(Widget)
        self.openImage.setObjectName(u"openImage")
        self.openImage.setGeometry(QRect(0, 330, 131, 24))
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(140, 330, 451, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.width_picture = QLabel(Widget)
        self.width_picture.setObjectName(u"width_picture")
        self.width_picture.setGeometry(QRect(10, 370, 121, 16))
        self.height_picture = QLabel(Widget)
        self.height_picture.setObjectName(u"height_picture")
        self.height_picture.setGeometry(QRect(10, 400, 121, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.openFile.setText(QCoreApplication.translate("Widget", u"Open txt", None))
        self.showData.setText(QCoreApplication.translate("Widget", u"Show Data", None))
        self.graphDiagramRozkid.setText(QCoreApplication.translate("Widget", u"\u0413\u0440\u0430\u0444\u0456\u043a \u0434\u0456\u0430\u0433\u0440\u0430\u043c \u0440\u043e\u0437\u043a\u0438\u0434\u0443", None))
        self.showSummaryStatistics.setText(QCoreApplication.translate("Widget", u"Show Main characteristic", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0413\u0440\u0430\u0444\u0456\u043a\u0438:", None))
        self.graphHystograma.setText(QCoreApplication.translate("Widget", u"\u0413\u0456\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u0430", None))
        self.openImage.setText(QCoreApplication.translate("Widget", u"Open image", None))
        self.width_picture.setText("")
        self.height_picture.setText("")
    # retranslateUi

