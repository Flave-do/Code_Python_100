
# 1.可迭代对象 Iterable
# for 临时变量 in 可迭代对象
# 数据类型：int str list tuple dict set
# 能被for循环取值：除了int都可以
# 迭代：对这些数据使用for循环语法从其中依次取出值来进行使用，这样的过程称为遍历，也叫迭代
#
# 可迭代对象: 泛指一类对象，满足以下条件的对象可以成为可迭代对象
# 1>.对象实现了__iter__方法
# 2>.__iter__方法返回了一个迭代器对象

# li = ['执念', '田扬', '十笙', '森森', '伊凡']
#
# for i in li:
#     print(i)

# 2.for 循环工作原理：
# 1> 在内部对可迭代对象调用__iter__方法，获取到迭代器对象
# 2> 再一次次的通过迭代器对象调用__next__方法获取迭代结果
#
# 3. 如何判断一个对象是否可以迭代: isinstance()
# from collections.abc import Iterable
#
# print(isinstance(100, Iterable))     # False
# print(isinstance({1, 2}, Iterable))  # True










