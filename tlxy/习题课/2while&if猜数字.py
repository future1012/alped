#题目：猜数字再1-100内，给定猜的次数，超过此数提示：没机会了，程序退出。目标数字随机。并提示猜的数字是正好等于或者大小。

import  random

secret = random.randint(1,100)
times = 10

while times:
    num = input('input a num: ')
    if num.isdigit():
        num = int(num)
        if num == secret:
            print('猜对了')
            times-=1
            break
        elif num < secret:
            print('猜小了')
            times-=1
        else:
            print('猜大了')
            times-=1
    else:
        print('应该输入一个数字')
        times-=1
else:
    print('没机会了')
