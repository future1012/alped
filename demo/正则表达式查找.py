import re,os

#将当前目录中的以'd'开头的文件名并且文件内容匹配到大写的字符所在的行打印出来
upperRegex = re.compile(r'([A-Z]+)')
fileRegex = re.compile(r'd.+\.txt')
path = '.'
for file in os.listdir(path):
   res = fileRegex.search(file)
   if res:
       print(res.group(0),':')
       filelines = open(file, 'r', encoding='utf-8').readlines()
       for line in filelines:
           if upperRegex.findall(line):
                print('匹配到大写字母的行：' + line.strip('\n'))


