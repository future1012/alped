from bs4 import BeautifulSoup
import requests

#baidu = requests.get("http://www.women.org.cn").content
baidu = requests.get("https://jobs.zhaopin.com/CC187965628J00083889410.htm").content

# print(baidu)
soup = BeautifulSoup(baidu,'html.parser')

#获取网页标签里的子标签
# print(soup.body.div.attrs)

links = soup.findAll('a')

for l in links:
    print(l.string)