
# 1. 匹配变量名是否有效: 不能以数字开头
import re
# name_li = ['jiuge', '4jiuge', 'jiu', '_jiuge']
#
# for i in name_li:
#     # print(i)
#     res = re.match('\D+', i)  # \D匹配非数字  +:匹配前一个字符出现1次或者无限次
#     if res:
#         print('正确的变量名：', res.group())
#     else:
#         print('非法的变量名：', i)


# 2.高级用法
# 1.search()会扫描整个字符串并返回第一个成功匹配的字符串
# res = re.search('\d+', '九歌老师翻车翻了108次, 上课上了25次')
# print(res)
# print(res.group())

# match从开始位置匹配, search扫描整个字符串查找匹配

# 2.findall()以列表形式返回匹配到的字符串
# res = re.findall('\d+', '九歌老师翻车翻了108次, 上课上了25次, 开车开了361次')
# print(res)
# print(type(res))

# 总结：
# match     从头开始匹配       返回object    匹配一次   不常用
# search    仅返回第一个匹配    返回object    匹配一次   较常用
# findall   从头到尾匹配        返回列表      匹配所有   最常用


# 3.sub() 将匹配到的数据进行替换
# sub(正则表达式,新内容,字符串, 指定要替换的个数)
# res = re.sub('\d+', '43', '小希的尺码是42码, 太阳的尺码是40码, 木木的尺码是42码')
# res = re.sub('\d+', '43', '小希的尺码是42码, 太阳的尺码是40码, 木木的尺码是41码', 2)
# print(res)


# 4.split()根据匹配进行切割字符串，并返回一个列表
# split(正则表达式, 字符串)
# res = re.split(' ', 'a b; c 12')
# print(res)


# 5.贪婪与非贪婪
# 贪婪匹配：
# 			在满足匹配时，匹配尽可能长的字符串，默认情况下，采用贪婪匹配.
# 非贪婪匹配：
# 			在满足匹配时，匹配尽可能短的字符串，使用?来表示非贪婪匹配.
# 在*、+、{m,n}等后面加上？, 使贪婪变成非贪婪

# *: 最少0次，最多n次
# +：最少1次，最多n次
# ?: 最少0次，最多1次

# res = re.match('ab*', 'abbbc')  # abbb

# ?修饰的是前面的*, *最少是0次，b的0次没有值
# res = re.match('ab*?', 'abbbc')   # a
# ?修饰的是前面的+, +最少是1次，b的1次就是一个字符b
# res = re.match('ab+?', 'abbbc')   # ab
# print(res.group())


# res = re.match('a*', 'aaaa')  # aaaa
# res = re.match('a?', 'aaaa')    # a
# res = re.match('a*?', 'aaaa')    # a
# print(res.group())

# 6. 原生字符串
# python中字符串前面加上r表示原生字符串

# print('abc123')     # abc123
# print('abc\n123')
# print('abc\\n123')  # abc\n123
# print(r'abc\n123')  # abc\n123

# 如果需要匹配字符串中的"\", 在正则表达式需要4个反斜杠
# 因为在正则表达式中，'\\'表示一个反斜杠
# res = re.match('\\\\', '\def')

# res = re.match(r'\\', '\def')
# res = re.match(r'\\*', r'\\def')
res = re.match(r'\\\\', r'\\def')
print(res.group())







