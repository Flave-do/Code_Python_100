# partition(字符串)            左侧切割成三组数据的元组
# rpartition(字符串)           右侧切割成三组数据的元组
# split(字符，切割数)           以指定字符串切割数据为列表
# splitlines()                 以换行符切割数据为列表
# join(字符串)                 对字符串进行占位连接
# +                            连接字符串
str1 = 'hello python, hello world'

print(str1.partition('o'))


print(str1.rpartition('o'))

print(str1.split('o',3))       # 前面找到三个o切掉，第四个保留
print(str1.split('o',4))        # 4个o分成五份

str1 = '❤'
print(str1.join('周周老师'))     # 周❤周❤老❤师
