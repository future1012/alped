class Dog(object):
    def work(self):
        print('指哪儿打哪儿')

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('检测毒品')

class Persion(object):
    def work_with_dog(self,dog):
        return dog.work()

class Sdog(Dog):
    def superTest(self):
        super().work()

daqiu = Persion()
A = ArmyDog()
B = DrugDog()
daqiu.work_with_dog(A)
daqiu.work_with_dog(B)


s = Sdog()
s.superTest()
