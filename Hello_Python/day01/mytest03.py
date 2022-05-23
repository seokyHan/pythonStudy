aa= input("첫 수를 넣으세요");
bb = input("끝를 넣으세요");
cc = input("배수를 넣으세요");

a = int(aa)
b = int(bb)
c = int(cc)

bsum = 0
for i in range(a,b+1):
    if(i % c == 0):
        bsum += i
print(bsum)    