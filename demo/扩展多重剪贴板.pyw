import shelve
import pyperclip
from sys import argv


'''
该程序将利用一个关键字保存每段剪贴板文本。
例如，
当运行 py mcb.pyw save spam，剪贴板中当前的内容就用关键字spam保存。
通过运行 py mcb.pyw spam，这段文本稍后将重新加载到剪贴板中。
如果用户忘记了都有哪些关键字，他们可以运行 py mcb.pyw list，将所有关键字的列表复制到剪贴板中。

下面是程序要做的事：
针对要检查的关键字，提供命令行参数。
如果参数是 save，那么将剪贴板的内容保存到关键字。
如果参数是 list，就将所有的关键字拷贝到剪贴板。
否则，就将关键词对应的文本拷贝到剪贴板。
这意味着代码需要做下列事情：
从 sys.argv 读取命令行参数。
读写剪贴板。
保存并加载 shelf 文件。
'''

mcbshelf = shelve.open('mcbb')

if len(argv) == 3 and argv[1].lower() == 'save':
    mcbshelf[argv[2]] = pyperclip.paste()
elif len(argv) == 3 and argv[1].lower() == 'delete':
    del mcbshelf[argv[2]]
    print('delete {}'.format(argv[2]))
elif len(argv) == 2:
   if argv[1].lower() == 'list':
       pyperclip.copy(str(list(mcbshelf.keys())))
   elif argv[1].lower() == 'delete':
       mcbshelf.clear()
       print('clear.')
   elif argv[1] in mcbshelf:
       pyperclip.copy(mcbshelf[argv[1]])

mcbshelf.close()
