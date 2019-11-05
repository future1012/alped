import  os,shutil

'''
选择性拷贝
编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。
不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。
'''

def copyfile2dir(srcdir, suffix, distdir):
    print('当前目录是' + os.getcwd())
    print()
    if not os.path.exists(distdir):
        os.mkdir(distdir)
    for foldername,subfolername, filenames in os.walk(srcdir):
        for filename in filenames:
            filesuff = filename.split('.')[1]
            if filesuff in suffix:
                fileabspath = os.path.join(foldername,filename)
                shutil.copy(fileabspath, distdir)
                print('已拷贝：{} 到 {}'.format(fileabspath,distdir))

if __name__ == '__main__':
    copyfile2dir(r'D:\soursedir', ['txt','pdf','docx','xls','xlsx'], r'C:\Users\tengy\Desktop\distdir')
