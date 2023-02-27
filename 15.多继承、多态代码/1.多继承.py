
# 1.多继承： 子类可以拥有多个父类，具有所有父类的属性和方法
# class Father:      # 父类一
#     def test(self):
#         print('爸爸的双眼皮')
#
#
# class Mother:     # 父类二
#     def test2(self):
#         print('妈妈的高鼻梁')
#
# # 多继承可以让子类对象，同时具有多父类的属性和方法
# class Child(Father, Mother):   # 子类
#     pass
#
# ch = Child()
# ch.test2()
# ch.test()

# 父类中存在同名的方法
class Father:      # 父类一
    def test(self):
        print('爸爸的双眼皮')


class Mother:     # 父类二
    def test(self):
        print('妈妈的单眼皮')

# 父类中存在同名的方法, 谁先继承就用谁的
class Child(Mother, Father):   # 子类
    # 子类重写了父类的方法，所以先用子类自己的
    # def test(self):
    #     print('变成内双')

    def test(self):
        super().test()  # 调用父类方法，调用顺序遵循mro类属性的顺序(目前super不支持执行多个父类的同名方法)
        # 扩展父类方法： super().方法名()     类名.方法名(self)
        # Father.test(self)   # 继承father的

# ch = Child()
# ch.test()

# 确定子类调用方法的顺序
# MRO -- 方法搜索顺序
# print(Child.__mro__)  # 使用内置属性可以查看顺序(知道)
#
# 总结：
# 1.多继承可以继承多个类, 也继承了所有父类的属性和方法
# 2.如果多个父类中有同名的，默认使用第一个父类的属性和方法(根据mro的顺序来调用)
# 3.如果子类和父类的方法名和属性名相同，默认使用子类的。(子类重写了父类的东西)

# 继承举例:
# 一代：
# class Robot:   # 父类
#     def __init__(self, year, name):
#         self.year = year
#         self.name = name
#
#     def walk(self):   # 机器人的功能
#         print(f'{self.name}只能行走，遇到障碍物摔倒')
#
#     def produce(self):  # 机器人的信息
#         print(f'{self.year}年生产的, 名字是{self.name}')

# 实例化对象
# rt = Robot('2010', '九歌一号')
# rt.walk()
# rt.produce()

# 二代  --- 单继承
# class Robot2(Robot):  # 子类  --- 单继承
#     def walk(self):
#         print(f'{self.name}遇到障碍物会自己躲开')
#
#     def sing(self):
#         print('会唱歌')

# rt2 = Robot2('2020', '九歌二号')
# rt2.walk()
# rt2.produce()
# rt2.sing()

# 三代  --- 多继承
class Robot:   # 父类  --- 一代
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walk(self):   # 机器人的功能
        print(f'{self.name}只能行走，遇到障碍物摔倒')

    def produce(self):  # 机器人的信息
        print(f'{self.year}年生产的, 名字是{self.name}')


class Robot2:  # 父类  --- 二代
    def walk(self):
        print(f'遇到障碍物会自己躲开')

    def sing(self):
        print('会唱歌')


class Robot3(Robot2, Robot):   # 三代继承了两个父类
    def fly(self):
        print(f'{self.name}会在天上飞')


rt3 = Robot3('2030', '九歌三号')
rt3.walk()
rt3.sing()
rt3.fly()
rt3.produce()
