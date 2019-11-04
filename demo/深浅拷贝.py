import copy
print('====情况1====')
L = [1,2,3,4]
L1 = L
L = [5,6,7,8]
print(L)
print(L1)
print('====情况2====')
L = [1,2,3,4]
L1 = L
L[0] = 5
L[1] = 6
L[2] = 7
L[3] = 8
print(L)
print(L1)
