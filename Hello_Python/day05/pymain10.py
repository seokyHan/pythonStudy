import sys
import threading
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('pymain10.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.myClick)
        
    def myClick(self):
        threading.Thread(target=self.myCount).start()
            
    def myCount(self):
        for i in range(1,10+1):
            self.lbl.setText(str(i))
            time.sleep(1)
        
      
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    