class Listinfo(object):
    def __init__(self,list):
        self.list = list

    def add_key(self,new_list):
        if isinstance(new_list,list):
            self.list.extend(new_list)
            return  self.list
        else:
            self.list.append(new_list)
            return self.list

    def del_key(self):
        return  self.list.pop()

L1 = [1,2]
L2 = 4
l = Listinfo(L1)

print(l.add_key(L2))
# print(l.del_key())

