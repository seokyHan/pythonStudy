import sys

from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('myomok.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flagWb = True
        self.flagEnd = False
        self.reset.clicked.connect(self.myReset)
        
        # 이미지 숫자 배열
        self.arr2D= [
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0]
        ]
        
        # 버튼 2차원배열
        self.pb2D = []
             
        for i in range(19):
            # arr2D와 pb2D를 매핑시키기 위함
            line = []
            for j in range(19):
                btn = QPushButton(self)
                btn.setText("")
                btn.setIcon(QIcon("0.png"))
                btn.setGeometry(40*j,i*40,40,40)
                btn.setIconSize(QSize(40,40))
                btn.setToolTip((f"{i},{j}"))
                btn.clicked.connect(self.myClick)
                line.append(btn)
            self.pb2D.append(line)
        
        self.myrender()
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QIcon('0.png')) 
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QIcon('1.png')) 
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QIcon('2.png')) 
                 
    
    def myClick(self):
        
        if self.flagEnd:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        up = self.checkUP(i,j,stone)
        dw = self.checkDown(i,j,stone)
        rt = self.checkRight(i,j,stone)
        lt = self.checkLeft(i,j,stone)
        ur = self.checkUR(i,j,stone)
        ul = self.checkUL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        
        d1 = up + dw + 1
        d2 = rt + lt + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if (d1 == 5) or (d2 == 5) or (d3 == 5) or (d4 == 5):
            if(self.flagWb):
                QMessageBox.question(self, 'Result', 'white Win', QMessageBox.Yes, QMessageBox.NoButton)
            else:
                QMessageBox.question(self, 'Result', 'black Win', QMessageBox.Yes, QMessageBox.NoButton)
            self.flagEnd = True
        
        self.flagWb = not self.flagWb
    
    def checkUR(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                i -= 1
                j += 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def checkUL(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                i += 1
                j -= 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def checkDR(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                i -= 1
                j += 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def checkDL(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                i += 1
                j -= 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def checkRight(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                j -= 1
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def checkLeft(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                j += 1
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def checkUP(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                i -= 1
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
            
    def checkDown(self,i,j,stone):
        cnt = 0      
        try:
            while True:
                i += 1
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
    
    def myReset(self):
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j] = 0
        
        self.myrender()
        self.flagWb = True
        self.flagEnd = False
        
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    