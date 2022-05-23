import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('pymain08.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.myClick)
        
    def myClick(self):
        first = self.leFirst.text()
        last = self.leLast.text()
        a = int(first)
        b = int(last)
        output = ""
        
        for i in range(a,b+1):
            output += self.drawStar(i)
        
        self.result.setText(output)
    
    
    def drawStar(self, cnt):
        star = ""
        
        for i in range(cnt):
            star += "*"
        
        star += "\n"
        
        return star
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()