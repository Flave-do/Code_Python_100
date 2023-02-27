
# 正则表达式是一个强大的字符串处理工具

# 1.正则用法：
import re  #  直接导入模块即可

# match方法：从字符串的开始位置匹配正则表达式，返回match对象
# 如果起始位置没有匹配成功，返回None

# re.match(正则表达式, 要匹配的字符串)

# group方法：如果匹配到数据的话，可以使用group方法来提取数据

# 2.举例：
# res = re.match('sixstar', 'sixstar')
# print(res)  # 返回match对象
# print(res.group())  # 没有匹配到,会显示：'NoneType' object has no attribute 'group'


# 3.匹配单个字符
# .	匹配任意1个字符(除了\n之外)
# res = re.match('.', '信手斩龙')
# print(res.group())

# [ ]	匹配[ ]中列举的字符
# [0-35-68-9] 不匹配数字4和7
# res = re.match('[0-9][123456789][0-35-68-9][信手]', '456信手斩龙')
# res2 = re.match('[a-z][a-zA-Z]', 'aBcd')

# print(res.group())
# print(res2.group())

# \d	匹配数字: 0,1,2,3,4,5,6,7,8,9
# res = re.match('\d\d', '23#')


# \D	匹配非数字, 既不是数字
# res = re.match('\D', '#是23#')


# \s	匹配空白, 即 空格 和 tab 键
# \S	匹配非空白
# res = re.match('\s\s\S', '  #是23#')
# print(res)

# \w	匹配单词字符, 即a-z,A-Z,0-9,_ ,中文
# \W	匹配非单词字符
# res = re.match('\w', '_AlphaZHUQILayman')
# res = re.match('\w', '权志龙')
# print(res)
# print(res.group())

