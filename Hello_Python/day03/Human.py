class Human:
    def __init__(self,age):
        print("생성자", age)
        self.skill = 0
    def exp(self, mama):
        self.skill += mama
    def __del__(self):
        print("소멸자",self.skill)
        
human = Human(5)
print(human.skill)
human.exp(5)
print(human.skill)