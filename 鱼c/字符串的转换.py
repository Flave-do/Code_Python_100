# lower()             可转换字符转成小写
# upper()               大写
# title()               单词首字母转大写其他转小写
# swapcase()             字符串中大小写互换
# capitalize()            字符串首字母转大写，其余转小写

str1 = 'Hello,武汉加油,Python,周黑鸭加油'
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.swapcase())
print(str1.capitalize())

# 格式转换
# strip()           去掉字符串左右两侧的指定占位符
# lstrip              去掉字符串左侧的指定占位符
# rstrip              去掉字符串右侧的指定占位符
#
#
# ljust(长度,占位符)              左边占位符在右侧补占位符
# rjust(长度,占位符)                右侧占位符在左侧补占位符
# center(长度,占位符)               两侧补占位符

str1 = '*****hello,武汉加油*****'
print(str1.strip('*'))
print(str1.lstrip('*'))     # left  左
print(str1.rstrip('*'))     # right 右

str1 = 'hello,武汉加油'
print(len(str1))

# left 原有字符串左移
print(str1.ljust(15,'*'))        # 15为变换后的长度

# right 原有字符串右移
print(str1.rjust(15,'*'))


print(str1.center(15,'*'))        # 5个 两个半 优先左边给一个 左右左右左


