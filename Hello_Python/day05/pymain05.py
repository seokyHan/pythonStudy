import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('pymain05.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.myClick)
        
    def myClick(self):
        arr = [
        1,2,3,4,5, 6,7,8,9,10,
        11,12,14,15, 16,17,18,19,21,
        21,22,23,24,25, 26,27,28,29,30,
        31,32,33,34,35, 36,37,38,39,40,
        41,42,43,44,45
        ]
        
        lotto = []
        
        while(len(lotto) < 6):
            rnd = int(random.random()*45)
            if(arr[rnd] > 0):
                lotto.append(arr[rnd])
                arr[rnd] = -1
            else:
                continue
        
        print(lotto)
        self.mysort(lotto)
        print(lotto)
        
        self.num1.setText(str(lotto[0]))
        self.num2.setText(str(lotto[1]))
        self.num3.setText(str(lotto[2]))
        self.num4.setText(str(lotto[3]))
        self.num5.setText(str(lotto[4]))
        self.num6.setText(str(lotto[5]))
        
    def mysort(self,arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            
            
               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()