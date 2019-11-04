# from types import MethodType
# class A():
#     pass
#
# def say(self):
#     print('hello....')
#
#
# # a = A()
#
#
# # A.say = say
#
# a=A()
# # a.say=say()
# a.say=MethodType(say,A) # 将say函数绑定到A类上
# a.say()

##############################
# def say(self):
#     print('Saying...')
#
# def talk(self):
#     print('Talking...')
#
#
# a= type('A', (object,),{'c_say':say,'c_talk':talk})
#
#
# aa = a()
#
# # print(dir(aa))
#
#
# aa.c_say()
# aa.c_talk()

#元类 metaclass

# #元类写法固定，必须继承自type，如下：
# class TENGYUEMetaClass(type):
#     def __new__(/cls, name, bases,attrs):
#         print('我是元类')
#         attrs['id']='000000'
#         attrs['addr']='beijing'
#         return  type.__new__(cls, name, bases, attrs)
#
# class Teacher(object, metaclass=TENGYUEMetaClass):
#     pass
#
# t=Teacher()

# print(t.id)


# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def run(self):
#         return ('I can run')
#
#     def talk(self):
#         return ('I can talk')
#
#
# s = Student('ty',18)
#
#
# class Student1(Student):
#     pass
#
# my_name=s.name
# my_age=s.age
# run=s.run()
# talk=s.talk()
#
# s1=Student1('SJ',16)
#
# print('My name is {0}, and I {1} years old, {2}, and {3}'.format(my_name,my_age,run,talk))
#
#
# na = s1.name
# print(na)


# class Student():
#     name = 'sj'
#     age = 16
#     __age1 = 160
#
#     def say(self):
#         self.name= 'ty' #如果注释掉此行和下边一行，上边的类属性会生效
#         self.age = 18
#         print('My name is {0},and I am {1} years old'.format(self.name,self.age))
#         print('My name is {0},and I am {1} years old'.format(__class__.name,__class__.age))  #访问类属性用'__class__'
#
#     def sayagain(s):
#         print('My name is {0},and I am {1} years old'.format(s.name,s.age))
#
# s = Student()
#
# s.say()   #如果这里不调用，下边的调用，变量值会找上边的类属性,如果调用了，那么下边再次调用也会跟这个调用使用同样的变量值, 变量调用从上到下
# print('*' * 20)
# s.sayagain()
#
# print(s._Student__age1)   #打印私有变量     对象名_类名+ 私有变量名


# class A():
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D():
#     pass
#
#
# #res = issubclass(B, C,)
# res = issubclass(C, object)
#
# print(res)
#
# a = A()
# ies = issubclass(B, object)
# #检查第一个元素是否是第二个元素的一个实例（一个对象是否是一个类的一个实例）
# print(isinstance(a,A))


# class Student():
#     name = 'ty'
#     age = 18

# #检查一个属性或者方式是否属于第一个元素（类）的成员。
# s = Student()
# # res = hasattr(s, 'name')
#
# # print(res)
#
#
# setattr(s,'name1',xxx)
# print(s.name)

# print(help(setattr))


#使用setaddr
# class People:
#     country='China'
#     # def __init__(self,name):
#     #     self.name=name
#     name = 'aaa'
#     # def people_info(self):
#     #     print('%s is xxx' %(self.name))
#
# obj=People()
#
# setattr(People,'x',111) #等同于People.x=111
# print(People.x)
#
#
# class Student():
#     name = 'ty'
#     age = 18
#
# s = Student()
#
# print('My name is {0}'.format(s.name))
# setattr(s,'name','sj')
# setattr(s,'addr','beijing')
# print('My name is {0}'.format(s.name))
# print('My addr is {0}'.format(s.addr))


# class Persion():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.setname(name)
#
#     def hello(self):
#         return ('My name is {0}, and I {1} years old.'.format(self.name,self.age))
#
#     #因为在给name或者其他变量添加value的时候每个人的写法不同意（例如可能是：TengYue,tengyue,TENGYUE),
#     # 为了统一，写法如下，全部大写：
#     def setname(self,name):
#         self.name = name.upper()
#
#
#
# p = Persion('tengyue', 18)
# p1 = Persion('sunjing', 16)
# print(p.hello())
# print(p1.hello())

#类成员描述，property
# class Persion():
#
#     def fget(self):
#         return self.name
#
#     def fset(self,name):
#         self.name = name.upper()
#
#     def fdel(self):
#         self.name = 'Noname'
#
#     myname = property(fget,fset,fdel, '我是文档。')
#
#
# p = Persion()
# # p.fset('tengyue')
# p.myname = 'sunjing'
# print(p.name)
#
# del p.myname
# print(p.name)

# #心形
# import time
# sentence = input("想打印的话：")
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)
# class Student():
#     def __init__(self, name):
#         self._name = name
#
#     def __gt__(self, obj):
#         print("哈哈， {0} 会比 {1} 大吗？".format(self, obj))
#         return self._name > obj._name
#
#     # def __str__(self):
#     #     return 'lalala'
#     #形如 "哈哈， one 会比 two 大吗？" 打印
#     def __str__(self):
#         return "{0}".format(self._name)
#
# # 作业：
# # 字符串的比较是按什么规则
# stu1 = Student("one")
# stu2 = Student("two")
#
# print(stu1 > stu2)
# print(stu1)
# print(stu2)

#super()
# class Persion():
#     def __init__(self,name,age):
#         self.name = 'sj'
#         self.age = 16
#
# class Student(Persion):
#
#     def __init__(self,name,age,num):
#         self.name = name
#         self.age = age
#         self.num = num
#         super().__init__(name,age)
#
# i = Student('tengyue',18,25)
#
# print(i.name)
# print(i.age)
# print(i.num)


#Dog 类距离，有文档
# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self,name,age):
#        """初始化name和age属性"""
#        self.name = name
#        self.age = age
#
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title() + " is now sitting")
#
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         print(self.name.title() + " roll over!")
#
#
#
# d = Dog('dahuang', 6)
#
# d.sit()
#
# print(Dog.__doc__)
#
# # print(help(Dog))
# print(help(d))

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print(i,j,k, end=',')

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             for l in range(1,5):
#                 if (i !=j ) and (j != k ) and (k != l ) and (l != i ):
#                     print(i,j,k,l)

