file_name1 = input('请输入第一个文件名：')
file_name2 = input('请输入第二个文件名：')

f1 = open(file_name1)
f2 = open(file_name2)

count = 0
list1=list(f1)
list2=list(f2)
length = len(list1)
for i in range(length):
    if list1[i] != list2[i]:
        count += 1
        print('第%d行不一样' % (i+1))
    else:
        continue
print('两个文件共有【%d】处不同'% count)

f1.close()
f2.close()
