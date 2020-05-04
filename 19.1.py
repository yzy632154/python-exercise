def count(*str1):
    num = '0123456789'
    alp = 'abcdefghijklmnopqrstuvwxyz'
    number = 0
    #symbol = r'''.!@#$%^&*'''
    for each in str1:
        count_num,count_alp,count_space,count_other = 0,0,0,0
        number += 1
        for i in each:
            if i in num:
                count_num += 1
            elif i in alp:
                count_alp += 1
            elif i == ' ':
                count_space += 1
            else:
                count_other += 1
        print('第%d个字符串：英文字母%d个，数字%d个，空格%d个，其他字符%d个' % (number,count_alp,count_num,count_space,count_other))

