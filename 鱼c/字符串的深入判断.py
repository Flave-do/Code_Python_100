
str1 = 'hello,武汉加油,hello,周黑鸭加油'

# 判断字母是否为大写
print(str1.isupper())

# 判断是否所有字母都为小写
print(str1.islower())       # 只判断字母,空格不属于字母

# 判断是否都是字母
print(str1.isalpha())

# 判断是否由字母或数字组成
print(str1.isalnum())

# 判断是否都为数字
print(str1.isdigit())       # 判断出来中文归于字母

# 判断首字母是否大写
print(str1.istitle())

print(str1.startswith('hello'))   # 是否以指定字符串开始


print(str1.endswith('周黑鸭'))     # 是否以指定字符串结尾


print(str1.index('加'))          # 默认从0开始寻找，找到就停止，默认找到最后

print(str1.index('加',9,))




























