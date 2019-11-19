import sys
#展示系统界面
def info_print():
    print('''
请选择----------:
1.添加用户
2.删除用户
3.打印全部用户
4.推出系统
---------------
''')

#等待用户输入

while True:
    #执行相应操作
    info_print()
    userInputnum = int(input('请选择：'))
    if userInputnum == 1:
        print('添加用户')
    elif userInputnum == 2:
        print('删除用户')
    elif userInputnum == 3:
        print('打印全部用户')
    elif userInputnum == 4:
        print('退出系统')
        sys.exit()
    else:
        print('输入有误，请重新输入。')