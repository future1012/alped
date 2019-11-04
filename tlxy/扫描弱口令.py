#!/usr/bin/python3
#coding: utf-8
import random
import time
import threading
import os
import sys
from sys import argv


def generate_random_str(randomlength=16):
    random_str = ''
    #base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    base_str = '123456'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def wpscan(leng):
    count = 0
    pwd = '123456'
    while True:
        str = generate_random_str(leng)
        if str == pwd and second == 'twns':
            print('[{0}] Correct!'.format(str))
            print()
            leng = len(pwd) + 15
            print('*' * leng)
            print('密码是: [{0}]'.format(str))
            print('*' * leng)
            print('你可以尝试使用浏览器访问:\nhttp://{0}\n用户名: {1} \n密码: {2}'.format(first, second, pwd))
            exit()
        else:
            print('[{0}] ERROR!'.format(str))
            # time.sleep(1)
        count += 1
        if count == 100:
            break

if __name__ == '__main__':
    try:
        script, first, second = argv
        print('###')
        print('###')
        leng = len(first) + 15
        print('*' * leng)
        print('扫描路径或者域名: [{0}]'.format(first))
        print('用户名: [{0}]'.format(second))
        print('*' * leng)
        print()
        input('按回车键继续: ')
        count = 0
        while True:
            for i in range(6, 7):
                wpscan(i)
                #time.sleep(0.5)
                #count += 1
                #if count == 10:
                #    input('The number of probes: [{0}], Enter key continues: '.format(count))
               	#    count = 0
    except KeyboardInterrupt as e:
        print('\n\nprogram exit!')
    except Exception as e:
        print('ERROOOOOOOOOOOOR!!!')
        print('USAGE: {0} {1} {2}'.format(os.path.split(__file__)[-1], '<你的域名>', '<用户名>'))
