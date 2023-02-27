
# 老师不会一节课全部都教，有些可以自己下课研究
# 1. os模块 包含普遍的操作系统功能
import os
# 1.1  os.getenv()  读取环境变量
# print(os.getenv('path'))

# 1.2 os.path.split() 把路径分为两部分, 第一个是目录路径，第二个是文件名
# os.path.dirname() : split分割出的第一个元素
# os.path.basename() : split分割出的第二个元素

# print(os.path.split(r'D:\test10\26内置模块\2.内置模块.py'))
# print(os.path.dirname(r'D:\test10\26内置模块\2.内置模块.py'))
# print(os.path.basename(r'D:\test10\26内置模块\2.内置模块.py'))

# 1.3 os.path.exists()  判断路径是否存在， 存在返回True， 不存在返回False
# print(os.path.exists(r'D:\test10\26内置模块\2.内置模块.py'))  # True
# print(os.path.exists(r'D:\test10\26内置模块\3.内置模块.py'))  # False

# 1.4 os.path.isfile()   判断一个文件是否存在; 存在返回True， 不存在返回False
# os.path.isdir() 判断一个文件夹是否存在
# print(os.path.isfile(r'2.内置模块.py'))
# print(os.path.isdir(r'D:\test10\26内置模块'))

# 1.5   os.path.abspath(path)  返回path的绝对路径
# print(os.path.abspath('.'))  # 返回当前路径的绝对路径
# print(os.path.abspath('../'))  # 返回上一层路径的绝对路径


# 2. sys模块 负责程序跟python解释器的交互
import sys
# print(sys.path)  # 返回环境变量的路径
# print(sys.platform)  # 返回当前系统平台
# print(sys.version)  # 查看目前系统python的版本

# 3. time 模块 ：处理时间
import time
# 3.1 time.time() 时间戳
# print(time.time())

# 3.2 time.localtime()  将时间戳转换为当前时区的struct_time, 时间数组格式
# struct_time：结构化时间 ：包含了年月日时分秒的多元元组
# print(time.localtime())
# t1 = time.localtime()
# print(t1)
# print(t1[0])
# print(t1.tm_year)

# 3.3 time.asctime(): 把时间元组表示为 Sat Dec 19 21:25:19 2020
# print(time.asctime())


# 3.4  time.strftime(格式化字符串, struct_time对象) ：struct_time对象转成时间字符串, 使用字符串表示当地时间
# print(time.strftime('%Y-%m-%d', time.localtime()))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 3.5 time.strptime(时间字符串, 格式化字符串) :  将时间字符串转成struct_time对象
# stime = '2015-09-12 12:13:23'  # 时间字符串
# ftime = time.strptime(stime, '%Y-%m-%d %H:%M:%S')
# print(ftime)   # struct_time对象


# 4. 虚拟机

# 安装VMware -- VMware免费试用三十天,有序列号 --  打开虚拟机
# 1. 如果有其他虚拟机或者苹果电脑,可以不用下载群文件的ubuntu 18 !!!

# 2. 下载的同学，Ubuntu 18文件夹里面所有文件都要下载

# 3.现在用的是18版本, 有其他版本的也可以
# 用户名：sixstar   密码： 123

# 4. 如果打开显示..处于禁用状态，电脑虚拟化没有开启
# 解决办法：  知道自己的电脑型号， 找到进入BIOS的方法， 去里面开启虚拟化
# 举例： 联想电脑怎么开启虚拟化



# 5.考试
# 1.考试时间： 12月24号晚上7点半到10点          有特殊情况，私聊老师们
# 2.考试内容： 基础班知识    重点：数据类型、函数、面向对象
# 3.考试形式： 考题私聊九歌、瑶瑶、丸子老师, 发给你一个文档
# 4.考试题目： 单选、多选、代码题，总共25道
# 5.注意事项： 考卷统一发给九歌老师qq, 统一交py文件, 把答案写在一个py文件中, 名写上真名
# 6.考试的时候，QQ群会禁言。考完的同学，请不要泄题，还有其他同学没有考试
# 7.考试时，可以翻阅自己的笔记; 加上考勤分80分及格
# 8.请同学耐心等待，人数比较多，批改需要时间，到时候会尽快通知结果



