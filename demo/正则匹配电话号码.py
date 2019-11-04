def isPhoneNumber(text):
    '''
    判断给出一段文本是否符合电话号码的模式
    :param text:
    :return:
    '''
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

mesg = 'askdjfkasdfk323-343-4567ksdf987-656-4524sakdfj232-342-235335-2s'

if __name__ == '__main__':
    for i in range(len(mesg)):
        phonenumber = mesg[i:i+12]
        # print(phonenumber)
        if isPhoneNumber(phonenumber):
            print('找到号码了：{}'.format(phonenumber))
