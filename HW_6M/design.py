# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(432, 170)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.command = QtWidgets.QLabel(Form)
        self.command.setObjectName("command")
        self.verticalLayout.addWidget(self.command)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.result = QtWidgets.QLabel(Form)
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.output = QtWidgets.QLabel(Form)
        self.output.setText("")
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Math GUI"))
        self.command.setText(_translate("Form", "Enter math command:"))
        self.result.setText(_translate("Form", "Result:"))

