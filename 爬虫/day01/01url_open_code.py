import urllib.request

def load_data():
    url = 'http://www.baidu.com/'
    rps = urllib.request.urlopen(url)
    data = rps.read()
    strdata = data.decode('utf-8')
    print(strdata)
    #with open('baidu.html', 'wb', encoding='utf-8') as f:
    with open('baidu.html', 'w',encoding='utf-8') as f:
        f.write(strdata)


load_data()