class Person(object):
    def __init__(self, gun):
       self.gun = gun

    def fire(self):
       self.gun.shoot()

    def fillBulletbox(self,count):
        self.gun.bulletBox.count = count
        print('!!! Filled with {} bullets'.format(self.gun.bulletBox.count))
