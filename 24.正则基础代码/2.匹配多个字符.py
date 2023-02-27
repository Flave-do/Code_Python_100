
import re
# 1.*	匹配前一个字符出现0次或者无限次,即可有可无
# res = re.match('\d*', '123sixstar')
# * 可以是0次,  \D*没有匹配到不会报错，是空字符串
# res = re.match('\D*', '123sixstar')
# print(res)


# 2. +	匹配前一个字符出现1次或者无限次，即至少有1次
# res = re.match('\d+', '123sixstar')
# 至少得1次，\D+ 没有匹配到会报错
# res = re.match('\D+', '123sixstar')

# 3.  ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# res = re.match('[1-9]?\d', '6789')
# [1-9]?  匹配不出数据，不会报错，因为最少是0次
# res = re.match('[1-9]?', '06789')
# res = re.match('[1-9]?\d', '06789')
# res = re.match('[1-9]?', '6789')
# print(res)
# print(res.group())

# 4.{m}	匹配前一个字符出现m次
# res = re.match('\w{4}', 'abc123_ert')
# print(res.group())

# 5.{m,n}	匹配前一个字符出现从m到n次
# 最少是m次，最多是n次
# res = re.match('\w{4, 6}', 'abc123_ert') # 里面需要是英文符号
# res = re.match('\w{4,6}', 'abcertyu')
# print(res.group())