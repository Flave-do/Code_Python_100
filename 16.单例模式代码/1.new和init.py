
# 1. new 和 init

# class Test:
#     def __init__(self, name):  # 初始化
#         self.name = name  # 实例属性

    # def funa(self):   # 实例方法
    #     print(self.name)

# 实例化对象
# te = Test('旺仔好开森')
# te.funa()

# 1.1  顺序： 最先调用的是__new__方法,然后是__init__方法
# init是在类实例对象创建之后调用, new就是创建这个实例对象的方法
# 类中写了init和new，先调用new方法创建对象，再给init去用；
# 因为我们重写了new方法，导致它原来的功能没有了，所以new还是可以调用，但是init不能

class Test2(object):
    def __new__(cls, *args, **kwargs):  # 左右两边双下划线
        print('这是new中的：', cls)
        print('森森同学')  # 相当于重写了object里面的new方法

    def __init__(self):
        print('这是init中的：', self)
        print('旺仔同学')


# te2 = Test2()
# print('这是类：', Test2)

# 1.2  new方法作用
#     1.在内存中为对象分配空间
#     2.返回对象的引用
# python解释器获取到对象的引用后，把引用作为第一个参数，传递给init方法


# 2.  重写new方法
# 举例一：
class Person(object):
    def __init__(self):    # 3.利用这个实例对象来调用init方法
        print('李云龙同学')  # 4.执行init里面的代码

    def __new__(cls, *args, **kwargs):  # 缺少了创建对象的功能
        print('Kylin同学')        # 1.先执行new方法的代码
        # 重写父类方法：new  ---- 扩展
        # 父类名.方法名(cls)
        # return object.__new__(cls)
        # super().方法名(cls)
        return super().__new__(cls)  # 2.new方法返回Person类的实例对象

# p = Person()
# 举例二：
class Human(object):
    def __init__(self, name):
        self.name = name
        print('这是init方法中的self:', self)
        print('名字是：', self.name)
        print('这是init')


    def __new__(cls, *args, **kwargs):
        print('这是new方法中的cls:', cls)
        print('这是new')
        print('这是new方法中返回的值：', super().__new__(cls))
        return super().__new__(cls)

print('这是类外面的：', Human)
hu = Human('悟')  # 实例化对象
print('这是实例化的对象：', hu)


# 总结：
# 一个对象的实例化过程，先执行类的new方法,
# 如果没有写，默认调用object里面的new方法，返回一个实例化对象,
# 然后再调用init方法，对这个对象进行初始化
#
# 总结init和new区别
# 1.new方法创建对象   init方法初始化对象
# 2.new 返回对象引用   init 定义实例属性
# 3.new控制生成一个新实例的过程，是类级别的方法
#     init初始化一个实例，是实例级别的方法
# 4. 先调用new方法再调用init方法






