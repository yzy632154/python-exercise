def huiwen(x):
    list1 = list(x)
    list2 = list1.copy()
    list1.reverse()
    if list2 == list1:
        flag = 1
    else:
        flag = 0
    return flag

str1 = input('请输入一句话：')
if huiwen(str1) == 1:
    print('是回文联')
else:
    print('不是')

    
