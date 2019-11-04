class Dictclass(object):
    def __init__(self,dict):
        self.dict = dict

    def del_key(self,key):
       if key not in self.dict:
           print('{} 不存在'.format(key))
       else:
           self.dict.pop(key)
           return 'delete success'

    def get_dict(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 'not found'

    def get_key(self):
        return self.dict.keys()

    def upate_dict(self,new_dict):
        self.dict = dict(self.dict,**new_dict)
        return self.dict.values()

dict1 = {'a':1,'b':2,'c':3}
d = Dictclass(dict1)

print(d.upate_dict({'t':5,'y':6}))