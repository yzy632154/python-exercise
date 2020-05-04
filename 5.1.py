temp = input ('请输入一个年份：')
while not temp.isdigit():
    print ('输入有误',end ='')
    temp = input ('请重新输入：')
year = int(temp)
chu4 = int(year/4)
chu100 = int(year/100)
chu400 = int(year/400)
if ((chu4 == year/4) and (chu100 != year/100) or (chu400 == year/400)):
    print (temp+'年是闰年')
else:
    print(temp+'年不是闰年')
