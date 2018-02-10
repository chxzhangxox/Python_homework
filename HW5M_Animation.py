#Create a window with a red bouncing ball
#The ball still bounces even when the mainwindow is resized during runtime


import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class BouncingBall(QWidget):
    
    #initialize the window, box and the ball
    def __init__(self):
        super(BouncingBall, self).__init__()        
        self.initUI()
        
    def initUI(self): 
        #diameter and position of the ball, position is at the corner
        self.d = 30; self.x = 0; self.y = 0;
        #speed of the ball, x and y coordinate
        self.dx = 1; self.dy = 1;
        #size of the box inside the main window
        self.boxwidth = 590; self.boxheight = 400;
        
        #self.timeron = False #won't start without pressing the button
        #initialization of the case when button is not pushed
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(3)
        
        self.setGeometry(300, 400, 600, 400)
        
        self.setWindowTitle('Animation')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
    
    def resizeEvent(self, e):
        self.boxwidth = self.width()
        self.boxheight = self.height()
    
    def drawRectangles(self, qp):

        qp.setPen(QtGui.QColor(255, 255, 255, 255))
          
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, self.boxwidth, self.boxheight)
        
        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
      
    def animate(self):
        self.x += self.dx
        self.y += self.dy
        self.checkCollision()
        self.update()
        
    def checkCollision(self):
        #position of the ball is recognized at the corner
        #reverse the moving direction
        if (self.x <= 0) or ((self.x + self.d)>= self.boxwidth):
            self.dx = -self.dx 
        if (self.y <= 0) or ((self.y + self.d)>= self.boxheight):
            self.dy = -self.dy
              
def main():
    
    app = QApplication(sys.argv)
    ex = BouncingBall()
    app.exec_()


if __name__ == '__main__':
    main()
