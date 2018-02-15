import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog

class Example(QWidget):
    
    #initialize the window, box and the rectangle
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self): 
        self.d = 30; self.x = 0; self.y = 0;
        #initialize the position of the cursor
        self.pos_x = 0
        self.pos_y = 0
        #detect if the mouse is released
        self.release = False
        #set the box size
        self.boxwidth = 600; self.boxheight = 400;
        #initialize the color of the rectangle
        self.color = QtGui.QColor(200,0,0,255)
        
        self.setGeometry(300, 300, 600, 400)
        
        self.setWindowTitle('Animation')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        if self.pos_x != 0 and self.pos_y != 0:
            self.drawCircle(qp)
        qp.end()
        
    def drawRectangles(self, qp):

        qp.setPen(QtGui.QColor(0, 0, 0, 255))
          
        qp.setBrush(QtGui.QColor(255, 255, 255, 255))
        qp.drawRect(0, 0, self.boxwidth, self.boxheight)
        
        qp.setPen(self.color)
        qp.setBrush(self.color)
        qp.drawRect(self.x, self.y, self.d, self.d)
    
    def drawCircle(self, qp):
        if self.release == False:
            qp.setPen(QtGui.QColor(0, 0, 0, 255))
            qp.setBrush(QtGui.QColor(0, 0, 0, 0))
        else:
            qp.setPen(QtGui.QColor(0, 0, 0, 0))
            qp.setBrush(QtGui.QColor(0, 0, 0, 0))
        qp.drawEllipse(self.pos_x - 10, self.pos_y - 10, 20, 20)
    
    def mousePressEvent(self,e):
        self.release = False
        self.pos_x = e.x()
        self.pos_y = e.y()
        if e.x() > self.x + self.d or e.x() < self.x:
            self.inside = False
        elif e.y() < self.y or e.y() > self.y + self.d:
            self.inside = False
        else:
            self.inside = True
            self.init_x = e.x() - self.x
            self.init_y = e.y() - self.y
        self.update()
    
    def mouseMoveEvent(self,e): 
        self.pos_x = e.x()
        self.pos_y = e.y()
        if self.inside == True:
            self.x = e.x() - self.init_x
            self.y = e.y() - self.init_y
        
        self.update()

    def mouseReleaseEvent(self,e):
        self.release = True
        self.update()
    
    def mouseDoubleClickEvent(self,e):
        if self.inside == True:
            color_pick = QColorDialog(self)
            self.color = color_pick.getColor()
            self.update()
        

def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()


if __name__ == '__main__':
    main()