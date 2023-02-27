
# 1.类型转换
# n = int(input('请输入你的号码：'))
# print(type(n))

# st = 'abcd'
# print(st)
# st2 = list(st)
# print(st2)
# print(type(st2))

# 1.1  str() 转为字符串
# a = 100
# print(type(a))
# b = str(a)
# print(b)
# print(type(b))

# 1.2 repr() 返回一个对象的str格式
# a = 123
# b = repr(a)
# print(b)
# print(type(b))

# 1.3 eval() 来执行一个字符串表达式，返回表达式的值
# print(1+1)
# print('1+1')
# c = eval('1+1')
# c = eval("'1+1'")  # 去掉外面一层引号
# print(c)
# print(type(c))

# li = '[1, 2, 3]'
# li = "{'name': 'zs'}"
# print(type(li))
# print(type(eval(li)))

# 1.4  tuple() 把对象转换成元组
# 字符串、元组、列表三者可以互转
li = [1, 2, 3]
# li = 'abcd'       # 字符串
# print(li)
# li2 = tuple(li)   # 把字符串转换成元组
# print(li2)
# print(type(li2))   # 查看转换后的类型---元组
#
# li3 = list(li2)   # 把元组转换成列表
# print(li3)
# print(type(li3))   # 查看转换后的类型---列表

# dict() 函数 把对象转为字典
# dic = {'name': 'zs', 'age': 20}
# 字典---字符串
# dic2 = str(dic)
# print(type(dic2))

# 字典---元组
# dic3 = tuple(dic)  # 键名转换成元组
# dic3 = tuple(dic.values())  # 字典的值转换成元组
# print(dic3)

# 字典---列表
# dic4 = list(dic)
# print(dic4)

# 列表转字典 (列表中的元素是元组类型)
# list2 = [('name', 'zs'), ('age', 20)]
# print(list2)
# print(type(list2))
# list3 = dict(list2)
# print(list3)
# print(type(list3))


# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# print(dict(zip(a, b)))

