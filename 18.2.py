str1 = input('请输入目标字符串:')
def findstr(a,b):
    j = 0
    count = 0
    for i in str1:
        if a == i and b == str1[j+1]:
            count += 1
        j += 1
    return count
str2 = input('请输入两个字符：')
num = findstr(str2[0],str2[1])
print('字符串出现%d次'% num)
