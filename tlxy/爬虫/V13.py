from urllib import request, parse
from http import cookiejar

#创建cookie实例
cookie = cookiejar.CookieJar()

#生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

#创建http请求管理器
http_handler = request.HTTPHandler()

#创建https请求管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名和密码，用来获取登录cookie凭证
    :return:
    '''
    #此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    #此键值需要从登录的form的两个对应的input中提取name属性
    data = {
        "email": "tengyue1023@163.com",
        "password": "aijing1314"
    }

    #把数据进行编码
    data = parse.urlencode(data)

    #创建一个请求对象

    req = request.Request(url, data= data.encode())

    #使用openner发起请求
    rsp = opener.open(req)


def getHomePage():
    url = "http://www.renren.com/487469521/profile"
    #如果已经执行了login函数，则opener自动已经包含对相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html",'w',encoding='utf8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()