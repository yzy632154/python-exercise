file_name = input('请输入文件名：')
file_saved = open(file_name+'.txt','w')
print('请输入内容：')
context = []

while 1:
    a = input()
    if a != ':w':
        context.append(a+'\n')
    else:
        break


file_saved.writelines(context)

file_saved.close()
