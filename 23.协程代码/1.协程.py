#
# 1.协程
# 对于协程来说，程序员就是上帝, 想让谁执行到哪里，他就执行到哪里
#
# 简单实现协程  -- yield
# import time
#
# def work1():
#     while True:
#         yield 1
#         time.sleep(1)
#
# def work2():
#     while True:
#         yield 2
#         time.sleep(1)
#
# w1 = work1()
# w2 = work2()
# while True:
#     print(next(w2))
#     print(next(w1))


# 2. greenlet
# 是一个用C实现的协程模块，通过设置switch()可以实现任意函数之间的切换，这种切换属于手动切换。
#
# 切记： 不用用第三方模块、内置模块名作为自己的py文件命名！！！
#
# 2.1 下载greenlet模块
# 安装库/模块命令  -- pip install 模块名
# 1. 进入命令提示符 --  输入 pip install greenlet
# 2. 在pycharm编辑器下方 ---  点击Terminal(终端) -- 输入 pip install greenlet
# 3. pip list      查看已经安装的库、模块
# 4. python -m pip install --upgrade pip   更新pip版本
# 'pip' 不是内部或外部命令，也不是可运行的程序  ---  检查一下解释器配置/修改一下环境变量


# 2.2 使用greenlet实现任务切换
# from greenlet import greenlet
#
# def study():
#     print('需要下载模块')
#     g2.switch()
#     print('下载完成')
#     g2.switch()
#
# def play():
#     print('趣味运动会')
#     g1.switch()
#     print('跑完了')
#
# # 实例化一个协程  :   greenlet(目标函数), 函数后面没有小括号
# g1 = greenlet(study)
# g2 = greenlet(play)
#
# # switch() 切换执行
# g1.switch()      # 切换到g1中运行
# # g2.switch()    # 切换到g2中运行




