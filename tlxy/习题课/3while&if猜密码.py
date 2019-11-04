#打印出0-100所有的奇数
# for i in range(0,100):
#     if i%2 == 1:
#         print(i)



''' 有一个长阶梯，每步上2阶，最后剩1阶
                    3        2
                    5        4
                    6        5
                    7        0
'''
# i = 0
# while i < 10000:
#     if i%3==2 and i%5==4 and i%6==5 and i%7==0:
#         print(i)
#         i+=1
#     else:
#         i+=1


# for _ in range(0,10,2):
#     print('tuling')

times = 3

while times:
    secret = input('请输入密码：')
    if '*' in secret:
        print('密码不能有星号,你还有{0}次机会'.format(times))
    elif secret != 'aaa':
        times-=1
        print('密码错误,你还有{0}次机会'.format(times))
    else:
        print('密码正确')
        break

# while times:
#     secret = input('请输入密码：')
#     if '*' in secret:
#         print('密码不能有星号,你还有{0}次机会'.format(times))
#     elif  secret == 'aaa':
#         print('密码正确')
#         break
#     else:
#         times-=1
#         print('密码错误,你还有{0}次机会'.format(times))




