
# 1. run方法
# from threading import Thread
# import time

# 线程类：
# class MyThread(Thread):  # 需要继承Thread类
#
#     # 重构run方法, 规定是run这个名字, 表示线程活动的方法
#     def run(self):
#         print('耗子尾汁')
#         time.sleep(2)
#         print('头大如我')
#
# if __name__ == '__main__':
#     # 创建一个线程实例
#     my = MyThread()
#     # 启动线程   start会调用run方法
#     my.start()

# 2.线程之间执行是无序的
# import threading
# import time
#
# def work():
#     time.sleep(1)
#     # current_thread()是线程模块的内置方法，返回当前的线程对象
#     print('当前线程：', threading.current_thread().name)  # 打印一下当前执行的线程名
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         # 创建子线程
#         s1 = threading.Thread(target=work)
#         s1.start()

# 3.多线程资源共享
# 举例一：
# li = []  # 空列表
#
# # 写数据
# def write():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.1)
#     print('写入的数据：', li)
#
#
# # 读数据
# def read():
#     print('读取的数据：', li)
#
# if __name__ == '__main__':
#     # 创建写入数据的子线程
#     w1 = Thread(target=write)
#     # 创建读取数据的子线程
#     r1 = Thread(target=read)
#     w1.start()
#     w1.join()  # 阻塞，等w1执行完
#     r1.start()
#
# 举例二  : 资源竞争
#
# a = 0
# b = 1000000
#
# # 循环一次给全局变量a+1
# def jia():
#     for i in range(b):
#         global a  # 声明全局变量
#         a += 1
#     print('第一次：', a)
#
#
# def jia2():
#     for i in range(b):
#         global a  # 声明全局变量
#         a += 1
#     print('第二次：', a)
#
# if __name__ == '__main__':
#     # 创建两个线程
#     t1 = Thread(target=jia)
#     t2 = Thread(target=jia2)
#
#     t1.start()
#     t1.join()  # 主线程等待第一个子线程执行完代码再继续执行
#     t2.start()




# 4. 资源竞争解决办法
#
# 同步：
#     有两个线程， 线程A和线程B, A是用来写入的，B是读取A的值; A要先写入数据，B才能读取这些数据。
#     线程A和B之间就是一种同步关系
#
# 线程同步的方式：线程等待(join) 、 互斥锁
# 互斥锁：能够保证多个线程访问共享数据不会出现数据错误的问题
# 对共享的数据进行锁定, 保证同一时刻只能有一个线程去操作
#
# 互斥锁使用：
#     1.导入Lock
#     2.创建全局互斥锁
#     3.acquire(加锁)和release(解锁)方法之间的代码同一时刻只能由一个线程去操作

from threading import Thread, Lock

a = 0
b = 1000000

# 1.创建全局互斥锁
lock = Lock()

# 循环一次给全局变量a+1
def jia():
    lock.acquire()    # 2.加锁
    for i in range(b):
        global a  # 声明全局变量
        a += 1
    print('第一次：', a)
    lock.release()   # 3.解锁


def jia2():
    lock.acquire()
    for i in range(b):
        global a  # 声明全局变量
        a += 1
    print('第二次：', a)
    lock.release()

if __name__ == '__main__':
    # 创建两个线程
    t1 = Thread(target=jia)
    t2 = Thread(target=jia2)

    t1.start()

    t2.start()

# 总结:
#     1.acquire() 和release() 这两个方法必须成对出现
#     2.使用互斥锁，确保某段关键代码只能由一个线程从头到尾执行
#     3.使用互斥锁会影响代码的执行效率，多任务变成了单任务执行
#     4.互斥锁如果没有使用好容易出现死锁的情况
#
# 死锁：
#     1.一直等待对方释放锁的情况就是死锁
#     2.会造成应用程序停止响应, 不能再处理其他任务了
#     3.使用互斥锁的时候,注意死锁的问题，在合适的地方释放锁

# 大概是20几号考试, 之前知识点遗漏或者忘记的同学，赶紧复习
# 关于考试形式、考试时间等内容，先不要急着去了解！
# 进程、协程、正则内容比较多，一定要去预习

