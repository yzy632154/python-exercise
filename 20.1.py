
def daxie3(str2):
    length = len(str2)
    list1=[]
    if (str2[0].isupper()) and (str2[1].isupper()) and (str2[2].isupper()) and (str2[3].islower()):
        list1.append(0)
    for i in range(1,length-3):
        if str2[i] == '\n':
            continue
        if (str2[i].isupper()) and (str2[i+1].isupper()) and (str2[i+2].isupper()) and (str2[i-1].islower()) and (str2[i+3].islower()):
            list1.append(i)
    return list1
            
#def findsecret(str1):
    #length = len(str1)
    #for i in range(3:length-3):
        #if (str1[i] in alpxiao) and (str1[i-3] in alpha) and (str1[i-2] in alpha) and (str1[i-1] in alpha) and (str1[i+1] in alpha) and (str1[i+2] in alpha) and (str1[i+3] in alpha) :

str1 = input('输入字符串：')
list1=[]
list2 = daxie3(str1)
length = len(list2)
for i in range(1,length):
    if str1[i] == '\n':
            continue
    if list2[i] == list2[i-1] + 4:
       list1.append(list2[i]-1)

for each in list1:
    print(str1[each],end='')
        
