class Gun(object):
    def __init__(self, bulletBox):
       self.bulletBox = bulletBox


    def shoot(self):
        if self.bulletBox.count == 0:
            print('!!! No bulletbox!')
        else:
            self.bulletBox.count -= 1
            print('Shoot 1 bullet, and {} bullets left'.format(self.bulletBox.count))
