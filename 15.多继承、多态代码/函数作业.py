
# 面向对象作业
# 1.属性：
# level    值为整型，表示生熟程度     5
# mat     值为字符串，表示生熟信息   半熟
# 2.方法:
# __init__：设置默认属性
# cook：烤红薯方法

# 课前先讲函数作业，有录播

# 函数作业
# 名片管理器  --- 增删改查(退出)
li = ['zs', 'ls']  # 存放名片的空列表

# print(li.index('zs'))
# li[0] = 'jiuge'
# print(li)

# 添加
def add():
    name = input('请输入你要添加的名字：')
    li.append(name)

# 查询
def get():
    print(li)

# 修改
def update():
    old_name = input('请输入你要修改的名字：')
    new_name = input('请输入你要修改后的名字：')
    # 找出旧名的下标
    n = li.index(old_name)
    # 根据下标去修改
    li[n] = new_name

# 删除
def delete():
    del_name = input('请输入你要删除的名字：')
    li.remove(del_name)

# 根据用户输入循环执行
while True:
    inp = int(input('1.添加  2.查询  3.修改  4.删除 5退出:'))
    if inp == 1:
        add()
    elif inp == 2:
        get()
    elif inp == 3:
        update()
    elif inp == 4:
        delete()
    elif inp == 5:
        break  # 退出循环

    else:
        print('输入不正确')





