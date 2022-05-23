# 상속
class Animal:
    def __init__(self):
        self.mylife = 100
        self.myage = 0
        
    def getAge(self):
        self.mylife -= 1
        self.myage += 1

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill = 1
        
    def exp(self,mama):
        self.skill += mama
    
if __name__ == '__main__':
    hum = Human()
    print(hum.mylife)
    print(hum.myage)
    print(hum.skill)
    hum.getAge()
    hum.exp(100)
    print(hum.mylife)
    print(hum.myage)
    print(hum.skill)