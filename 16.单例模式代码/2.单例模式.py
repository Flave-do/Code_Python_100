
# 1.单例模式
# 单例: 是一种特殊的类，这个类只能创建一次实例
class Jiuge:
    def speak(self):
        print('九歌在说话')

jiuge = Jiuge()
# jiuge.speak()
shige = Jiuge()
# shige.speak()
# print(id(jiuge))
# print(id(shige))


# 类在实例化的时候, 执行同一个内存地址,称之为单例模式
# 单例模式实现的几种方法:
    # 1.通过@classmethod
    # 2.通过装饰器实现
    # 3.通过__new__实现
    # 4.通过导入模块时实现

# 2. 通过new方法实现
# 流程
# 1.定义一个类属性，初始值是None, 记录单例对象的引用
# 2.重写new方法
# 3.进行判断, 如果类属性为空，调用父类方法分配空间，在类属性中记录结果
# 4.返回类属性中记录的对象引用

class Exam(object):
    # 记录第一个被创建对象的引用 -- 类属性
    ins = None
    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空
        if cls.ins == None:
            # 2.类属性为空，调用父类方法，为第一个对象分配空间
            cls.ins = super().__new__(cls)
            # super().__new__(cls)   继承父类object里面的new方法，然后进行重写

        # 3.返回类属性保存的对象引用
        return cls.ins

# 每次实例化所创建的实例对象都是同一个(内存地址都是一样的)
# 每次实例化都会去调用new方法
print('未实例化前：', Exam.ins)
exam = Exam()    # 第一次实例化
print('第一次实例化后：', Exam.ins)
print('第一次实例化的对象', exam)
exam2 = Exam()  # 第二次实例化
print('第二次实例化后：', Exam.ins)
print('第二次实例化的对象', exam2)

# print(id(exam))
# print(id(exam2))

# 总结：
# 单例模式保证了在程序的不同的位置都可以且可以取到同一个对象实例,
# 如果实例不存在，就会创建一个实例，如果已经存在就会返回这个实例。

