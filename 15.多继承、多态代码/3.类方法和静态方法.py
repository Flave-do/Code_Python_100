
# 1.新式类以及经典类
# python2.x版本中 存在两种：新式类和经典类
# python3.x :取消了经典类, 使用的都是新式类
#     class Person:
#     class Person():
#     class Person(object):  # 推荐使用这一种
#
#     三种写法没有区别
#
# object是python中为所有对象提供的基类

# 2.类方法：使用@classmethod
# 类方法就是针对类对象定义的方法，内部可以直接访问类属性或者调用其他的类方法
# 类方法中第一个参数是cls  --- 类对象

class Person(object):
    name = '森森'   # 类属性
    # 类方法
    @classmethod
    def get(cls):
        print(cls)  # cls就是代表类对象
        print('名字是：', cls.name)

    # 类方法对类属性修改之后，再去访问就发生了变化
    @classmethod
    def set(cls, Name):
        cls.name = Name

p = Person()

# print(p.name)  # 实例对象查看类属性
# p.get()  # 通过实例对象调用
# Person.get()   # 通过类对象调用
# p.get()
# # print(Person)  # 类对象
# p.set('超超')
# p.get()


# 3.静态方法   @staticmethod
# 静态方法就是类中函数, 不需要实例

# class Dog(object):
#     # 静态方法
#     @staticmethod
#     def eat():   # 主要是来存放逻辑性的代码
#         print('狗狗在啃骨头')
#
# dog = Dog()
# dog.eat()
# Dog.eat()


# 总结：
# 1.实例方法：默认self参数
#     方法内部需要访问实例属性，调用实例方法
#
# 2.类方法：默认cls参数
#     方法内部需要访问类属性
#
# 3.静态方法：
#     方法内部不需要访问实例属性和类属性