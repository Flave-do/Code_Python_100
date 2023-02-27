# 判断该字符串中包含多少个大写字符，并打印出来。
# st = 'HellO pYthon'
# print(st.upper())  # 小写转换为大写
# print(st)
# 第一种：
# n = 0  #  记录大写字符的个数
#
# st = st.replace(' ', '')
# for i in st:
#     if i == i.upper():
#         print(i)
#         n += 1
# print('大写的字符是：', n)

# 第二种:
st = 'HellO pYthon'
# print(st.isupper())   # 检测字符串是否由大写字符组成  是返回True,否则为False
# print(st.islower())   # 检测字符串是否由小写字符组成
# c = 0
# for i in st:
#     if i.isupper():
#         print(i)
#         c += 1
#
# print(c)


# 1.局部变量：在函数内定义的变量；作用范围就是函数内部
# def funa():
#     a = 10
#     print(a)
# funa()
#
# def funb():
#     a = 20
#     print(a)
# funb()

# 2.全局变量：在函数外定义的变量；可以在一个函数中使用，也能在其他函数中使用
# b = 'zs'
# def func():
#     print('这是func中的：', b)
#
# func()
#
# def fund():
#     print('这是fund中的：', b)
#
# fund()

# 3. 全局跟局部名字相同，此时理解为定义了一个局部变量，而不是修改全局变量
# c = 20      # 全局变量
# def fune():
#     c = 100   # 局部变量
#     print('函数内：', c)

# fune()
# print('函数外：', c)

# 4.修改全局变量
# global:在局部作用域中修改全局变量

# c = 20
# def fune():
#     global c  # 声明全局变量
#     c = 100
#     print('函数内：', c)
#
# fune()
# print('函数外：', c)

# a1 = [1, 2, 3]
# b1 = 10


# def test():
#     global a1, b1   # 一次对多个全局变量进行声明
#     a1 = 'qw'
#     b1 = 20
#     print(a1, b1)
#
# print(a1, b1)
# test()
# print(a1, b1)

# 5.nonlocal: 声明外层的局部变量
# 1.不能修改全局变量
# 2.只对局部起作用，离开嵌套函数,该变量就无效

# a = 10
# def funa():   # 外层函数 --- 大哥
#     a = 20
#     print('funa修改前：', a)
#     def funb():   # 内层函数 --- 小弟
#         nonlocal a
#         a = 40
#         print('这是funb函数：', a)
#
#     funb()
#     print('这是funa函数：', a)
#
# funa()
# print('函数外的a:', a)


# 总结：
# global 将局部变量变成一个全局变量; 可以用在任何地方
# nonlocal ：
# 在内层函数中修改外层函数的(非全局)变量;
# 只能用于嵌套函数中，并且外层函数中定义了局部变量














