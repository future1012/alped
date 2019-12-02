class A():
    def __init__(self):
        self.num = 111

    def __str__(self):
        return str(self.num)


obj = A()

print(obj)

class B(A):
    pass

obj1 = B()
print(obj1)