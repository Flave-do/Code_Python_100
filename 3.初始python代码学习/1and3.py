f = open('C:\\Users\\Administrator\\Desktop\\python_work\\课后作业\\1.txt',mode='w',encoding='utf-8')
d = open('C:\\Users\\Administrator\\Desktop\\python_work\\课后作业\\hello.txt',mode='w')

# print(list(f))
f.writelines('小胖次')
f.writelines('是白色的')
f.write('哈哈哈')
f.close()

d.writelines('xiao pang ci')
d.writelines(' ha ha ha')
d.close()

#
# # f.close()
# import os
# print(os.getcwd())      # 当前默认运行路径
#
# print(os.path.getsize('.\\课后作业\\1.txt'))        # 显示当前文件的字节数
#
# print(os.listdir('.\\课后作业'))        # 显示当前文件夹的所有文件列表

print()
print()

f = open('C:\\Users\\Administrator\\Desktop\\python_work\\课后作业\\1.txt',mode='r',encoding='utf-8')
d = open('C:\\Users\\Administrator\\Desktop\\python_work\\课后作业\\hello.txt',mode='r')

print(f.read())
print(d.read())
f.close()
d.close()




