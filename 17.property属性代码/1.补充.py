
# 1.父类私有属性
# 子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法
# class Test(object):  # 父类
#     def __init__(self):
#         self.name = '九歌'  # 实例属性
#         self.__age = 18     # 私有属性
#
#     def funa(self):  # 实例方法
#         print(self.name)
#         print(self.__age)
#
#     def __money(self):  # 私有方法
#         print('我有私房钱')
#
#
# class Te(Test):   # 子类
#     def speak(self):
#         print('这是子类中定义的实例方法')
#         # 子类对象中，不能直接调用私有属性和私有方法
#         # print('访问父类的私有属性', self.__age)
#         # self.__money()
#
# te = Te()
# te.funa()
# te.speak()
# te.money()  # 不能直接访问

# 子类对象可以通过父类的公有方法，间接访问到私有属性和私有方法

# class Test(object):  # 父类
#     def __init__(self):
#         self.name = '九歌'  # 实例属性
#         self.__age = 18     # 私有属性
#
#     def funa(self):  # 实例方法
#         print(self.name)
#         print(self.__age)
#         print('我可以查看他的手机来知道私房钱的位置')
#         self.__money()
#
#     def __money(self):  # 私有方法
#         print('我有私房钱')
#
#
# class Te(Test):   # 子类
#     def speak(self):
#         print('这是子类中定义的实例方法')
#         # 调用父类的公有方法
#         self.funa()
#
# te = Te()
# te.speak()

# 2.异常类
# try:
#     print(a)
# except Exception as e:
#     print('哈哈哈哈，我就是错了怎么样')

# 自定义异常类，通常继承EXception类
# python中内置异常的名字都以Error来结尾，所以实际命名尽量跟标准的异常命名一样

# st = 'wer'
# print(st.isalpha())  # isalpha()如果字符串包含字母，返回为True

class JiugeError(Exception):
    def __init__(self):
        print('这是九歌自定义的异常类, 出错了')

try:
    inp = input('请输入数字：')
    if inp.isalpha():    # inp.isalpha()判断输入的字符串里面是不是包含字母
        raise JiugeError()  # 抛出异常
except JiugeError as e:
    print(e)

else:  # 没有异常就执行
    print('森森和旺仔')

finally:  # 有没有异常都执行
    print('九歌和廖俊涛')




