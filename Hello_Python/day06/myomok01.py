import sys

from PyQt5 import uic
from PyQt5.Qt import QIcon
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('myomok01.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cnt = 0
        self.btn.clicked.connect(self.myClick)
        
    def myClick(self):   
        self.cnt += 1
        self.btn.setIcon(QIcon(f'{self.cnt%3}.png'))
            
        
           
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    