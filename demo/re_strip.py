#导入re模块
import re


def my_strip(f,s=r'\s'):
    '''
    定义功能函数
    :param f: 原始字符串
    :param s: 指定替换掉的字符
    :return: 返回正则匹配替换结果
    '''
    # print(s)
    #利用用管道符，匹配已制定字符开头或结尾的字符。
    return re.sub(r'^{}+|{}+$'.format(s, s), '', f)


if __name__ == '__main__':
    print(my_strip('ccc66aaa666666c', 'c'))
    print(my_strip('  66aaaa66666   '))