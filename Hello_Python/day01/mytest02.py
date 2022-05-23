aa = input("첫 수를 넣으세요")
bb = input("두번째 수를 넣으세요")
a = int(aa)
b = int(bb)

msum = 0;

for i in range(a,b+1):
    msum += i
    
    
# print(f"{a}에서 {b}까지 합은 {msum} 입니다.")
print("{}에서 {}까지 합은 {} 입니다.".format(a,b,msum))