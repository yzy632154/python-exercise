def sum(x):
    result = 0
    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result
print(sum(('12345432',3,4,4.2,True)))
