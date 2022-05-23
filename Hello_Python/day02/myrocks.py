import random

me = input("가위 바위 보 입력 >> ")
arr = ["가위","바위","보"]
com = arr[int(random.random()*3)]
result =""

if me == com:
    result = "비김"
elif (me == "가위" and com == "바위") or (me == "바위"  and com == "보") or (me == "보"  and com == "가위"):
    result = "컴퓨터 이김"
else:
    result = "내가 이김"

print("나 : ", me)
print("컴퓨터 : ", com)
print("결과 : ", result)
    


