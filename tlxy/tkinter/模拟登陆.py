import tkinter
from tkinter import *

# base= tkinter.Tk()
# base= Tk()
root = tkinter.Tk()

root.wm_title('我要学python')
# root.geometry('500x300+500+200')

root.maxsize(600, 400)

root.minsize(300, 240)
# lb1 = tkinter.Label(base, text='姓名:')
# lb1.pack()
# lb2 = tkinter.Label(base, text='你好',background='red')
# lb2.pack()
#
#
#
# def  tylabel(event):
# # def  tylabel():
#     global base
#     tylb = tkinter.Label(base, text='滕跃')
#     tylb.pack()


# btn = tkinter.Button(base, text='哈哈', command = tylabel)
# btn.pack()

# btn2 = tkinter.Button(base, text='呵呵')
# btn2.bind("<Button-1>", tylabel)
# btn2['width']=20
# btn2['height'] = 4
# btn2['background'] = 'red'
# btn2.pack()

# Label(base, text='账号: ').grid(row = 0, sticky = W)
# Entry(base).grid(row = 0, column = 1, sticky = E)
# Label(base, text='密码: ').grid(row = 1, sticky = W )
# Entry(base).grid(row = 1, column = 1, sticky = E )
# Button(base, text='登陆').grid(row = 2, column = 1, sticky = E)
# base.mainloop()

def reg():
    name = etr1.get()
    pwd = etr2.get()
    if name == 'tengyue' and pwd == '123':
        lb3['text'] = '登录成功'
    else:
        lb3['text'] = '用户名或密码错误'
        etr1.delete(0,len(name))
        etr2.delete(0,len(pwd))


lb1 = tkinter.Label(root, text='账号: ')
lb1.grid(row = 0, column = 0, sticky = W)

etr1 = tkinter.Entry(root)
etr1.grid(row = 0, column = 1, sticky=E)

lb2 = tkinter.Label(root, text='密码: ')
lb2.grid(row = 1, column = 0, sticky = W)

etr2 = tkinter.Entry(root)
etr2.grid(row = 1, column = 1, sticky=E)
#输入密码用星号代替（遮挡密码）
etr2['show'] = '*'

btn1 = tkinter.Button(root, text='登录', command= reg)
btn1.grid(row = 2, column = 1,sticky = W)

lb3 = tkinter.Label(root, text='')
lb3.grid(row=3, column = 1, sticky = E)

root.mainloop()



