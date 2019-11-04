import re

phoneNumberre = re.compile(r'(\(\d{3}\)-)?(\d{3})-(\d{4})')
starnameRegex = re.compile(r'teng(xiao)*yue')
plusnameRegex = re.compile(r'sun(xiao)+jing')
haReggex = re.compile(r'(ha){1,2}')
mo = phoneNumberre.search('my phone number is (111)-123-4567')
starnameMo = starnameRegex.search('my name is tengxiaoyue')
plusnameMo = plusnameRegex.search('my name is sunxiaoxiaojing')
print('这是groups: %s ' % str(mo.groups()))
print('这是group: %s ' % str(mo.group()))
print(starnameMo.group())
print(plusnameMo.group())

hamo = haReggex.search('hahaha')
print(hamo.group())