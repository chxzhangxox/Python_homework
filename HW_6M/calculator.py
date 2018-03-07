# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:09:52 2018

@author: chxzh
"""

import sys, design
from sympy import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import re

class Calculator(QWidget, design.Ui_Form):
    def __init__(self):
        super(Calculator,self).__init__()
        self.setupUi(self)
        self.lineEdit.editingFinished.connect(self.editDone)
    
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
    
        self.output.setText(str(self.input).replace('**', '^'))
        

def main():
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()
    app.exec_()
    
if __name__ == '__main__':
    main()