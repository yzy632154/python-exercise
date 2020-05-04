print('|---欢迎进入---|')
print('|---1.查询联系人---|')
print('|---2.插入联系人---|')
print('|---3.删除联系人---|')
print('|---4.退出通讯录---|')
dict2 = {}
def enquiry():
    x = input('请输入联系人姓名：')
    print(x,':',dict2[x])

def insert():
    x = input('请输入联系人姓名：')
    if x not in dict2:
        y=input('请输入电话号码：')
        dict2[x]=y
    else:
        print('你输入的姓名以存在-->>',x,':',dict2[x])
        z=input('是否修改用户资料（YES/NO）：')
        if z == 'YES':
            m = input('请输入电话号码：')
            dict2[x]=m

            
def delete():
    x = input('请输入联系人姓名：')
    dict2.pop(x)


while 1:
    a = int(input('请输入相关指令：'))
    if a == 1:
        enquiry()
    elif a == 2:
        insert()
    elif a == 3:
        delete()
    elif a == 4:
        print('|---感谢使用通讯录---|')
        break
    else:
        print('输入指令有误')
        
