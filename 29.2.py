file_name = input('请输入要打开的文件名：')
num = int (input ('请输入需要显示的行数：'))
print('文件'+file_name+'的前'+str(num)+'行的内容如下：')
f = open(file_name)
list1 = list(f)
for i in range(num):
    print(list1[i])
