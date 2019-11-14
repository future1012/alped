import urllib.request
import urllib.parse
import  string

def get_method_parames():
    url = 'http://www.baidu.com/s?wd='
    #https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
    name = 'women+men'
    final_url = url+name
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    rps = urllib.request.urlopen(encode_new_url)
    data = rps.read()
    strdata = data.decode('utf-8')
    print(strdata)
    with open('美女.html','w',encoding='utf-8') as f:
        f.write(strdata)

get_method_parames()