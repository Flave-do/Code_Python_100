# find(字符串,开始索引,结束索引)             查询
# rfind(字符串,开始索引,结束索引)            右侧查询
# index(字符串,开始索引,结束索引)             查询
# rindex(字符串,开始索引,结束索引)             右侧查询
# replace(原字符,新字符,替换数量)            替换
# expandtabs()                            \t替换空格

str1 = 'hello python, hello world'
print(str1.find('o'))             # 默认从0开始找，找到一个就满足了
print(str1.find('a',5,11))

print(str1.rfind('o'))            # 默认从右边开始找 找到一个就满足了

# index 就是找不到就发脾气 就报错，而find不会报错
str1 = '         jell     '
print(str1.expandtabs())



