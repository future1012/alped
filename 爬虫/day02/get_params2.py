import urllib.request
import urllib.parse
import string


def get_parames():
    url = 'http://www.baidu.com/s?'
    parames = {
        'wd': '中文 英文',
        'key': 'zhang',
        'values': 'san'
    }
    end_url = urllib.parse.urlencode(parames, string.printable)
    #print(end_url)
    final_url = url + end_url
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    print(end_url)
    rps = urllib.request.urlopen(end_url)

    resdata = rps.read().decode('utf-8')
    print(resdata)

    with open('中文.html', 'w', encoding='utf-8') as f:
        f.write(resdata)



get_parames()