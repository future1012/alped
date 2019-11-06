import os,shutil,re

def fillnumfile(prefix,destdir):
    numRegex = re.compile(r'('+ str(prefix) +'\d+\.)')
    localfilelist = []
    #清理本地文件列表，将不符合编号要求的排除
    for i in os.listdir(destdir):
        if numRegex.findall(i):
            localfilelist.append(i)
    #比对本地文件名是否安装编号排序，否则重命名
    for num in range(0,len(localfilelist)):
        becheckfile = '{}{}.txt'.format(prefix, str(num+1).rjust(3,'0'))
        becheckfilepath = os.path.join(destdir, becheckfile)
        if os.path.join(destdir,localfilelist[num]) != becheckfilepath:
            shutil.move(os.path.join(destdir, localfilelist[num]),becheckfilepath )
            print('{} rename to {}'.format(localfilelist[num], becheckfilepath))
        else:
            print('{} 编号正常'.format(localfilelist[num]))

if __name__ == '__main__':
    fillnumfile('ty', r'C:\Users\tengy\Desktop\destdir')
