import random
secret = random.randint(1,10)
i = 1
print('我爱yzy')
temp = input('不妨猜猜yzy想的哪个数字：')
guess = int(temp)
if guess == secret:
    print('一次就中了')
else:
    while guess != secret and i < 4:
        if guess > secret:
            print('大了大了')
        else:
            print('小了小了')
        temp = input('错了，请重新输入：')
        guess = int(temp)
        i = i+1
        if guess == secret:
            print("猜中了")
            print('猜中没奖励') 

if i >= 4 and guess != secret:
    print('没缘分啊')
print('游戏结束')
