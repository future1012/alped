#http error
from urllib import request,error


url = 'http://www.nwccw.gov.cn/html/news.html'

try:
    req = request.Request(url)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

except error.HTTPError as e:
    print(e)

except error.URLError as e:
    print(e.reason)