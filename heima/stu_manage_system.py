import sys
#展示系统界面
def info_print():
    print('''
请选择----------:
1.添加用户
2.删除用户
3.查询用户
4.修改用户
5.打印全部用户
6.推出系统
---------------
''')
info = []
# 添加用户功能
def add_info():
    global info
    # 等待用户输入
    new_id = input('ID: ')
    new_name = input('名称：')
    new_age = input('年龄：')
    new_tel = input('电话：')
    user_dict = {}
    # 判断用户是否存在
    # 存在，提示用户已存在，推出add_info
    for i in info:
        if new_name == i['name']:
            #print(info)
            print('用户已存在!')
            return
    # 不存在，添加用户
    user_dict['id'] = new_id
    user_dict['name'] = new_name
    user_dict['age'] = new_age
    user_dict['tel'] = new_tel
    info.append(user_dict)
    #print(info)
    print('添加成功！')

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
        #print(info)
        print('删除成功！')
    print('用户不存在!')

def que_info():
    que_user = input('请输入要查询的用户名: ')
    for i in info:
        if que_user == i['name']:
            print(f"ID: {i['id']}, 姓名：{i['name']}, 年龄：{i['age']}, 电话：{i['tel']}")
            break
    else:
        print('您要查询的用户不存在！')

def mod_info():
    global info
    mod_user = input('请输入要修改的用户名: ')
    for i in info:
        if mod_user == i['name']:
            mod_cont = int(input('''请输入需要修改内容的序号: (1.名称, 2.年龄, 3.电话) '''))
            if mod_cont == 1:
                i['name'] = input('请输入新的名称：')
            elif mod_cont == 2:
                i['age'] = input('请输入新的年龄：')
            elif mod_cont == 3:
                i['tel'] = input('请输入新的电话：')
            print('修改成功：')
            print(f"ID: {i['id']}, 姓名：{i['name']}, 年龄：{i['age']}, 电话：{i['tel']}")
            break
    else:
        print('需要修改的用户不存在!')

def print_all():
    global info
    print(f"{'ID':<10s}{'姓名':<9s}{'年龄':<5s}{'电话':<11s}")
    #print('{:^2s},{:^10s},{:^3s},{:^11s}'.format('ID','姓名','年龄','电话'))
    for i in info:
        print(f"{i['id']:<10s}{i['name']:<10s}{i['age']:<6s}{i['tel']:<11s}")
        #print("{}\t{}\t{}\t{}".format(i['id'],i['name'],i['age'],i['tel']))
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
            print('查询用户>>>')
            que_info()
        elif userInputnum == 4:
            print('修改用户>>>')
            mod_info()
        elif userInputnum == 5:
            print('打印全部用户>>>')
            print_all()
        elif userInputnum == 6:
            print('已退出系统。')
            #sys.exit()
            break
        else:
            print('输入有误，请重新输入。')