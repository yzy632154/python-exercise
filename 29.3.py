file_name = input('请输入要打开的文件名：')
hang = input ('请输入需要显示的行数：')
f = open(file_name)
list1 = list(f)
length = len(list1)

def xianshi(a,b):
    for i in range(a,b):
        print(list1[i])

(start,end) = hang.split(':',1)
if start == '':
    print('文件'+file_name+'从开始到第'+end+'行的内容如下：')
    xianshi(0,int(end))
   
elif end == '':
    print('文件'+file_name+'从第'+start+'行到末尾的内容如下：')
    xianshi(int(start)-1,length)
    
else:
    print('文件'+file_name+'从'+start+'行到第'+end+'行的内容如下：')
    xianshi(int(start)-1,int(end))
    
    

