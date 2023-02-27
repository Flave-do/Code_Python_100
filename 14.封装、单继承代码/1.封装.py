# 上课的时候，老师的QQ有另一位老师在登录
# 下课后没有回复的同学，再私聊一下（可能会有遗漏）
# 解答课--周五      函数作业---周六课前讲，有录播
# 装饰器作业不强制交, 先理解装饰器再去做作业

# 1.面向对象  --- 类和对象  类：属性和方法
class Lesson:  # 定义一个类，类名Lesson
    thing = '学习'   # 类属性

    def __init__(self, name):  # 初始化, self代表实例对象本身
        # print('这是init')       # 实例化对象时，会自动调用init方法
        self.name = name       # 实例属性

    def study(self):   # 实例方法
        print(f'{self.name}同学在学习')


# 实例化对象
le = Lesson('夜夜夜夜夜')
# le.study()
# Lesson.study()  # 类不能调用实例方法

# 对象、类调用类属性
# print(le.thing)
# print(Lesson.thing)

# 对象调用实例属性
# print(le.name)
# print(Lesson.name) # 类不能调用实例属性

# 总结：
# 1.类属性：类可以访问到，实例对象也可以访问
# 2.实例属性：类访问不到，实例对象可以访问
# 3.类属性属于类的，所有实例对象共享一个属性； 实例属性属于实例对象，互不干扰

# 2.封装  --- 面向对象
# 封装意义：
# 2.1 将属性和方法放在一起作为一个整体，然后通过实例化对象来处理
# 2.2 隐藏内部实现细节，只需要和对象及其属性和方法进行交互就可以了
# 2.3对类的属性和方法增加访问权限控制

# 私有属性：不能在类的外部调用
# python中定义私有属性或方法，需要在前面加上__(双下划线)
# _name:单下划线开头，也是私有属性，实例化的对象可以访问

class Tea:
    name = '红茶'    # 类属性
    __milk = '奶茶'  # 私有属性
    _black = '黑茶'

    def find(self):  # 实例方法
        print(Tea.__milk)  #在类内部访问私有属性
        # print(Tea.name)  # 实例方法中访问类属性， 类名.属性名


# te = Tea()
# te.find()
# print(te.name)
# print(te._black)
# print(te.__milk)  # 报错，私有属性不能在类外部直接访问

# _类名__属性名 (了解)  最好不要这样做
# print(te._Tea__milk)


class Person:
    def __init__(self):
        self.__name = '十九歌'

    def __speak(self):  # 私有方法
        print('这是speak')


    def find(self):
        print(self.__name)  # 类内部访问私有属性
        self.__speak()      # 类内部调用私有方法

# pe = Person()
# pe.find()

# 总结：
# 1.类中的私有属性、方法，都不能通过对象直接访问，需要在类内部访问
# 2._xx：单下划线开头, 声明私有权限，但是实例对象可以访问
# 3.__xx: 双下划线开头, 声明私有权限, 无法在类外部直接访问
# 4.__xx__: 前后双下划线， 魔术方法,不用自己这样去定义名字






