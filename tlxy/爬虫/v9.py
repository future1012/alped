#useragent 身份隐藏

from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        #两种方法添加header
        #1.构造header
        #2.使用add_header
        headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        req = request.Request(url, headers=headers)
        #req.add_header(key='User-Agent',val='Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
        req.add_header('User-Agent','Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')

        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e.reason)
    except error.URLError as e:
        print(e.reason)
    except Exception as e:
        print(e)

print('DONEEEEEEEEEEEEE')