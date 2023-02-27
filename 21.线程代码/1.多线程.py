# 导入线程模块

from threading import Thread
import time
# 1. 多线程
# 线程模块：threading
# 线程类Thread 参数：
#     target:执行的目标任务名
#     args:以元组的形式给执行任务传参
#     kwargs:以字典的方式给执行任务传参


# def study(**kwargs):
#     print(f'{kwargs}在上课')
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     for i in range(4):   # 循环四次，创建多个子线程
#         # 创建子线程
#         t1 = Thread(target=study, kwargs={'name': 'zs'})  # 任务是study
#         # 启动子线程
#         t1.start()


# 2.多线程步骤
# 1.导入模块
# 2.创建子线程
# 3.守护线程 setDaemon
# 4.启动子线程 start
# 5.阻塞主线程 join

def funa():
    print('明月清风')
    time.sleep(2)
    print('今年不收礼')

def funb():
    print('信手斩龙')
    time.sleep(2)
    print('森思熟滤')

if __name__ == '__main__':
    # 1.创建子线程
    t1 = Thread(target=funa)
    t2 = Thread(target=funb)

    # 3.守护线程：主线程执行完了，子线程也跟着结束; 要放在start前面
    t1.setDaemon(True)
    t2.setDaemon(True)


    # 2.开启子线程
    t1.start()
    t2.start()

    # 4.阻塞主线程:有暂停的作用, 等添加了join的子线程执行完，主线程才能继续执行
    # 必须放在start后面; 加了join，守护线程功能还在，只是没有体现
    t1.join()
    t2.join()

    # 6.修改名字
    t1.setName('线程1')
    t2.setName('线程2')

    # 5.获取名字
    print(t1.getName())
    print(t2.getName())

    print('旺仔思思森森, 这是主线程')
