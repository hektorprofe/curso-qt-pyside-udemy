# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kanbanhhSrtK.ui'
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
        MainWindow.resize(682, 360)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color: white;\n"
"}\n"
"\n"
"QListWidget{\n"
"border: 0;\n"
"outline: 0;  /* Desactiva un outline dotted que hay por defecto*/\n"
"color: #090909;\n"
"font-size: 18px;\n"
"font-weight: 300;\n"
"background-color: white;\n"
"padding: 0px;\n"
"}\n"
"\n"
"QLabel {\n"
"padding: 10px;\n"
"font-size: 22px;\n"
"font-weight: 300;\n"
"}\n"
"\n"
"QListWidget::item { \n"
"padding: 0px;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"padding: 0px;\n"
"background-color: rgb(255, 235, 12);\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;\n"
"color: black;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"padding: 0px;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;\n"
"color: black;\n"
"}\n"
"\n"
"/* Items impares con fondo gris\n"
"QListWidget {\n"
"padding: 0px;\n"
"background-color: #DDDDDD;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;\n"
"color: black;\n"
"}*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Completadas = QLabel(self.centralwidget)
        self.label_Completadas.setObjectName(u"label_Completadas")
        font = QFont()
        font.setFamily(u"Roboto Light")
        font.setBold(False)
        font.setItalic(False)
        self.label_Completadas.setFont(font)
        self.label_Completadas.setStyleSheet(u"background-color: rgb(132, 255, 94);")
        self.label_Completadas.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Completadas, 1, 2, 1, 1)

        self.label_EnProgreso = QLabel(self.centralwidget)
        self.label_EnProgreso.setObjectName(u"label_EnProgreso")
        self.label_EnProgreso.setFont(font)
        self.label_EnProgreso.setStyleSheet(u"background-color: #FFAF3F;")
        self.label_EnProgreso.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_EnProgreso, 1, 1, 1, 1)

        self.label_Pendientes = QLabel(self.centralwidget)
        self.label_Pendientes.setObjectName(u"label_Pendientes")
        self.label_Pendientes.setFont(font)
        self.label_Pendientes.setStyleSheet(u"background-color: rgb(85, 170, 255)")
        self.label_Pendientes.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Pendientes, 1, 0, 1, 1)

        self.lista_EnProgreso = QListWidget(self.centralwidget)
        __qlistwidgetitem = QListWidgetItem(self.lista_EnProgreso)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.lista_EnProgreso)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.lista_EnProgreso.setObjectName(u"lista_EnProgreso")
        self.lista_EnProgreso.setStyleSheet(u"")
        self.lista_EnProgreso.setWordWrap(True)

        self.gridLayout.addWidget(self.lista_EnProgreso, 2, 1, 1, 1)

        self.lista_Pendientes = QListWidget(self.centralwidget)
        __qlistwidgetitem2 = QListWidgetItem(self.lista_Pendientes)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.lista_Pendientes)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.lista_Pendientes)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.lista_Pendientes.setObjectName(u"lista_Pendientes")
        font1 = QFont()
        font1.setBold(False)
        self.lista_Pendientes.setFont(font1)
        self.lista_Pendientes.setStyleSheet(u"")
        self.lista_Pendientes.setWordWrap(True)

        self.gridLayout.addWidget(self.lista_Pendientes, 2, 0, 1, 1)

        self.lista_Completadas = QListWidget(self.centralwidget)
        __qlistwidgetitem5 = QListWidgetItem(self.lista_Completadas)
        __qlistwidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.lista_Completadas.setObjectName(u"lista_Completadas")
        self.lista_Completadas.setStyleSheet(u"")
        self.lista_Completadas.setWordWrap(True)

        self.gridLayout.addWidget(self.lista_Completadas, 2, 2, 1, 1)

        self.label_Titulo = QLabel(self.centralwidget)
        self.label_Titulo.setObjectName(u"label_Titulo")
        self.label_Titulo.setStyleSheet(u"font-size: 28px;\n"
"background-color: rgb(69, 69, 69);\n"
"color: #e9e9e9;")
        self.label_Titulo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Titulo, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de tareas Kanban", None))
        self.label_Completadas.setText(QCoreApplication.translate("MainWindow", u"Completadas", None))
        self.label_EnProgreso.setText(QCoreApplication.translate("MainWindow", u"En progreso", None))
        self.label_Pendientes.setText(QCoreApplication.translate("MainWindow", u"Pendientes", None))

        __sortingEnabled = self.lista_EnProgreso.isSortingEnabled()
        self.lista_EnProgreso.setSortingEnabled(False)
        ___qlistwidgetitem = self.lista_EnProgreso.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tarea en progreso 1", None));
        ___qlistwidgetitem1 = self.lista_EnProgreso.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tarea en progreso 2", None));
        self.lista_EnProgreso.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.lista_Pendientes.isSortingEnabled()
        self.lista_Pendientes.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.lista_Pendientes.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tarea pendiente 1", None));
        ___qlistwidgetitem3 = self.lista_Pendientes.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tarea pendiente 2", None));
        ___qlistwidgetitem4 = self.lista_Pendientes.item(2)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tarea pendiente 3", None));
        self.lista_Pendientes.setSortingEnabled(__sortingEnabled1)


        __sortingEnabled2 = self.lista_Completadas.isSortingEnabled()
        self.lista_Completadas.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.lista_Completadas.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tarea completada 1", None));
        self.lista_Completadas.setSortingEnabled(__sortingEnabled2)

        self.label_Titulo.setText(QCoreApplication.translate("MainWindow", u"Tablero Kanban", None))
    # retranslateUi

