import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('pymain02.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.myClick)
    def myClick(self):
        a = self.lbl.text()
        cnt = int(a)
        cnt -= 1
        self.lbl.setText(str(cnt))
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()