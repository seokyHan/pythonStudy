import random
# me = input("홀/짝을 고르시오")
# print(f"나 : {me}")
# rnd = random.random()
# if(rnd > 0.5):
#     com = "홀"
# else:
#     com = "짝"
# print(f"컴 : {com}")
#
#
# if(me == com):
#     print("결과 : 비김")
# elif(me == "홀" and com == "짝"):
#     print("결과 : 이김")
# else:
#     print("결과 : 짐")


com = ""
mine = ""
result = ""

mine = input("홀/짝을 고르시오")
rnd = random.random()
if(rnd > 0.5):
    com = "홀"
else:
    com = "짝"
    
if(mine == com):
    result = "결과 : 비김"
elif(mine == "홀" and com == "짝"):
    result = "결과 : 이김"
else:
    result = "결과 : 짐"

print("나",mine)
print("컴퓨터", com)
print("결과", result)
