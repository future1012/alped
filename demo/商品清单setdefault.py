# def displayinventory(sth):
#     totalnum = 0
#     print('Inventory: ')
#     for k,v in sth.items():
#         totalnum = totalnum + v
#         print(str(k) + ': ' +  str(v))
#     print('total is ' + str(totalnum))
#
# def addToInventory(inventory, addedItems):
#     for i in addedItems:
#         inventory.setdefault(i, 0)
#         inventory[i] = inventory[i] + 1
#     return inventory
#
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayinventory(inv)



# 展示物品清单函数
def displayinventory(sth):
    totalnum = 0
    print('Inventory: ')
    for k,v in sth.items():
        totalnum = totalnum + v
        print(str(k) + ': ' + str(v))
    print('total is ' + str(totalnum))
# 处理新增的物品，增加到原物品清单的字典中。
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayinventory(inv)