import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('pymain09.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.myClick)
        self.btn2.clicked.connect(self.myClick)
        self.btn3.clicked.connect(self.myClick)
        self.btn4.clicked.connect(self.myClick)
        self.btn5.clicked.connect(self.myClick)
        self.btn6.clicked.connect(self.myClick)
        self.btn7.clicked.connect(self.myClick)
        self.btn8.clicked.connect(self.myClick)
        self.btn9.clicked.connect(self.myClick)
        self.btn0.clicked.connect(self.myClick)
        self.btn.clicked.connect(self.myCall)
        
    def myCall(self):
        tel = self.le.text()
        QMessageBox.question(self, 'calling', tel, QMessageBox.Yes, QMessageBox.NoButton)
        
    def myClick(self):
        str_old = self.le.text()
        str_new = self.sender().text()
        self.le.setText(str_old + str_new)
            
    
    
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()