import pprint
mesgs = 'oirkjfksad'
count={}

for c in mesgs:
    count.setdefault(c,0)
    count[c] = count[c] + 1

# print(count)
# pprint.pprint(count)
a=pprint.pformat(count)
print(a)