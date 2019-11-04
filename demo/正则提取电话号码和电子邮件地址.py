#导入需要的模块
import  re,pyperclip

#测试文本
'''
Skip to main content
Home
Search form
Search
GO!
Topics
Arduino
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
JavaScript
Kids
LEGO?
LEGO? MINDSTORMS?
Linux & BSD
Skip to main content
Home
Search form
Search
GO!
Catalog
Media
Write for Us
About Us
Topics
Arduino
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
JavaScript
Kids
LEGO?
LEGO? MINDSTORMS?
Linux & BSD
Manga
Minecraft
Programming
Python
Science & Math
Scratch
System Administration
Early Access
Gift Certificates
Free ebook edition with every print book purchased from nostarch.com!
Shopping cart
3 Items Total: $53.48
View cart Checkout
Contact Us
No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 ext435 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950
Reach Us by Email
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Navigation
My account
Log out
Manage your subscription preferences.
About Us | ★ Jobs! ★ | Sales and Distribution | Rights | Media | Academic Requests | Conferences | Order FAQ | Contact Us | Write for Us | Privacy
Copyright 2018 No Starch Press, Inc
'''
#创建一个匹配电话号码的正则模式
phoneNumRegex = re.compile(r'''(    #结尾小括号将真个匹配的结果放在一个分组里, 分组1，如：'(123)-456-7890 ext 321'
(\(\d{3}\)|\d{3})?                  #匹配区号，这个区号可能带一个小括号，可能不带。分组2，如：(123)
(\s|-|\.)?                          #区号后边的分隔符，可能是一个空白字符、短横线或者一个点。分组3，如：'-'
(\d{3})                             #主号码的第一部分的3个数字。分组4
(\s|-|\.)                           #第二个分隔符，可能是一个空白字符、短横线、或者一个点。分组5
(\d{4})                             #主号码的后四位数字。分组6
(\s*                                #将分机符号和分级号码分成一个分组，分组7
(ext|ext.|x)                        #分机符号用ext或者ext.或者是一个x ,分组8
\s*                                 #分机符号和分机数字之间可能包括若干空白字符
(\d{2,5})                           #分级号码，分组9, 就是下边代码的groups[8]
)?                                  #分组7的结束括号
)''', re.VERBOSE)                   #分组1的结束括号，和使用冗长模式re.VERBOSE

#打印出正则查找的一个栗子
find_res = phoneNumRegex.findall('800.420.7240 ext 456')
print(find_res)

#创建一个匹配电子邮件地址的正则模式
emailRegex = re.compile(r'''(   #结尾的括号是第一个分组括号，这个括号要有啊。否则打印不完整啊
[a-zA-Z0-9-_%+.]+               #匹配@符号之前的地址，由中括号中的任意一种字符的一个或多个组成
@                               #电子邮件的@符号
[a-zA-Z0-9.-]+                  #域名中点（.)之前的部分，由中括号中的任意一种字符的一个或多个组成
(\.[a-zA-Z]{2,4})               #顶级域名部分,一个独立的分组2
)''', re.VERBOSE)               #第一个分组的结束括号，和使用冗长模式re.VERBOSE

#打印一个匹配邮件地址的栗子
print(emailRegex.findall(r'hahaha@qq.com'))

#将剪贴板中的内容写进text变量
text = str(pyperclip.paste())

#初始化一个空列表，存放匹配到的电话号码和电子邮件地址
matches = []

#匹配出电话号码,并追加到matches列表中
for groups in phoneNumRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

#匹配出电子邮件地址,并追加到matches列表
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#打印匹配的结果
print(matches)
print('#'*20)

# 将匹配结果写进剪贴板,同时打印到标准输出
if len(matches):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
