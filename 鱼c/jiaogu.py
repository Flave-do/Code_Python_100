# # i = 3
# # while i > 0 :
# #     user = input('请输入用户名')
# #     password = input('请输入密码')
# #     if user == 'zs' and password == 123 or user == 'ls' and password == 456:
# #         print('登录成功')
# #         break
# #     else:
# #         print('用户名或密码错误')
# #         i -= 1
#
#
#
#
#
#
# # class Exam(object):
# #     # 记录第一个被创建对象的引用 -- 类属性
# #     ins = None
# #     def __new__(cls, *args, **kwargs):
# #         # 1.判断类属性是否为空
# #
# #         if cls.ins == None:
# #             # 2.类属性为空，调用父类方法，为第一个对象分配空间
# #             cls.ins = super().__new__(cls)
# #             # super().__new__(cls)   继承父类object里面的new方法，然后进行重写
# #
# #         # 3.返回类属性保存的对象引用
# #         return cls.ins
# #
# # # 每次实例化所创建的实例对象都是同一个(内存地址都是一样的)
# # # 每次实例化都会去调用new方法
# # print('未实例化前：', Exam.ins)
# # exam = Exam()    # 第一次实例化
# # print('第一次实例化后：', Exam.ins)
# # print('第一次实例化的对象', exam)
# # exam2 = Exam()  # 第二次实例化
# # print('第二次实例化后：', Exam.ins)
# # print('第二次实例化的对象', exam2)
# #
# # # print(id(exam))
# # # print(id(exam2))
#
#
#
#
# class rectangle(object):
#     def area(self,long,wide):
#         self.long = long
#         self.wide = wide
#         print('面积为',self.long*self.wide)
#
# A = rectangle()
#
# print(A.area())


#
# class rectangle(object):
#
#     def area(self):
#         self.long = int(input('请输入长'))
#         self.wide = int(input('请输入宽'))
#         return self.long * self.wide
#
# A = rectangle()
# print('面积为',A.area())

# # print((1, 2, '1', '2')[0] > 1)
#
# f = open('lyric.txt','w')
# f.write('奇妙的事无法用言语说尽, 桌上留的文字你最后聆听。感受到的每口呼吸我都珍惜，冰箱的牛奶我只留给你。')
# f.close()
#
# file = open('lyric.txt', 'r')
# content = file.read()
# file.close()
# name = input('请输入文件名：') # 新的文件名
# file2 = open(name, 'w')
# file2.write(content)
# file2.close()

import re
time = 'abc 2020-12-24 2020-12-25'
res = re.compile(r'\d{4}-\d{2}-\d{2}')
res.findall('abc 2020-12-24 2020-12-25')
print(res.findall('abc 2020-12-24 2020-12-25'))