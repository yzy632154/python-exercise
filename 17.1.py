def gcd(x,y):
    if x < y:
        temp1 = x
        temp2 = y
        y = temp1
        x = temp2
    else:
        while x % y != 0:
            temp1 = x
            temp2 = y
            x = temp2
            y = temp1%y
        return y
