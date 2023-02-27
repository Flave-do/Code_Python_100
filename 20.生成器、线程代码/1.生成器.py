
# 1.装饰器作业
# 编写装饰器，增加认证的功能

# def outer(fn):  # fn是被修饰的函数名
#     def inner():
#         name = input('请输入用户名：')
#         pwd = int(input('请输入密码：'))
#         if name == 'wu' and pwd == 123:
#             fn()
#         else:
#             print('你什么都捡不到')
#
#     return inner
#
# def add():
#     print('捡到一把屠龙刀')
#
# ot = outer(add)
# ot()


# 2.生成器  --  generator
# 在python中，使用了yield的函数被称为生成器
# 生成器就是一个迭代器

# 2.1 如何创建生成器
# 1.生成器表达式：类似于列表推导式
# [表达式 for 变量 in 可迭代对象]   ---  列表推导式的写法
# li = [i*5 for i in range(1, 20)]
# print(li)
#
# li2 = (i*5 for i in range(4))  # 生成器表达式
# print(li2)
# print(next(li2))
#
# for a in li2:
#     print(a)


# 2.生成器函数
# yield:使函数中断,并保存中断的状态
# 一次返回一个结果，在每个结果中间，挂起函数,方便下次从它离开的地方继续执行
# def jiuge():
#     print('----开始----')
#     yield '森森'
#     yield '悟'
#     yield '太阳'
#
# jiu = jiuge()   # 调用一个生成器函数
# print(jiu)    # 返回的是生成器对象
# 取值方式一:
# print(next(jiu))
# print(next(jiu))
# print(next(jiu))

# 取值方式二:
# for i in jiu:
#     print(i)


# 2.2  举例
# 处理文件，用户指定要查找的文件和内容

def check(fname, word):  # fname是文件名   word是查找的内容

    with open(fname, 'r+', encoding='utf-8') as f:
        for i in f:
            # print(i)  # 遍历出每行的内容
            if word in i:
                yield i

ch = check('jiuge.txt', '灰同学')

print(next(ch))
print(next(ch))
print(next(ch))


# 2.3 return 和 yield
#
# def funa():
#     yield 1
#     yield 2
#     # return '这是return'  # 如果return返回了值，这个值就是StopIteration异常的说明
#
# a = funa()
# print(next(a))
# print(next(a))
# print(a)


# def funb():
#     return 1
#     return 2  # 执行完第一句return后，函数结束
#
# print(funb())

# 总结：
# 相同点：都是返回函数执行的结果
# 不同点：return返回结果后结束函数的执行; yield让函数变成一个生成器，函数被冻结，唤醒后再产生一个值
