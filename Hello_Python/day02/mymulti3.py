def addminmuldiv(a,b):
    return a+b,a-b,a*b,a/b

a,b,c,d = addminmuldiv(4, 5)
print(a,b,c,d)

# 이거도 가능(작은 배열)
a = addminmuldiv(5, 4)
print(a[0])