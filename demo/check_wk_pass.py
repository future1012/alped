import re,sys
upperRegex = re.compile(r'[A-Z]+')
lowerRegex = re.compile(r'[a-z]+')
numRegex = re.compile(r'\d+')
lenRegex = re.compile(r'[\w\d]{8,}')

def stringPasscheck():
    while True:
        print('请输入一个密码，密码的要求长度大于等于8位，必须包含大小写字母和最少一个数字。')
        inputPass = input('请输入密码（q:退出）：')
        if inputPass != 'q':
            if upperRegex.search(inputPass) and lowerRegex.search(inputPass) and numRegex.search(inputPass) and lenRegex.search(inputPass):
                print('密码符合强度要求。')
                sys.exit(0)
            else:
                print('密码符合不强度要求,请重试。')
        else:
            break

if __name__ == '__main__':
    stringPasscheck()
