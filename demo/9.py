while True:
    name = input('请输入你的名字：')
    if name.strip().isalpha():
        break
    else:
        print('输入错误，请重新输入。')
