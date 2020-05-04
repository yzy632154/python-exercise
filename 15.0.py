while 1:
    temp = input('请输入一个整数：')
    if temp == 'Q':
        break
    number = int(temp)
    num16 = '%#x' % number
    num8 = '%#o' % number
    num2 = bin(number)
    print(num16,num8,num2)

