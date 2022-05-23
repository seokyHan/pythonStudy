import sys

from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('myomok02.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
             
        for i in range(18):
            for j in range(18):
                btn = QPushButton(self)
                btn.setText("")
                btn.setIcon(QIcon("0.png"))
                btn.setGeometry(40*i,j*40,40,40)
                btn.setIconSize(QSize(40,40))
                btn.clicked.connect(self.myClick)
    
    def myClick(self):
        white = self.sender()
        white.setIcon(QIcon('1.png'))  
                
            
        
        
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    