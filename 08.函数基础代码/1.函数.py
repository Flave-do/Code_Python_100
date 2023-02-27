
# 1.函数：把独立的代码块, 写进函数里重复使用

# 优点：
# 1.减少代码的重复性
# 2.代码可读性更好

# 2.函数格式  def 关键字
# def 函数名():
    # 函数体

# 函数名只能包括字母、下划线、数字，且数字不能开头
# 定义函数
# jiuge = [1, 2, 3]

# def jiuge():
#     print('这是九歌')


# 调用函数
# 基本写法：函数名()
# 调用多少次，函数里面的代码就执行多少次
# jiuge()

# 总结：
# 2.1必须先定义再去调用函数
# 2.2 不要跟变量名冲突


# 3.返回值   return
# 作用：
# 3.1 会给函数的执行者返回值,需要通过print打印出来
# 3.2 函数中遇到return，函数结束,下面的代码不会再执行


# def funa():   # 定义函数，函数名是funa
#     a = 10
#     b = [1, 2, 3]
#     c = {'name': 'zs'}
#     # print(a)
#     return a, 20, b, c  # return可以一次性返回多个数据,以元组的形式返回
#
# print(funa())   # 调用函数

def funb():
    print(123)
    print(456)
    # print(789)

# funb()

def func():
    a = ['中文']
    print('九歌')
    return 123, a
    # return 123, a        # 只要有一个return执行了，那么函数结束，下面的不会再执行
    # return 789
    # return 456

# print(func())

def add():
    a = 1
    b = 2
    return a+b

print(add())



# 总结：
# 1.return返回值
# 1.1 如果return后面写了一个值, 返回给调用者这个值，通过print打印
# 1.2 如果return后面写了多个值,以元组的形式返回
# 1.3 return后面什么都不写，返回的结果是None

# 2.return跟print区别：
# 2.1  return之后的语句不执行, print会一直执行
# 2.2 return返回结果, print是输出，打印的功能




