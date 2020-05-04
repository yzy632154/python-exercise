def huiwen(x):
    length = len(x)
    if length == 1:
        print ('是回文')
    elif length == 2 and x[0] == x[1]:
        print('是回文')
    elif length == 3 and x[0] == x[2]:
        print('是回文')
        
    elif (x[0] == x[length-1]) and  (length> 3):
        return huiwen(x[1:length-1])#length-1不包括
    else:
        print('不是回文')
        
