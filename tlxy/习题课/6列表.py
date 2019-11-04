#append/extend/insert   区别

list_a = [1,2,3]
list_b = [4,5,6]

list_a.append(list_b)
print(list_a)

list_a.extend(list_b)
print(list_a)

list_a.insert(1,list_b)
print(list_a)


member = ['六','六','六','六']

a = [1,3,5,7]
b = [99,88,77,66]

c = zip(a,b)
print(c)
for i,j in c:
    member.insert(i,j)

print(member)



d = [1,[1,2,['aaa']],3,5,8,13,18]

d[1][2][0]='bbb'
print(d)

############
#还原列表推导式：
#l = [(x,y) for x in range(10) for y in range(10) if x%2==0  if y%2!=0]
print(ll)
l = []
for x in range(10):
    for y in range(10):
        if x%2 == 0 and y%2!=0:
            l.append((x,y))
print(l)