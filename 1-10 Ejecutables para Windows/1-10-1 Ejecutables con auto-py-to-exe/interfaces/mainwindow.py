# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowiGfpKw.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(243, 135)
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/qt.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #282936;\n"
"	color: #ffffff;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: #282936;\n"
"	color: #ffffff;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"	background-color: #282936;\n"
"	color: #fff;\n"
"	border: 1px solid #282936;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #ffc80b;\n"
"	color: #000000;\n"
"	font-weight: bold;\n"
"	border: 0px solid;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #ffe152;  \n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #e5c010;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	background-color: #e5c010;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #ffc80b;\n"
"	color: #000000;\n"
"	font-"
                        "weight: bold;\n"
"	border: 0px solid;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #ffe152;  \n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #e5c010;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::checked\n"
"{\n"
"	background-color: #e5c010;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: white;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	border: 0px solid;\n"
"	border-radius: 2px;\n"
"	selection-background-color: #0949ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::focus\n"
"{\n"
"	padding: 3px;\n"
"	border: 1px solid #0949ff;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit\n"
"{\n"
"	background-color: white;\n"
"	color: #000;\n"
"	border-color: #000000;\n"
"	border: 0px solid;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"	background-color: #3a3a4e;\n"
"	color: #fff;\n"
"	border: 0px solid;\n"
"	border-radius:"
                        " 2px;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    border: 1px solid #ffc80b;\n"
"    border: none;\n"
"    color: #000;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #ffc80b;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #ffc80b;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover \n"
"{\n"
"    background-color: #282936;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:vertical \n"
"{\n"
"   border: none;\n"
"   width: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal \n"
"{\n"
"   border: none;\n"
"   height: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"   border: none;\n"
"   border-radius : 0px;\n"
"   background-color: #ffc80b;\n"
""
                        "   min-height: 80px;\n"
"   width : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"   background-color: #e5c010; \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:horizontal:hover\n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed, \n"
"QScrollBar::add-line:horizontal:pressed\n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:horizontal:hover\n"
"{\n"
"   background-color"
                        ": transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed,\n"
"QScrollBar::sub-line:horizontal:pressed\n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::up-arrow:horizontal\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical, \n"
"QScrollBar::down-arrow:horizontal\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"   background-color: white;\n"
"	\n"
"}\n"
"")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/recursos/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSalir.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 243, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Primer dise\u00f1o", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"&Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Introduce un nuevo texto", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Soy un campo de texto", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Soy un bot\u00f3n", None))
#endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

