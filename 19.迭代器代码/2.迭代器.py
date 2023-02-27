
# 1.迭代器 iterator
# iter()函数和next()函数
#
# 2.迭代器特性：
# 1>访问者不需要关心迭代器内部结构，只需要不断执行next函数h获取下一个元素
# 2>不能随机访问对象中的某个值, 只能从头到尾顺序的读取
# 3>访问到一半不能回退, 不能访问之前的值
# 4>适合遍历很大的数据集合, 节省内存，提升速度
#
#
# 3.如果不用for循环迭代,可以这样做：
# li = ['悟', '太阳', '蓝天色', '旺森', '程越']  # 列表是可迭代对象
# it = iter(li)   # 1.通过iter方法转变成迭代器对象
# print(it)
# print(next(it))   # 2.对获取到的迭代器对象不断使用next()函数来获取下一个值
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))   # 3.取完元素，再使用就会引发StopIteration

# 总结：
# 1> 先调用类型的iter()函数
#         iter()函数直接调用该对象的__iter__方法，并把__iter__方法的返回结果作为自己的返回值
#             这个用法通常被称为"创建迭代器"
# 2>使用next()函数调用__next__方法
# 3> 元素取完后再去, __next__方法将会引发StopIteration异常
#
# 直接调用方法：
# it2 = li.__iter__()
# print(it2.__next__())


# 4. 跟异常一起使用
# jiuge = {'韩非', '焰灵姬', '紫女', '卫庄', '弄玉'}
# tianxing = iter(jiuge)
#
# try:
#     while True:  # 死循环
#         print(next(tianxing))
#
# except StopIteration:
#     print('角色很多，但是人满了，还是等下辆车')

# 5.可迭代对象和迭代器
# 可迭代对象 Iterable      迭代器 iterator

# 可以for循环的属于可迭代对象
# 可以next()的是迭代器

# from collections.abc import Iterable, Iterator
#
# li = [1, 2, 3]
#
# print(isinstance(li, Iterable))  # True
# print(isinstance(li, Iterator))  # False
#
# my = iter(li)   # 转换为迭代器对象
# print(isinstance(my, Iterable))  # True
# print(isinstance(my, Iterator))  # True

# 迭代器对象一定是可迭代对象, 而可迭代对象不一定是迭代器对象
# 可迭代对象可以通过方法变成迭代器对象     （水果可以通过工厂加工变成水果罐头）


# 6.迭代器协议
# 概念：对象必须提供一个next方法，执行该方法要么返回迭代中的下一项，要么就引起一个StopIteration异常，终止迭代

# class Wu:
#     def __init__(self):
#         self.price = 10
#
#     def add(self):
#         self.price += 5
#         return self.price
#
#
# milk = Wu()  # 实例化对象
# print(milk.add())
# print(milk.add())
# print(milk.add())
#
# for i in milk:
#     print(i)     # TypeError: 'Wu' object is not iterable

# python中没有"迭代器"这个类的，具有以下两个特性的类可以称之为"迭代器"类
# 1. 有__iter__方法，返回迭代器本身
# 2. 有__next__方法, 返回下一个元素或抛出StopIteration异常

class Test:
    def __iter__(self):  # 类中定义了iter方法，这个类的实例就是一个迭代器，需要返回这个迭代器
        self.price = 10
        return self   # 返回self(实例对象本身)  表示自身就是自己的迭代器

    def __next__(self):
        self.price += 5
        return self.price

# 实例化对象
te = Test()

my_te = iter(te)
print(my_te)
print(next(my_te))
print(next(my_te))
print(next(my_te))

# a = 0
# while a < 5:
#     print(next(my_te))
#     a += 1

# for i in te:
#     if i <= 30:
#         print(i)
#     else:
#         break

# 在next方法中加入结束条件：
class Test:
    def __iter__(self):  # 类中定义了iter方法，这个类的实例就是一个迭代器，需要返回这个迭代器
        self.price = 10
        return self   # 返回self(实例对象本身)  表示自身就是自己的迭代器

    def __next__(self):
        if self.price >= 30:
            raise StopIteration('旺森奶茶店倒闭')
        self.price += 5
        return self.price

# 实例化对象
# te = Test()
# my = iter(te)
# for i in range(5):
#     print(next(my))