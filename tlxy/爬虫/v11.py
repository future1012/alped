
from urllib import request
import chardet


if __name__ == '__main__':

    url = "http://www.baidu.com/"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    cs = chardet.detect(html)
    print('####################')
    print(html)
    print('####################')
    html = html.decode(cs.get("encoding", "utf-8"))
    # html = html.decode()
    with open('rsp.html','w',encoding='utf8') as f:
        f.write(html)
