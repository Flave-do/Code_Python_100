
# 1. 进程间的通信 -- Queue

# q.put(): 放入数据
# q.get(): 取出数据
# q.empty(): 如果队列为空，返回True, 否则False
# q.qsize(): 返回当前队列包含的消息数量
# q.full(): 如果队列满了,返回True, 否则False


from queue import Queue
# 初始化一个Queue对象
# q = Queue(4)  # 里面有参数，代表最多接收三条信息； 没有参数, 没有大小限制
# q.put('a')
# q.put('b')
# q.put('c')
#
# print('判断队列是否满了：', q.full())

# 取出数据
# print(q.get())
# print(q.get())
# print(q.get())

# print(q.empty())
# print('现在的消息数量：', q.qsize())


# 2.进程操作队列

# from multiprocessing import Process, Queue
#
# name = ['旺仔', '森森', '木木', '思思']
#
# # 将名牌放入盒子中
# def write(q1):  # q1是形参, 代表初始化的Queue对象
#     for i in name:
#         print(f'将{i}放入盒子中')
#         q1.put(i)
#
#
#
# # 读取盒子里面的名牌
# def read(q2):
#     while True:
#         if q2.empty():
#             break
#         else:
#             print('我们从盒子中看到：', q2.get())
#
#
# if __name__ == '__main__':
#     # 创建Queue对象
#     que = Queue()
#     p1 = Process(target=write, args=(que, ))
#     p2 = Process(target=read, args=(que, ))
#
#     p1.start()
#     p1.join()
#     p2.start()


# 3.进程池
# 概念：定义一个池子, 在里面放上固定数量的进程，有需求来了，就拿一个池中的进程来处理任务；
# 等到处理完毕，进程并不关闭，而是将进程再放回进程池中继续等待任务

# apply_async: 异步非阻塞, 不用等待当前进程执行完毕，随机根据系统调度来进行进程切换
# 用法：主进程需要使用join, 用get收集结果

from multiprocessing import Pool
import time

def study(a):  # a是形参
    print('我们在学习')
    time.sleep(2)
    return a  # 这个是老师给你们演示的代码


if __name__ == '__main__':
    # 定义一个进程池, 最大进程数是3
    p = Pool(3)
    li = []
    for i in range(6):  # range(6) 是0  1  2  3  4  5
        # apply_async(执行的任务, 传递给任务的参数)
        res = p.apply_async(study, args=(i, ))  # 根据进程池中的进程数, 每次最多3个子进程在执行
        # res中保存的是任务执行后的结果，也就是study中返回的值
        li.append(res)


    # 关闭进程池
    p.close()
    p.join()

    # apply_async 用get来收集结果
    for i in li:
        print(i.get())









