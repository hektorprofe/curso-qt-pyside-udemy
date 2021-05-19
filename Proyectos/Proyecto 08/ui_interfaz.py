# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazUQMWXG.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(480, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(480, 230))
        MainWindow.setMaximumSize(QSize(480, 230))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")

        self.horizontalLayout_2.addWidget(self.url)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.language = QLineEdit(self.centralwidget)
        self.language.setObjectName(u"language")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(40)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.language.sizePolicy().hasHeightForWidth())
        self.language.setSizePolicy(sizePolicy1)
        self.language.setMinimumSize(QSize(40, 0))
        self.language.setMaximumSize(QSize(40, 16777215))
        self.language.setReadOnly(True)

        self.gridLayout.addWidget(self.language, 2, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.viewport = QLineEdit(self.centralwidget)
        self.viewport.setObjectName(u"viewport")
        self.viewport.setReadOnly(True)

        self.gridLayout.addWidget(self.viewport, 2, 4, 1, 1)

        self.author = QLineEdit(self.centralwidget)
        self.author.setObjectName(u"author")
        self.author.setReadOnly(True)

        self.gridLayout.addWidget(self.author, 5, 2, 1, 3)

        self.description = QPlainTextEdit(self.centralwidget)
        self.description.setObjectName(u"description")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(60)
        sizePolicy2.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy2)
        self.description.setMaximumSize(QSize(16777215, 60))
        self.description.setReadOnly(True)

        self.gridLayout.addWidget(self.description, 6, 2, 1, 3)

        self.title = QLineEdit(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setReadOnly(True)

        self.gridLayout.addWidget(self.title, 0, 2, 1, 3)


        self.verticalLayout_3.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Web Scrapper Concurrente", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.url.setText(QCoreApplication.translate("MainWindow", u"https://docs.hektorprofe.net/qt-pyside/", None))
        self.url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.ejemplo.com", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Scrappear", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Viewport", None))
    # retranslateUi

