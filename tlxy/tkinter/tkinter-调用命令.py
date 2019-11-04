#coding: utf-8
import tkinter
import os
# tkinter._test()


def showlabel():
    global base
    lb = tkinter.Label(base, text='show label')
    lb.pack()
    print('aaaaaaaaaaaaaaa')
    # os.system('calc')
    os.system('taskmgr')
base = tkinter.Tk()

base.wm_title("hello,world")

lb1 = tkinter.Label(base, text='PYTHON LABEL')
lb1.pack()

lb2 = tkinter.Label(base, text='aaaaaaa', background='green')
lb2.pack()

btn = tkinter.Button(base, text='打开任务管理器', command=showlabel)
btn.pack()
base.mainloop()