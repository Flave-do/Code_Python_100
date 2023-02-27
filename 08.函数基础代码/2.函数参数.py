# 1.函数参数-形参和实参

def add(a, b): # 定义函数的位置是形参
    return a+b

# print(add(23, 13))   # 函数调用的位置是实参

# 函数的传参：将函数的实参交给形参的过程

# def test(a, b):
#     print(a)
#     print(b)
#
# test([1, 2, 3], 'we')


# 2.函数参数
# 2.1必备参数 ： 写了几个形参，传几个实参

# 2.2默认参数：有默认值的参数
# def test2(name='zs'):
#     # pass   # pass执行不会报错
#     print(name)
#
# test2('李四')   # 调用函数

# 如果没有传实参，按默认的值去执行；给了实参就按传的值去执行

# 3.可变参数 *args
# args是一个普通的形参，前面加了*的话, 才有特殊的意义
# 我们传参的时候，会以元组的形式来接收值

# 传入的实参数量可以是任意多个，也可以没有
def test3(*args):
    print(args)
    print(type(args))  # 可以接收多个值，元组形式

# test3(1, 2, 3)
# test3()
# test3(4, 5, [1, 2])


# def test4(*we):
#     print(we)
#     print(type(we))
# test4('python')

# 4.关键字参数  **kwargs
# **也是有魔法作用,kwargs约定俗成作为形参
# 接收所有的关键字参数，将其转成一个字典, 赋值给kwargs这个形参
# 传入的实参数量可以是任意多个，也可以没有
def test5(**kwargs):
    print(kwargs)
    print(type(kwargs))
#
test5(name='zs', a=23, age=18)     #  键=值的形式


# def funa(*args, **kwargs):  # **kwargs必须在*args
#     print(args)
#     print(kwargs)
#
# funa(1, 'hello', ['学习', '快乐'], a=1, b=2, c=3)


# 5.函数嵌套
# 一个函数中还有一个函数

def test():  # 外函数
    print('这是test')
    def funa():    # 内函数
        print('这是funa')

    funa()  # 调用内函数

# test()  # 调用外函数