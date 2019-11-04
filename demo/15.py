import copy
L = [1,2,3,4,[5,6,7]]
print(id(L))
L1 = copy.copy(L)
print(id(L1))
L2 = copy.deepcopy(L)
print(id(L2))
print('L1等于L2吗？')
print(L1 == L2 )
print('L1是L2吗？')
print(L1 is L2)
print('现在将列表L的内存列表的第三个元素值改成77： ')
L[4][2] = 77
print('这是L ：{}'.format(L))
print('这是L1：{}'.format(L1))
print('这是L2：{}'.format(L2))

