
# 1.函数引用
def test():
    print(123)

# 调用函数
# test()
# 使用id()函数获取内存空间的地址
# print(id(test))

# 引用函数
# te = test
# print(id(te))

# 通过引用调用函数
# te()


# 2.闭包
# 条件：
# 2.1 函数中嵌套一个函数
# 2.2 内部函数使用了外部函数的变量
# 2.3 外部函数的返回值是内部函数的函数名

# 函数嵌套
# def outer():
#     n = 10
#     def inner():
#         n = 20
#         print('inner：', n)
#     print('outer:', n)
#     inner()

# outer()

# 闭包一：
# def outer():  # 外层函数
#     a = 10
#     def inner():   # 内层函数
#         b = 20
#         # 在内函数中，使用到了外函数的变量
#         print(a + b)
#     # 外函数的返回值是内函数的引用
#     return inner

# print(outer())  # inner函数的引用
# 第一种写法
# outer()()

# 第二种写法
# ot = outer()  # ot 保存了inner函数的引用
# ot()  # 相当于执行inner函数

# 闭包二：
# def test():  # 外函数
#     li = []  # 空列表
#     def test_in(val):  # 内函数
#         li.append(val)
#         res = sum(li)  # 列表中的元素进行求和
#         print(li)
#         return res
#     # 外函数返回内函数的引用
#     return test_in
#
# # 闭包的变量实际上只有一份，每次调用内函数都是在使用同一份闭包变量
# te = test()
# print(te(10))  # 调用内函数test_in
# print(te(20))
# print(te(30))

# 3.装饰器
# 标准装饰器写法:
# def wrapper(func):
#     def inner(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return inner

def check(fn):  # 外函数  fn是形参  （fn是需要修饰的函数名）    fn=speak
    def inner():  # 内函数
        print('请先登录')
        fn()   # speak()
    return inner  # 返回内函数的引用


# 使用装饰器来装饰函数
# 第一种:
# 需要修饰的函数
def speak():
    print('发表评论')

# ch = check(speak)  # speak是实参
# # print(ch)  # inner函数的引用
# ch()

# 第二种：语法糖@
# @check   # 等价于 ch = check(speak)
# def speak():
#     print('发表评论')
#
# speak()






