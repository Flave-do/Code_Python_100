
import re
# 1. 匹配开头结尾
# ^  开头
# 一是表示以什么开头； 二表示对什么取反
# 注意：^在[]中才表示不匹配
# res = re.match('^ab', 'abcd')

# [^ab]:表示匹配除了'a','b'的字符
# res = re.match('[^ab]*', 'jiugeabcd')
# res = re.match('[^ab]', '9abcd')
# print(res.group())

# $  结尾
# res = re.match('\w*e$', 'jiuge')  # 字符e结尾符合
# res = re.match('\w*t$', 'jiuge')    # # 字符t结尾符合
# print(res.group())



# 2. 匹配分组

# |	匹配左右任意一个表达式
# res = re.match('\d?\d$|100', '100')
# res = re.match('\d$', 'abc')
# res = re.match('\d$|\w*', 'abc')
# print(res.group())
# (ab)	将括号中字符作为一个分组
# res = re.match('\w{4,20}@163.com', 'test@163.com')
# res = re.match('\w{4,20}@(163|qq|129).com', 'test@178.com')
# print(res.group())


# \num	引用分组num匹配到的字符串
# res = re.match('<.*>', '<html>jiuge</html>')
# res = re.match(r'<(\w*)>.*</\1>', '<h2>jiuge</h2>')
# res = re.match(r'<(\w*)><(\w*)>.*</\2></\1>', '<html><h2>jiuge</h2></html>')
# print(res.group())


# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
# res = re.match(r'<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>', '<html><h2>jiuge</h2></html>')
# print(res.group())


