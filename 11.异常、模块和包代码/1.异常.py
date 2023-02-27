# 1.异常：程序运行时发生错误的信号
# 2.异常信息解读：
# Traceback (most recent call last):   方便我们查找问题，错在哪里
# NameError : 异常类型
# name 'a' is not defined  ： 异常内容的具体信息

# 3. 异常处理
# 3.1 捕获异常一
# 最简单的语法格式：
# try:
    # 被检测的代码块
# except 异常类型：
#     编写尝试失败的代码

# print(a)

# try:
#     # print(123)
#     print(a)
# except:
#     print('error')


# try:
#     # print(123)
#     print(a)
# except NameError as e:
#     print(e)

# 捕获万能异常  Exception: 可以捕获任意异常
li = [1, 2, 3]
# try:
#     print(li[3])
# except Exception as e:
#     print(e)

# 多分支： 对不同的异常定制不同的处理逻辑
# try:
#     # print(li[3])
#     print(a)
# except NameError as n:
#     print('nameerror')
#
# except IndexError as i:
#     print('indexerror')

# 3.2 捕获异常二  else
# else 在if中，条件不满足时才执行
# 捕获异常中，else在没有异常时才会执行
# try:
#     # print('我们在学习异常处理')
#     print(a)
# except Exception:
#     print('出现错误')
# else:
#     print('没有捕获到异常')

# 3.3 捕获异常三 finally
# finally无论是否有异常，都会执行
# try:
#     print('我们在学习异常处理')
#     # print(a)
# except Exception:
#     print('出现错误')
# finally:
#     print('没有捕获到异常')

# 4.异常的传递
# 从产生异常的地方开始传递到调用异常的地方
# def funa():
#     inp = int(input('请输入整数:'))
#     return inp
#
# def funb():
#     print(funa())
#
# try:
#     funb()
# except Exception as e:
#     print(e)


# def test():
#     inp = int(input('请输入整数:'))
#     print(10/inp)
#
# def test2():
#     test()
#
# test2()

# try:
#     test2()
# except ValueError:
#     print('类型错误，输入不正确')
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print('运行成功')
# finally:
#     print('最后执行，结束')

# 5.抛出异常  raise
# 主动抛出异常：
# 1.创建一个Exception('xxx') 对象, xxx是异常提示信息
# 2. raise 抛出这个对象(异常对象)

# raise Exception('这是抛出一个异常')

# def test():
#     raise Exception('在函数中抛出异常')  # 异常被抛出后，下面的代码无法执行
#     print('这是test函数')
#
# test()

# def login():
#     pwd = input('请输入密码：')
#     if len(pwd) == 6:
#         return pwd
#     # 创建异常对象
#     ex = Exception('长度不符合')
#     # 抛出异常对象
#     raise ex
#
#
# # 捕获异常
# try:
#     print(login())
# except Exception as e:
#     print('错误：%s' % e)


