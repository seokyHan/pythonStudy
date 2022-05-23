import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

from day01.if01 import a


form_class = uic.loadUiType('pymain04.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.myClick)
        self.mine.returnPressed.connect(self.myClick)
        
    def myClick(self):
        rnd = random.random()
        mine = self.mine.text()
        com = ""
        result =""
        
        if(rnd > 0.5):
            com = "홀"
        else:
            com = "짝"
        
        if(com == mine):
            result = "이김"
        else:
            result ="짐"
        
        self.com.setText(com)
        self.result.setText(result)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()