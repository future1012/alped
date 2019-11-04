try:
    num = int(input('plz input a num: '))
    rst = 100/num
    print('计算结果是： {0}'.format(rst))
except Exception as e:
    # print('你他娘的输入的什么玩意？')
    print(e)
    exit()
except ZeroDivisionError as e:
    print(e)
    exit()




try:
    asdfasd
except Exception as e:
    print('wo cuo le ')