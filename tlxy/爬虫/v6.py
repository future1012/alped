from urllib import request,parse
import json

'''
大致流程：
1、利用data构造内容，然后urlopen打开
2、返回json格式数据
3、结果就应是girl的翻译
'''
baseurl = 'https://fanyi.baidu.com/sug'

my_v = input('plz input a word: ')
data = {
    #girl 是要翻译的内容，应该由用户输入
    'kw': 'rl'
}

#使用parse对data进行编码
data = parse.urlencode(data).encode()

print(type(data))

#headers

headers = {
    #请求长度
    'Content-Length': len(data)
}

req = request.Request(url=baseurl,
                      data=data, headers=headers)

#有了 headers、data、url 就可以发送请求了

rsp = request.urlopen( data)

json_data = rsp.read().decode()

print(type(json_data))


json_data = json.loads(json_data)

# print(json_data['data'])

for item in json_data['data']:
    # print(item)
    print(item['k'], '---', item['v'])