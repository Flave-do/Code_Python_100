
# 1.多态：同一种事物的多种形态
# +: 同个加号可以用于不同的对象，体现了多态的功能
# print(1+2)
# print('he'+'llo')

# len()  计算长度   传入不同的参数，计算出不同的长度
# li = [1, 2, 3]
# print(len(li))
# print(len('python'))

# 多态 -- 对象所属的类之间有继承关系
# class Pay:           # 支付类
#     def pay(self, money):
#         print(f'支付了{money}')
#
# class Wechat(Pay):      # 微信支付
#     def pay(self, money):
#         print(f'使用微信支付了{money}')
#
# class Alipay(Pay):           # 支付宝支付
#     def pay(self, money):
#         print(f'使用支付宝支付了{money}')
#
# # py = Wechat()
# py = Alipay()
# py.pay(300)

# 举例一：
# class Animal:    # 动物类
#     def run(self):
#         print('动物都会走')
#
# class People(Animal):
#     def run(self):
#         print('人在走')
#
# class Pig(Animal):
#     def run(self):
#         print('猪在走')
#
# class Dog(Animal):
#     def run(self):
#         print('狗在走')
#
# class Cat(Animal):
#     pass
#
# pe = People()
# pig = Pig()
# dog = Dog()
#
# # 不同的对象调用同样的方法，做不同的事情
# pe.run()
# pig.run()
# dog.run()

# 举例二：
class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'{self.name}在跑来跑去')


class Black(Dog):
    def play(self):
        print(f'{self.name}在啃拖鞋')

class Person:
    def __init__(self, pname):
        self.pname = pname

    def plays(self, dog):  # dog = xiaohei
        print(f'{self.pname}和{dog.name}在玩耍')  # dog.name是狗狗的名字


# 创建狗对象
xiaohei = Black('小黑')
we = Black('小白')
ke = Black('柯基')
# xiaohei.play()

# 创建人对象
zs = Person('张三')
# 代码执行的时候，传入不同的狗对象，就会产生不同的执行效果
zs.plays(xiaohei)
zs.plays(we)
zs.plays(ke)