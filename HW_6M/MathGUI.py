# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from sympy import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import re

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)
        self.lineEdit.editingFinished.connect(self.editDone)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Math GUI"))
        self.command.setText(_translate("Form", "Enter math command:"))
        self.result.setText(_translate("Form", "Result:"))
    
    def editDone(self):
        regex_diff = re.compile(r'd[ie][fr][fi]\w*\((.+),\s?(\w*)\)')
        regex_integ = re.compile(r'int\w*\((.+),\s?(\w*)\)')
        regex_sol_equal = re.compile(r'sol\w*\((.*) = (.*),\s?(\w+)\)')
        regex_sol_reg = re.compile(r'sol\w*\((.+),\s?(\w*)\)')
        regex_eq = re.compile(r'(.*([xyzabc]).*) = (.*)')
        regex_diff.sub('^', '**')
        regex_integ.sub('^', '**')
        regex_sol_reg.sub('^', '**')
        regex_sol_equal.sub('^','**')
        regex_eq.sub('^', '**')
        diff = re.search(regex_diff, self.lineEdit.text())
        integ = re.search(regex_integ, self.lineEdit.text())
        sol_equal = re.search(regex_sol_equal, self.lineEdit.text())
        sol_reg = re.search(regex_sol_reg, self.lineEdit.text())
        eq = re.search(regex_eq, self.lineEdit.text())
        
        x, y, z = symbols('x y z')
        
        if self.lineEdit.text():
            if diff:
                self.input = sympify('diff(' + str(diff.group(1)) + ',' + str(diff.group(2)) + ')')
            elif integ:
                self.input = sympify('integrate(' + str(integ.group(1)) + ',' + str(integ.group(2)) + ')')
            elif sol_equal:
                self.input = sympify('solve(' + str(sol_equal.group(1)) + '-' + str(sol_equal.group(2)) + ',' + str(sol_equal.group(3)) + ')')
            elif sol_reg:
                self.input = sympify('solve(' + str(sol_reg.group(1)) + ',' + str(sol_reg.group(2)) + ')')
            elif eq:
                self.input = sympify('solve(' + str(eq.group(1)) + '-' + str(eq.group(3)) + ',' + str(eq.group(2)) + ')')
            else:
                self.input = sympify(self.lineEdit.text())
        else:
            self.input = ''
    
        self.output.setText(str(self.input).replace('**', '^'))
        
        
def main():
    app = QApplication(sys.argv)
    w = Ui_Form()
    w.show()
    app.exec_()
    
if __name__ == '__main__':
    main()        
        
        
        
        
        
        
    
