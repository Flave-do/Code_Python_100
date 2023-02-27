
# 1.编码格式

# 如果写入的是中文，改变一下编码格式
# with open('jiuge.txt', 'w', encoding='utf-8') as f:
#     f.write('悟俊涛')
# #
# with open('jiuge.txt', 'r', encoding='utf-8') as f2:
#     print(f2.read())

# 2.读取操作
# readline :一次读取一行内容

# with open('jiuge.txt') as f:
#     while True:
#         text = f.readline()
#         if not text:  # 判断一下有没有读取完
#             break     # 如果读取完了就跳出循环
#
#         print(text)


# readlines: 按照行的方式一次性读取文件内容，返回是一个列表
# with open('jiuge.txt') as f:
#     con = f.readlines()
#     print(con)
    # print(type(con))

# for i in con:
#     print(i)

