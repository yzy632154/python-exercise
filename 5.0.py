import random

times = 3
secret = random.randint(1,10)

print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")

while (guess != secret) and (times > 0):
    temp = input()
    
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
            if times > 1:
                print("再试一次吧：", end='')
            else:
                print("机会用光咯T_T")
    else:
        print("抱歉，您的输入有误，请输入一个整数：", end='')

    times = times - 1 # 用户每输入一次，可用机会就-1

print("游戏结束，不玩啦^_^")

