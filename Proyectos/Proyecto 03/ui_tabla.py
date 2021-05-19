# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablaDBjkBE.ui'
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
        MainWindow.resize(388, 429)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_nombre = QLabel(self.groupBox)
        self.label_nombre.setObjectName(u"label_nombre")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_nombre)

        self.line_nombre = QLineEdit(self.groupBox)
        self.line_nombre.setObjectName(u"line_nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_nombre)

        self.label_empleo = QLabel(self.groupBox)
        self.label_empleo.setObjectName(u"label_empleo")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_empleo)

        self.line_empleo = QLineEdit(self.groupBox)
        self.line_empleo.setObjectName(u"line_empleo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_empleo)

        self.label_email = QLabel(self.groupBox)
        self.label_email.setObjectName(u"label_email")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_email)

        self.line_email = QLineEdit(self.groupBox)
        self.line_email.setObjectName(u"line_email")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_email)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boton_borrar = QPushButton(self.groupBox)
        self.boton_borrar.setObjectName(u"boton_borrar")

        self.horizontalLayout.addWidget(self.boton_borrar)

        self.boton_nuevo = QPushButton(self.groupBox)
        self.boton_nuevo.setObjectName(u"boton_nuevo")

        self.horizontalLayout.addWidget(self.boton_nuevo)

        self.boton_modificar = QPushButton(self.groupBox)
        self.boton_modificar.setObjectName(u"boton_modificar")

        self.horizontalLayout.addWidget(self.boton_modificar)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.tabla = QTableView(self.centralwidget)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tabla)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos del contacto", None))
        self.label_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_empleo.setText(QCoreApplication.translate("MainWindow", u"Empleo", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.boton_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.boton_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.boton_modificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
    # retranslateUi

