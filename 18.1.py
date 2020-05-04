flag1 = 1
def shuixian(x):
    a = x//100
    b = (x - a*100)//10
    c = x - a*100 -b*10
    if x == a**3 + b**3 + c**3:
        flag = 1
    else:
        flag = 0
    return flag

for i in range(100,1000):
    if flag1 == shuixian(i):
        print(i)
