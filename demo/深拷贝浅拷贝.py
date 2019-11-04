import copy
L = [1,2,3,4,[1,2,3]]
L1 = copy.copy(L)
L2 = copy.deepcopy(L)
L[4][1] = 9
print(L)
print(L1)
print(L2)

