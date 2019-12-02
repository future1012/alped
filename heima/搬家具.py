class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = int(area)

    def __str__(self):
        return f'this is a {self.name}, it\' area is {self.area}.'

class Home():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return  f'房子的位置: {self.address}, 房子的面积：{self.area}, 房子的剩余面积: {self.free_area}' \
            f' 房子里的家具：{self.furniture}'

    def add_furniture(self,item):
        if item.area <= self.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('房子空间不足.')

desk = Furniture('桌子',4)
chair = Furniture('椅子', 2)
fangzi = Home('beijing', 1200)
ball = Furniture('篮球场', 2000)

fangzi.add_furniture(desk)
print(fangzi)
fangzi.add_furniture(chair)
print(fangzi)
fangzi.add_furniture(ball)
print(fangzi)
