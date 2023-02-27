
# 好记性不如烂笔头
# 1.文件操作
# 文本文件：使用文本编辑软件查看

# 二进制文件：提供给其他软件使用，不能使用文本编辑软件查看

# 2. 操作文件
# 1.打开文件
# 2.读、写文件
# 3.关闭文件

# 3.open(filename, mode)函数，创建一个文件对象
# 3.1open()函数默认以只读方式打开文件
# filename：文件的路径   mode：打开的方式

# 3.2 三个方法
# read :读取
# write: 写入
# close:关闭


# 3.3 文件对象的属性
# file.closed: 如果文件已关闭，返回True
# file.mode: 返回被打开文件的访问模式
# file.name: 返回文件的名称
# 1.打开文件
# f = open('we.txt')  # open函数创建一个文件对象，把这个文件对象赋值给了f
# # 2.读取文件内容
# print(f.read())
# # 3.关闭文件
# f.close()

# print('文件名：', f.name)
# print('访问模式：', f.mode)
# print('是否关闭：', f.closed)


# 4.访问模式
# 4.1  关于其他
# file = open('D:\\test10\\16单例模式\\旺仔.txt')
# file = open('D:/test10/16单例模式/旺仔.txt')
# print(file.read())  # 读取所有内容

# read(num): num表示从文件中读取数据的长度，如果没有传值，就表示读取所有
# print('第一次:', file.read(5))
# print('第二次:', file.read())
# file.close()

# 4.2 跟异常一起使用
# f = open('we.txt')
# try:
#     print(f.read())
# finally:
#     f.close()

# 4.3 r w r+ w+
# r:默认只读，文件必须存在
# w:默认只写, 不存在就创建，存在就删除文件内容
# +: 表示可以同时读写某个文件
# r+：可读写, 文件不存在抛出异常
# w+: 先写再读,会清空文件中的所有内容

# f = open('ss.txt', 'w+')
# f.write('Alpha456')
# f.seek(0, 0)
# print('第一次：', f.read())
# f.close()

# 4.4  文件指针
# 1.文件指针标记从哪个位置开始读取数据
# 2.第一次打开文件的时候，通常文件指针指向文件的开始位置
# 3.执行了read方法，文件指针会移动到读取内容的末尾

# tell()方法 ：查看文件的当前位置
# seek()方法： 改变当前文件的位置
# seek(offset, from)
# offset 表示要移动的字节数, from指定开始移动字节的参考位置
# 如果from为0, 将文件开头作为参考位置
# 如果from为1, 将当前位置作为参考位置
# 如果from为2, 将文件末尾作为参考位置

# f = open('we.txt', 'r+')
# print('第一次读取：', f.read(5))
# # 查看当前位置
# pos = f.tell()
# print('当前文件位置:', pos)
# # 把光标重新定位到文件开头
# f.seek(0, 0)
#
# print('第二次读取：', f.read())
# f.close()

# 4.5  文件复制举例
# file = open('ss.txt', 'r')
# content = file.read()
# file.close()

# name = input('请输入文件名：') # 新的文件名
# # 把内容放进新文件里面
# file2 = open(name, 'w')
# file2.write(content)
# file2.close()

# 4.6  with  :with关键字, 离开with代码块的时候，系统会自动调用close方法

# with open('wu.txt', 'r') as f:
#     print(f.read())

# print(f.closed)  # 会自动关闭文件






