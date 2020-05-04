
# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   in. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

number = '0123456789'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''

secret = input ('请输入密码：')

length = len(secret)

while secret.isspace() or length == 0:
    secret = input('密码全为空格（为空），请重新输入：')
    length = len(secret)

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

for each in secret:
    if each in number:
        flag_num = 1
        break

for each in secret:
    if each in alpha:
        flag_al = 1
        break

for each in secret:
    if each in symbol:
        flag_sym = 1
        break

while 1:
    print ('密码等级为：',end='')
    if (flag_len == 1) or (flag_sym != 1):
        print('低')
    elif (flag_len == 3) and (flag_num*flag_al*flag_sym == 1) and (secret[0] in alpha):
        print('高')
        print('请保持！')
        break
        
    else:
        print('中')
    break
    
