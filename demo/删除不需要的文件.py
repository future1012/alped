import  os
import shutil

def rmbigfile(dir,size):
    '''
    一些不需要的、巨大的文件或文件夹占据了硬盘的空间，这并不少见。如果你
试图释放计算机上的空间，那么删除不想要的巨大文件效果最好。但首先你必须找
到它们。
编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，比方说，超过
100MB 的文件（回忆一下，要获得文件的大小，可以使用 os 模块的 os.path.getsize()）。
将这些文件的绝对路径打印到屏幕上。
    '''
    for folder, subfoler, files in os.walk(dir):
        for file in files:
            filepath = os.path.join(folder, file)
            filesize = os.path.getsize(filepath)
            #size 单位是字节
            if filesize > size:
                os.unlink(filepath)
                print('Has delete {}'.format(filepath))


if __name__ == '__main__':
    rmbigfile(r'C:\Users\tengy\Desktop\destdir', 20000)
