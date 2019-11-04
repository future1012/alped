from urllib import request, parse
'''
使用urllib.request 请求一个网页内容，并把内容打印出来
'''
#
# if __name__ == '__main__':
#     url = 'http://www.baidu.com/s?'
#     wd = input('plz input your keyword: ')
#     qs = {'wd': wd}
#     qs = parse.urlencode(qs)
#     print(qs)
#     fullurl = url + qs
#     print(fullurl)
#     rsp = request.urlopen(fullurl)
#     html = rsp.read()
#     html = html.decode()
#     print(html)


if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input("Input your keyword:")
    qs = {"wd": wd}
    qs = parse.urlencode(qs)
    print(qs)
    #fullurl = url + qs
    # fullurl = url + 'wd=aaa'
    fullurl = 'http://www.baidu.com/s?wd=wps'
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)