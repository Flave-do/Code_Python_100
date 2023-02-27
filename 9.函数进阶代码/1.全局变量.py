
# 1. 匿名函数: 没有名字的函数
# 语法： 函数名 = lambda 形参:返回值

def funa(a, b):
    return a+b

# print(funa(3, 4))

# funb = lambda a, b: a+b  # a,b是形参    a+b是返回的表达式
# print(funb(6, 7))

# 取列表中下标为0和2的元素
li = ['a', 'c', 'b', 'd']
# print(li[0])
# print(li[2])

# func = lambda x: (x[0], x[2])  # x是形参
# print(func(li))

# 求平方值
def test(a):
    return a**2

# print(test(2))

# 语法： 函数名 = lambda 形参:返回值
# te = lambda b: b**2
# print(te(8))

# te2 = lambda b: print(b**2)
# te2(8)


# 2.内置函数
# 查看所有的内置函数
# import builtins
# print(dir(builtins))

# 2.1 abs绝对值
# print(abs(-4))
# 2.2  sum求和
# print(sum([1, 2, 3]))
# print(sum((1, 2, 3)))
# print(sum({1, 2, 3}))

# 2.3  min()最小值   max()最大值
# print(min([1, 2, 3]))
# print(max([1, 2, 3]))

# 2.4 zip()  拉链函数
# a = [1, 2, 3]
# b = ['a', 'b', 'c', 'd', 'e']
# print(list(zip(a, b)))
# list()会转换成列表
# zip() 就是把几个类型对齐，然后按列输出，里面是元组组成的内容; 个数不一致，按长度最短的返回

# 2.5 map 映射函数：对对象中的每一个元素进行映射，分别执行函数
# map(函数, 对象)

# li2 = [1, 2, 3]
#
# def funb(x):
#     return x*2
#
# mp = map(funb, li2)
# print(list(mp))

# 2.6  reduce()  对参数序列中元素进行累积
# reduce(函数, 对象)

# from functools import reduce  # 一定要先导入模块
#
# def func(x, y):
#     return x+y
#
# res = reduce(func, [1, 2, 3])
# print(res)


# 3.拆包
li3 = [1, 2, 3, 4]
# a, *b = li3   #  a取一个值，其他的都放在b中
# print(a, b)
# a, *b, c = li3  # a和c 取开头和结尾的数据，中间的数据放到了b中
# print(a, b, c)

a, *b = li3
print(a, b)







