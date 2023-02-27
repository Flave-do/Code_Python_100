
# 1. 魔法方法/魔术方法
class A(object):
    pass



# print(dir(A))  # 查看类里面的魔法方法

# 1.1 __doc__ 表示类的描述信息
# class B:
#     '''这是我打的注释'''
#
#     pass
#
# print(B.__doc__)

# 1.2 __str__ :类中如果定义了str方法,那么打印对象时，默认输出该方法的返回值
# 通常是返回一个字符串，作为这个对象的描述信息
# str输出是给人看的，repr输出是给程序员debug看的

class C:
    def __repr__(self):
        return '嘻嘻'

    def __str__(self):
        return '哈哈哈'   # 返回值必须有，而且一定是字符串类型

          # 返回值必须有，而且一定是字符串类型

c = C()
print(c)  # 直接打印实例化的对象

# 1.3 __module__: 表示当前操作的对象是在哪个模块
# 和__class__：表示当前操作的对象的类是什么

# import test
#
# py = test.Py()
# print(py.__module__)   # 输出模块
# print(py.__class__)    # 输出类

# 1.4 __call__  ： 允许一个类的实例像函数一样被调用
# class B:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('这是call')
#         print(args)
#
# b = B()
# b('we')   # call方法的执行是由对象名后加括号触发   ， 对象名()或者类名()()
#
# B()()