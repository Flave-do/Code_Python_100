

# 1. gevent模块
# 自动切换任务，在gevent中用到的主要模式是greenlet; gevent遇到IO操作，会自动进行切换，属于主动式切换。


# 2.gevent使用

# 下载gevent模块
# 安装库/模块命令  -- pip install 模块名    (pip install  gevent)


# 2.1 gevent.spawn()   创建一个协程对象
# spawn() 第一个参数是函数名, 后面的参数是传值

# 2.2 join:等待、阻塞、直到某个协程执行完毕
# 2.3 joinall: 这个方法的参数是一个协程对象列表，会等待所有的协程都执行完毕后再退出



# 3.gevent举例

# 3.1 如果没有遇到能识别的IO操作，不会进行任务切换
#   IO：指的是输入输出 input output, 比如说网络等待、文件操作等

# 3.2 gevent模块中自带了sleep耗时函数,当使用了sleep时，
# CPU会跳转到另一个就绪的程序,达到人工设置让其自动切换的功能


# import gevent
#
# def write():
#     print('开始写代码')
#     gevent.sleep(1)   #  gevent.sleep(1)模拟的是gevent可以识别的io操作
#     print('明月清风写完了')
#
#
# def drive():
#     print('森森开车了')
#     gevent.sleep(3)
#     print('Open cat')
#
# def eat():
#     print('吃烧烤')
#     print('吃火锅')
#
#
# # 创建协程对象
# g1 = gevent.spawn(write)
# g2 = gevent.spawn(drive)
# g3 = gevent.spawn(eat)
#
# g1.join()  # 等待g1结束
# g2.join()  # 等待g2结束
# g3.join()  # 等待g3结束


# 3.3 joinall: 这个方法的参数是一个协程对象列表，会等待所有的协程都执行完毕后再退出

# def work(name):
#     for i in range(3):
#         print(f'函数名:{name}, i的值:{i}')
#
#
# gevent.joinall([
#     gevent.spawn(work, '旺仔'),
#     gevent.spawn(work, '森森')
# ])

# 3.4 综合举例
# import gevent
#
# def boy():
#     print('男生：打个电话：')        # 1
#     gevent.sleep(2)
#     print('男生：咦, 为什么挂电话,接着打...')  # 5
#
#
#
# def girl():
#     print('女生：主人来电话啦...')   # 2
#     gevent.sleep(3)
#     print('女生：主人那家伙又来电话啦...')   # 6
#
#
# def content():
#     print('今天吃饭没')  # 3
#     gevent.sleep(1)
#     print('多喝热水')    # 4
#
#
# gevent.joinall([
#     gevent.spawn(boy),
#     gevent.spawn(girl),
#     gevent.spawn(content)
# ])

# 协程遇到IO操作，会自动进行切换
#
# 3.5 给程序打补丁
# 如果需要用到time.sleep(), 需要打一个补丁

# from gevent import monkey  # 导入模块
# import gevent
# import time
#
# # 该语句必须放在前面
# monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的代码
#
# def work(ne):
#     for i in range(3):
#         print('函数名:%s' % ne)
#         time.sleep(1)
#
# gevent.joinall([
#     gevent.spawn(work, 'ts'),
#     gevent.spawn(work, 'we')
# ])


# 3.6 简单总结
# 1.线程是CPU的调度的单位，进程是资源分配的单位
# 2.一个程序至少有一个进程，一个进行至少有一个线程
# 3.进程切换任务资源比较大，效率很低
# 线程切换任务资源一般，效率一般
# 协程切换任务资源很小，效率较高
