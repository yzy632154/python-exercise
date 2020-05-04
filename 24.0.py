list1 =[]
def decend(n):

    if n//2 == 0:
        list1.append(1)
        return list1
    else:
        list1.append(n%2)
        return decend(n//2)


n = int(input('请输入一个十进制数：'))
list1 = reversed(decend(n))
for i in list1:
    print(i,end='')
