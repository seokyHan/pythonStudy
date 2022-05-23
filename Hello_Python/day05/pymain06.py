import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('pymain06.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.myClick)
        self.dan.returnPressed.connect(self.myClick)
        
    def myClick(self):
        a = self.dan.text()
        dan = int(a)
        output = ""
        
        for i in range(1,10):
            output += str(dan) + " X " + str(i) + " = " + str(dan * i) + "\n" 
            
        self.result.setText(output)
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()