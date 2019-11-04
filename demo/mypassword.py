import sys, pyperclip, getpass
#账号和密码存储在字典中
my_pwd_dict = {
    'email': '12345',
    'weixin': '123',
    'blog': '123456'
}

#进入此程序的主密码
main_pwd = 'abcdef'
passwd = getpass.getpass("请输入主密码： ")

#验证主密码
if passwd.strip() != main_pwd:
    print('login failed!')
    sys.exit()

#需要给出一个参数或者给出一个账号
if len(sys.argv) < 2:
    print('Usage: python 11.py [account] - copy account password')
    print('Usage: python 11.py [-l] - show all account')
    sys.exit()
elif sys.argv[1] == '-l':
    print('All account: ')
    for k in my_pwd_dict.keys():
        print(k)
    sys.exit()

#如果账号在字典中,将对应的密码值写入剪贴板
account = sys.argv[1]
if account in my_pwd_dict:
    pyperclip.copy(my_pwd_dict[account])
    print('Password for {} has copied to clipboard '.format(account))
else:
    print('There is no account named {}'.format(account))
