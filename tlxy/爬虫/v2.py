from urllib import request
import chardet

if __name__ == '__main__':
    #url = 'https://jobs.zhaopin.com/CC252173610J00092402610.htm'
    url = 'http://exmail.qq.com/'

    #rsp 是bytes类型
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp.geturl())
    print(rsp.info())
    print(rsp.getcode())
    html = rsp.read()

    #chardet 检测编码
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    html = html.decode(cs.get("encoding", "utf-8"))
    # print(html)