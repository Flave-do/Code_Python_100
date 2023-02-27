
import copy

# 1.浅拷贝:会创建新对象，其内容并不原对象的引用，而是原对象第一层的引用
a = [1, 2, [3, 4, 5]]  # 嵌套列表
b = copy.copy(a)
# print('修改前：', a, b)
# print(id(a), id(b))        # 父对象的id不同
# print(id(a[2]), id(b[2]))  # 子对象的id一样

# a.append('a')
# print('修改后：', a, b)
# 把a列表里面的内层列表中的元素3---zs
# a[2][0] = 'zs'
# print(a)
# print(b)

# 浅拷贝：a,b父对象是一个独立的对象，但是子对象指向同一引用。修改子对象的数据，会一起变化。
# 浅拷贝只拷贝第一层，深层次的数据改变会影响其他


# 2.深拷贝  a,b父对象是一个独立的对象，子对象也独立。
# a = [1, 2, [3, 4]]
# b = copy.deepcopy(a)
# print(id(a), id(b))   # 父对象的id不同
# print(id(a[2]), id(b[2]))  # 子对象的id不同

# a.append('a')
# print('修改父对象：', a, b)
#
# b[2].append('b')
# print('修改子对象：', a, b)

# 深拷贝：完全拷贝, 数据变化只影响自己本身。拷贝出来的对象是一个全新的对象


# 3.可变不可变
# 不可变类型：  int /float/str/tuple
# 变量对应的值，他的数据不能被修改，如果修改就会分配新的内存空间
# a = 5
# print(a)
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# st = 'abc'
# print(id(st))
# st2 = st+'we'
# print(id(st2))
# 元组是不可变类型中特殊的一种，
# tu = (1, 2, 3)
# print(id(tu))
# tu2 = (1, 2, 3)
# print(id(tu2))

# 可变类型： list/dict/set
# 变量对应的值，他的数据是可以被修改的，但是内存地址保持不变

# li = [1, 2, 3]
# print(id(li))
# li.append('a')
# print(li)
# print(id(li))

# stu = {'name': 'zs', 'age': 20}
# print(id(stu))
# stu['age'] = 18
# print(id(stu))


# 4. 补充
# 4.1 reduce()  对参数序列中元素进行累积
# reduce(函数, 对象)   # 函数：有两个参数的函数


# from functools import reduce  # 一定要先导入模块
#
# def func(x, y):
#     return x**y
#
# res = reduce(func, [1, 2, 3])
# print(res)


# 拆包
# 元组拆包
# tu = (1, 2, 3, 4, 5)
# a, b, c = tu
# print(a, b, c)

# print(*tu)  # 使用* 拆包
#
# a, *b, c = tu
# print(a, b, c)
# d, e, f = b
# print(d, e, f)

