
# 1. 讲作业
# 2.内置模块
# 3.安装虚拟机、考试要求

# 1.烤红薯作业
# 烧烤时间：level
# 烧烤状态：0-3 生的   4-6半熟  7-9熟了  10以上 烤糊了

# level： 数字表示生熟程度
# mat: 字符串表示生熟

# __init__：初始化属性
# cook： 烤制方法

# 代码：

# class Jiuge(object):  # 烤酒鸽
#     def __init__(self, level):
#         self.level = level
#         self.mat = '生的'
#
#     def cook(self):
#         if 0 <= self.level <= 3:
#             self.mat ='生的'
#         elif 4 <= self.level <= 6:
#             self.mat = '半熟'
#         elif 7 <= self.level <= 9:
#             self.mat = '熟了'
#         elif self.level >= 10:
#             self.mat = '烤糊了'
#         else:
#             print('出错了')
#
#
#     def add(self, ment=1):
#         if ment == 1:
#             print(f'酒鸽烤了{self.level}分钟,不想加酱料')
#         else:
#             print(f'酒鸽烤了{self.level}分钟, {self.mat},添加的酱料是{ment}')
#
#
# jiu = Jiuge(7)
# jiu.cook()
# jiu.add()


# 2.文件操作作业
# with open('test.txt', 'w+') as f:
#     f.write('hello python')
#     f.seek(0, 0)
#     print(f.read())
















