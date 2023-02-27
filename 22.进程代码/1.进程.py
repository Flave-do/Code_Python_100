
# 1.进程的状态
# 就绪态： 运行的条件都已经具备，正在等CPU执行
# 执行态：CPU正在执行其功能
# 等待态: 等待某些条件满足


# import time
# print('程序开始')  # 程序开始，运行状态
# name = input('请输入你的名字：')  # 用户输入，进入阻塞
#
# print(name)
#
# time.sleep(1)   # 睡眠1秒，阻塞状态
# print('程序结束')   # 运行状态


# 2.进程语法结构  multiprocessing 模块 Process类
# from multiprocessing import Process
# import os

# 2.1 Process 参数：
#     target: 子进程要执行的任务
#     args：以元组的方式传递参数
#     kwargs:以字典的方式传递参数
#     name: 子进程名称，可以不设定

# 2.2 属性：name:当前进程的别名   pid：当前进程的进程号

# os.getpid(): 获取当前进程的进程号
# os.getppid(): 父进程号
#
# def one():
#     print('这是任务一')
#     print(f'one子进程id:{os.getpid()}, 父进程id:{os.getppid()}')
#
# def two():
#     print('这是任务二')
#     print(f'two子进程id:{os.getpid()}, 父进程id:{os.getppid()}')
#
# if __name__ == '__main__':
#     # 创建子进程
#     # p1 = Process(target=one, name='酒鸽')  # 设置子进程名称
#     p1 = Process(target=one)
#     p2 = Process(target=two)
#
#     # 启动子进程
#     p1.start()
#     p2.start()
#
#     # p1.name = '九歌'
#     # print('p1的子进程名：', p1.name)
#
#     # print('one中的进程号：', p1.pid)
#     # 查看主进程的进程号
#     print('主进程的id:%s, 父进程的id:%s' % (os.getpid(), os.getppid()))

# 在cmd中查看进程命令：tasklist

# 2.3 常用方法
# start： 启动子进程
# is_alive: 判断子进程是否还活着， 存活返回True, 否则False
# join: 主进程等待子进程结束

# def sleep():
#     print('赶紧起来，别睡了')
#
# def play():
#     print('赶紧学习, 别玩了')
#
# if __name__ == '__main__':
#
#     p1 = Process(target=sleep)
#     p2 = Process(target=play)
#
#     p1.start()
#     p1.join()  # 主进程等待p1子进程结束
#     p2.start()
#     p2.join()
#
#     print('p1的状态是：', p1.is_alive())
#     print('p2的状态是：', p2.is_alive())


# 2.4 进程间不共享全局变量
from multiprocessing import Process
import time

# li = []
#
# # 写入数据
# def write():
#     for i in range(3):
#         li.append(i)
#         time.sleep(1)
#     print('这是write里面的li: ', li)
#
# # 读取数据
# def read():
#     print('这是read里面的li: ', li)
#
# if __name__ == '__main__':
#     p1 = Process(target=write)
#     p2 = Process(target=read)
#
#     p1.start()
#     p1.join()
#     p2.start()






