
# 本周六因为九歌老师有事情，暂时不上课，后面会补上
# 20号左右基础班考试,现在开始复习，生成器的附加题可以不做
# 关于考试，会提前跟你们说，考试类型、时间

# 1.线程
# 1.1多任务：同一时间执行多个任务
# 多任务的执行方式：并发、并行
#
# 1.2 进程和线程
# 1.进程:打开一个程序至少就会有一个进程，是操作系统进行资源分配的基本单位
# 一个进程默认有一个线程，进程里面可以创建多个线程
#
# 2.线程：线程是CPU调度的基本单位，每个进程至少有一个线程，这个线程就是主线程;自己创建的是子线程

import time
# print(123)
# time.sleep(1)  # 睡眠, 以秒为单位
# print(456)

# 2.1单线程
# def drink():
#     print('喝红牛')
#     time.sleep(2)
#     print('抗疲劳')
#
# def eat():
#     print('吃烧烤')
#     time.sleep(2)
#     print('奥利给')
#
# drink()
# time.sleep(1)
# eat()

# 2.2多线程
# 线程模块：threading
# 线程类Thread 参数：
#     target:执行的目标任务名
#     args:以元组的形式给执行任务传参
#     kwargs:以字典的方式给执行任务传参
#
# 举例一：
# from threading import Thread  # 导入线程模块
#
# def drink():
#     print('喝红牛')
#     time.sleep(3)
#     print('抗疲劳')
#
# def eat():
#     print('吃烧烤')
#     time.sleep(3)
#     print('奥利给')
#
# if __name__ == '__main__':
#     # 1.创建子线程
#     # target：只需要告诉他函数名
#     t1 = Thread(target=drink)  # 任务名后面不要加小括号
#     t2 = Thread(target=eat)
#     # 2. 开启子线程  -- start方法
#     t1.start()
#     t2.start()

# 举例二：
# import threading
# def speak(name):
#     print(f'{name}在说话')
#     time.sleep(2)
#     print('哈哈哈')
#
# if __name__ == '__main__':
#     for i in range(4):
#         # 创建子线程， args传入参数,以元组的形式,只写一个参数需要后面加逗号
#         t1 = threading.Thread(target=speak, kwargs=({'name': 'zs'}))
#         t1.start()



