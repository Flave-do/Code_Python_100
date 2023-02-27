# ———------————名片管理系统————--------————-

print('******************欢迎使用名片管理系统******************')

names=['小胖次','黑夜','罗布罗','2狗子','狗蛋']

def inpt(sex):                 # 判断输入是否为数字
  a = input(sex)
  if a.isdigit():
    return a
  else:
    print('🤯小兔崽子这是选择题！')
    input('please:按回车键返回')
    return 0

def indexes(a):             # 按索引查找名片
  if -len(names) < a <= len(names)-1 :
    print('当前索引位置:',a,'     名片:',names[a],sep='')
    input('按回车键继续！')
    return a,names[a]
  
  else:
    print('你溢出了知不知道，膨胀😠😠')
    return 0,0

def price(a):               # 按名片查找索引
  if a in names:
    print('当前值为:',a,'索引为:',names.index(a))
    return a,names.index(a)
  else:
    print('名片不存在！请重新输入！')
    return 0,0

def find_name(sex):
  print("请输入",sex,"方式",sep='')
  x = inpt('[1] 按索引   [2] 按名片')
  if x == '1':
    s = int(inpt('请输入索引值:'))
    a,b = indexes(s)              # 返回名片，索引
    
  elif x == '2':
    s = input('请输入名片：')
    a,b = price(s)                #返回名片，索引
    
  else :
    print('搞事情是吧，🐻🐻')
    input('请按回车键返回上一层：')
    return 0,0

  return a,b

while True:
  print('''基础指令: 
  查找、修改、删除、增加、
  ⚠⚠退出:退出程序          ''')
#  print('''基础指令: 查找、修改、删除、增加、
# ⚠⚠退出:退出程序             ⚠⚠返回:返回上一级''')
  to_do = input('请输入您的指令')
  if to_do == '退出' or to_do == 'tuichu':
    print('程序结束，谢谢使用！😄😄😄')
    break

  elif to_do == '修改' :
    a,b = find_name(to_do)
#    print(type(find_name(to_do)))
    if (a,b) == (0,0):
      input('🦊你怕是个捣乱分子，请按回车键返回！')
      continue

    else:
      polish = input('修改为：')
      names[a] = polish
      print('修改成功',names[a])

  elif to_do == '查找':
    a = inpt('[1]🧭定向查找        [2]全局预览（管理员）')
    if a == '1':
      find_name(to_do)
    elif a == '2':
      print('当前名单列表为',names)
      input('请按任意键返回！')
    else:
      print('😠小捣蛋你是不是又没按要求做！')
      input('🔥🔥🔥按回车返回上一层！')

  elif to_do == '删除' :
    a,b = find_name(to_do)
    if (a,b) == (0,0):
      print('严重怀疑你到底是不是来砸场子的！😠😠')
    else:
      print('索引:',a,'名片',b)
      input('⚠️⚠️⚠️请确认您要删除该对象，可能删除了就没对象咯')
      names.remove(b)
      input('删除成功！👏👏👏    请按回车键返回')

  elif to_do == '增加':
    a = input('请输入您🤏要加入的名片:')
    names.append(a)
    print(a,'添加成功！👍👍👍')
    input('请输入回车键返回～')

  else :
    print('请输入  🙆‍正确🙆‍️指令！')
    input('🔥请按回车键返回🔙')
