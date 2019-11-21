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
info = []
# 添加用户功能
def add_info():
    global info
    # 等待用户输入
    new_id = input('ID: ')
    new_name = input('名称：')
    new_tel = input('电话：')
    user_dict = {}
    # 判断用户是否存在
    # 存在，提示用户已存在，推出add_info
    for i in info:
        if new_name == i['name']:
            print(info)
            print('用户已存在!')
            return
    # 不存在，添加用户
    user_dict['id'] = new_id
    user_dict['name'] = new_name
    user_dict['tel'] = new_tel
    info.append(user_dict)
    print(info)

def del_info():
    global info
    # 等待用户输入
    del_user = input('请输入要删除的用户名称：')
    for i in info:
        if del_user == i['name']:
            info.remove(i)
        print(info)
        break
    else:
        print(info)
    print('用户不存在!')

if __name__ == '__main__':
    while True:
        #执行相应操作
        info_print()
        userInputnum = int(input('请选择：'))
        if userInputnum == 1:
            print('添加用户>>>')
            add_info()
        elif userInputnum == 2:
            print('删除用户>>>')
            del_info()
        elif userInputnum == 3:
            print('打印全部用户')
        elif userInputnum == 4:
            print('退出系统')
            sys.exit()
        else:
            print('输入有误，请重新输入。')