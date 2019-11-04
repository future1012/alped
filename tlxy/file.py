#coding: utf8
# 假若他日相逢
# 我将何以贺你
# 以沉默
# 以眼泪
# strChar='_'
    # count = 1
    # while strChar:
    #     strChar = f.read(count)
    #     print(len(strChar))
        # print(strChar, end='')
        # count += 1
# import time
# with open(r'test01.txt', 'r', encoding='UTF-8') as f:
#     strChar = f.read(3)
#     while strChar:
#         print(strChar)
#         time.sleep(1)
#         print('-'*3)
        # strChar = f.read(3)
seq = ['菜鸟 1\n', '菜鸟 2']
with open('test01.txt', 'a', encoding='utf-8') as f:
    f.writelines(seq)
