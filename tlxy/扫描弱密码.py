#!/usr/bin/python3
import random
import time
import threading
def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    # base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    base_str = '1230twns!@*()_+'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def wpscan(leng):
    count = 0
    while True:
        str = generate_random_str(leng)
        if str == 'twns':
            print('Password is: {0}'.format(str))
            exit()
        else:
            print('{0} is wrong!'.format(str))
            # time.sleep(1)
        count += 1
        if count == 100:
            break

if __name__ == '__main__':
    while True:
        for i in range(1, 7):
            wpscan(i)

# try:
#     pass
# except Exception