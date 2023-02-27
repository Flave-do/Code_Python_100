
# 1.继承： 子类拥有父类的所有方法和属性
# 继承分为单继承和多继承
# class Father:   # 父类
#     name = '张'
#
#     def speak(self):
#         print('会说话')
#
# class Son(Father):  # 子类一  儿子
#     def work(self):
#         print('在工作')
#
# class Daug(Father):    # 子类二    女儿
#     pass
#
# son = Son()
# son.speak()
# print(son.name)
# son.work()
#
# daug = Daug()
# daug.speak()


# 继承传递性：子类拥有父类以及父类的父类中所有的属性和方法
class Person:   # 父类的父类   --- 爷爷
    Sname = '动物类'      # 类属性
    def __init__(self, name, age):
        self.name =name   # 实例属性
        self.age = age

    def eat(self):  # 实例方法
        print(f'{self.name}在吃东西, 今年{self.age}')


class Jiuge(Person):  # 父类  ---  爸爸
    def study(self):
        print('我在学习')

# 实例化子类对象，对象执行父类的属性/方法
# jiuge = Jiuge('九歌', 18)
# jiuge.eat()

class Jiuge19(Jiuge):  # 子类   ---- 儿子
    pass

# jiuge19 = Jiuge19('十九歌', 19)
# jiuge19.eat()
# jiuge19.study()


# 2.重写
# 重写：父类的方法不能满足子类的需求时，可以对方法进行重写
# 2.1 覆盖父类的方法
#     如果父类的方法不能满足子类需要，在子类中重写编写父类方法
# 2.2 对父类方法进行扩展
#     实现方式:  使用super().父类方法() ;   父类名.方法(self)

# 覆盖
# class Human:        # 父类
#     def paly(self):
#         print('我在玩电脑')
#
#
# class ZS(Human):     # 子类一
#     def paly(self):
#         print('我张三不玩电脑，玩手机')
#
# class Ls(Human):  # 子类二
#     pass
#
# zs = ZS()
# zs.paly()

# 扩展:
# 1.父类名.方法(self)
# class Animal:     # 父类
#     def eat(self):
#         print('吃东西')
#
# class Dog(Animal):   # 子类
#     def eat(self):
#         # 父类名.方法(self)    在父类的基础上增加自己想要功能
#         Animal.eat(self)
#         print('啃骨头和吃翔')
#
#
# dog = Dog()
# dog.eat()


# 2.super().父类方法()
# super是一个特殊的类, super()就是使用super类创建出来的对象

# class Animal:     # 父类
#     def bark(self, name):
#         print(f'{name}动物都会叫')
#
# class Dog(Animal):  # 子类
#     def bark(self, name):
#         # super().方法名()
#         super().bark(name)
#         print(f'{name}狗是汪汪叫')
#         print('哈哈哈哈')
#
# dog = Dog()
# dog.bark('zs')











