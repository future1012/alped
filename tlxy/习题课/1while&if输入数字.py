#题目：要求用户输入1-100之间的整数并且判断
#输入符合要求的打印‘你好看’，否则打印‘你丑八怪，天黑别把灯打开’

while True:
    num = input('PLZ INPUT A NUM(1-100,q：exit): ')
    if num.isdigit():
        if 1<= int(num) <= 100:
            print('你好看')
        else:
            print('你丑八怪，天黑别把灯打开')
    else:
        if num == 'q':
            break
        else:
            print('你丑八怪，天黑别把灯打开')
