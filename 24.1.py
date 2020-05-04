list1 = []
def get_digits(n):
    if n // 10 == 0:
        list1.insert(0,n)
        return list1
    else:
        list1.insert(0,n%10)
        return get_digits(n//10)
