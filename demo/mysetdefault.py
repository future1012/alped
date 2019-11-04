allGuests = {
    'Alice': {'apples': 15, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def totalBrought():
    item_num = {}
    for item in allGuests.values():
        for k,v  in item.items():
            item_num.setdefault(k,0)
            item_num[k] = item_num[k] + v
    print(item_num)

totalBrought()

# if 'color' not in spam:
#     spam['color'] = 'black'
#
# spam.setdefault('color', 'black')



