file_name = input('请输入文件名：')
word = input('请输入想要替换的字符：')
replace = input('请输入想要替换的字符：')
f = open(file_name)
list1 = list(f)
f.close
length = len(list1)
trantab = str.maketrans(word,replace)
list2=[]
count = 0

for i in range(length):
    if word in list1[i]:
        count += 1
        newstr = list1[i].translate(trantab)
        list2.append(newstr)

print('文件'+file_name+'中共有'+str(count)+'个'+word)
print('你确定要把所有的'+word+'换成'+replace+'吗？')

if input('【YES/NO】:') == 'yes':
    g=open(file_name,'w')
    g.writelines(list2)
    g.close()
