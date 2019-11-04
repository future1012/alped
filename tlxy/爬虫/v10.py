#使用代理访问baidu
#可用
#代理地址 from www.goubanjia.com; www.xicidaili.com

from urllib import request,error

if __name__ == '__main__':
    url = "http://blog.tengyue.info"

    #开始使用代理
    #1,设置代理地址
    proxy = {'http': '113.200.56.13:8010'}
    #2,创建proxyhandler
    proxy_handler = request.ProxyHandler(proxy)
    #3，创建opener
    opener = request.build_opener(proxy_handler)
    #4，安装opener
    request.install_opener(opener)

    #访问url,则会使用代理服务器
    try:
        UA = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        req = request.Request(url)
        req.add_header('User-Agent', UA)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)



