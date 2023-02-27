
# 1.递归函数： 自己调自己
# 递归函数特性：
#   1.要有明确的结束条件
#   2.进入更深一层的递归时，问题规模会比上次递归有所减少
#   3.相邻两次重复之间有紧密的联系

# 计算累积和
def funa(n):
    s = 0
    for i in range(1, n+1):
        s += i
    print(s)

# funa(7)

# 递归函数  : 1+2+...+7    递归深度是有限制的，默认是1000
# def funb(a):  # a = 7 --- a = 6
#     # 在a值为1的时候，不去调用
#     if a == 1:  # 设置一个结束条件
#         return 1
#
#     # 每调用一次自身，相当于复制一份该函数
#     return a + funb(a-1)  # return 7 + funb(6)  ---   return 7+ 6 + funb(5)
#
# print(funb(4))

# 斐波那契数列： 1  1 2 3 5 8 13 21
# 从第三个数开始， 结果是前两个数之和

def func(n): # n = 3 -- n = 2/ n=1
    if n <= 1:
        return n

    return func(n-1) + func(n-2)  # func(2) + func(1) -- func(1)+func(0)+func(0)+func(-1)

print(func(3))  # 代表数列第几项的结果

# for i in range(1, 10):
#     print(func(i))




