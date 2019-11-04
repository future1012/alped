from multiprocessing import Process
import multiprocessing
from time import sleep, ctime
import os

# def clock(interval):
#     while True:
#         print("The time is {0}".format(ctime()))
#         sleep(interval)
#
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=clock, args=(5,))
#     p.start()


def info(title):
    print(title)
    print('Module name:', __name__)
    print('Parent process id: ', os.getppid())
    print('Itself id: ', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('ahahaha',))
    p.start()
    p.join()
