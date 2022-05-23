class Animal:
    def __init__(self, molla):
        print("생성자",molla)
        self.mylife = 100
        self.myage = molla
        
    def getAge(self):
        self.mylife -= 1
        self.myage += 1
        
    def __del__(self):
        print("소멸자", self.myage)

ani = Animal(5)

if True:
    ani2 = Animal(10)

# ani = Animal()
# print("ani", ani.mylife)
# ani.getAge()
# print("ani", ani.mylife)
    