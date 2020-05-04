def bin1(x):
    list1=[]
    while x // 2 != 0:
        list1.append(x%2)
        x = x//2
    list1.append(x%2)
    list1.reverse()
    for i in list1:
        print(i,end='')
