import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

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
        result = ""
        
        if rnd < 0.3:
            com = "가위"
        elif rnd < 0.6:
            com = "바위"
        else:
            com = "보"
            
        if mine == com:
            result = "비김"
        elif (mine == "가위" and com == "바위" or mine == "바위" and com == "보" or mine == "보" and com == "가위"):
            result = "컴퓨터 승리"
        else:
            result = "내가 이김"
        
        self.com.setText(com)
        self.result.setText(result)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()