
# 1.property属性：用起来跟使用的实例属性一样的特殊属性
# 有两种方式
# 1.1 类属性：在类中定义值为property对象的类属性
# property中有四个参数：
#     1.方法名---查看属性自动触发执行的方法
#     2.方法名---修改属性自动触发执行的方法
#     3.方法名---删除属性自动触发执行的方法
#     4.字符串--调用对象.属性.__doc__， 属性的描述信息
class A(object):
    def __init__(self):
        self.name = '悟zs'
    # 查看
    def get_name(self):
        return self.name
    # 修改
    def set_name(self, name2):
        self.name = name2
    # 删除
    def del_name(self):
        del self.name

    # 定义一个属性
    pro = property(get_name, set_name, del_name, '悟空空')

# a = A()
# print(a.pro)      # 调用get_name方法
# a.pro = '陈浩南'  # 调用set_name方法
# del a.pro
# print(a.pro)      # 调用del_name方法
# 查看property属性的描述信息
# print(A.pro.__doc__)

# 1.2 装饰器：在方法上应用装饰器
# @property 、 @方法名.setter   @ 方法名.deleter
# 1.定义： 在实例方法的基础上添加@property 装饰器，并且仅有一个self参数
# 2.调用： 调用时，无需括号

# class Person(object):
#     def funa(self):
#         print('彭于晏')
#
#     @property
#     def funb(self):
#         print('权志龙')
#
# pe = Person()
# pe.funa()   # 调用实例方法
# pe.funb     # 调用property属性


# 旺森店举例

class Milk_tea(object):
    def __init__(self):
        # 旺仔原价
        self.price = 10
        # 活动折扣
        self.dist = 0.9

    # 查看
    @property
    def milk(self):
        print('欢迎品茶')
        print('旺仔的原价是：', self.price)
        new_price = self.price * self.dist
        print('活动价：', new_price)

    # 修改
    @milk.setter
    def milk(self, val):
        self.price = val
        print('店内生意好, 九歌决定调价, 旺仔价格变为：', self.price)


    # 删除
    @milk.deleter
    def milk(self):
        print('价格太高，销量不好了，旺森店倒闭')
        del self.price


mt = Milk_tea()
mt.milk        # 获取旺仔价格
mt.milk = 20   # 修改旺仔价格
del mt.milk    # 删除旺仔价格














