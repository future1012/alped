class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')


class Prentice(Master,School):
    def __init__(self):
        #super().__init__()
        self.kongfu = '[独创煎饼果子配方]'
        self.__money = 2000000

    def __info_print(self):
        print('这是私有方法')

    #获取私有属性
    def get_money(self):
        return self.__money

    #修改私有属性
    def set_money(self,value):
        self.__money = value

    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)




daqiu = Prentice()


daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake()
daqiu.make_cake()
# daqiu._Prentice__money = 33333333333
# print(daqiu._Prentice__money)
# daqiu._Prentice__info_print()

money = daqiu.get_money()
print(money)

money = daqiu.set_money(666666)
money = daqiu.get_money()
print(money)
