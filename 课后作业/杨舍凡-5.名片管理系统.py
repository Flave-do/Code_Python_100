# ———------————名片管理系统————--------————-

st = '欢迎使用名片管理系统'
welcom = st.center(30,'*')
print(welcom)
print('⚠⚠⚠⚠⚠⚠注意事项：小本经营，乱输入代码可是会报错的哦  账号308726757   初始密码qsw')

names = ['花花','黑夜','夏奥黑','顺拐','2狗子']
admin = '308726757'
cipher = 'qsw'

# if do_it == '登陆':

def adminr():
  global cipher
  cipher = input('请输入新密码')
  print('😊😊😊管理员密码修改成功，重启后生效😊😊😊')

while True:
  et = input('-----1、登录 ☆☆☆☆☆ 2、退出------')
  if et == '1':

    user = input('请输入管理员账号')
    code = input('请输入管理员密码')

    if user == admin and code == cipher:
      print('--------登陆成功--------')
      input('请按任意键进行下一步')
      while True:
        print('😀😀😀当前为主菜单😀😀😀')
        do_it = input('😏请牢记操作指令：添加、删除、修改、查找, esc：返回上级  退出：退出登录  密码：修改密码')


        def growa(a):  # 增加名片

          if a not in names:
            names.append(a)
            print('太简单啦，添加成功')
            input('请按任意键返回主菜单')
          elif a in names:
            b = input('这个人貌似已经被你加进来了，同胞兄弟输入Y、取消请输入N')
            if b == 'Y':
              names.append(a)
              print('大兄弟，添加成功')
              input('请按任意键进行下一步')
            else:
              print('已取消该骚操作')
              input('请按任意键进行下一步')


        def dell():  # 删除名片

          while True:
            a = input('1、按索引删除  2、按内容删除')
            if a == '1':
              b = input('请输入要删除的名片索引值：')
              if b.isdigit() is True:
                b = int(b)
                print('名片：', names[b], '索引位置：')
                c = input('请确认您要删除此名片: Y/N')
                if c == 'Y':
                  names.remove(names[b])
                  print('删除成功，欢迎下次光临')
                  input('请按任意键进行下一步')
                else:
                  print('那就取消咯')
                  dell()
              else:
                input('😡😡数字!数字！请按任意键返回')

            elif a == '2':
              b = input('请输入想要删除的名片信息')
              if b in names:
                print('名片：', b, '索引位置：', names.index(b))
                c = input('请确认您要删除此名片: Y/N')
                if c == 'Y':
                  names.remove(b)
                  print('删除成功，欢迎下次光临')
                else:
                  print('已取消操作，请重新输入')
                  dell()
              else:
                print('抱歉，没找到您要删的名片⚠⚠⚠')
                print('TPS:别急，您可以重新输入一次看，或者输入esc返回观摩一下名单！')
                input('请按任意键进行下一步')

            elif a == 'esc':
              break


        # ------------按索引值修改删除懒得做了，纯逻辑代码一点都不优雅-------
        def findas():  # 查看或查找名片

          while True:
            a = input('请输入数字：1、按位置查找  2、全局预览（管理员才有权限哦）')
            if a.isdigit() is True:
              a = int(a)

              if a == '1':
                b = input('请输入您要查看的名片索引：')
                if b.isdigit() is True:
                  b = int(b)

                  print(names[b])
                  input('请按任意键进行下一步')
                else:
                  input('😡😡数字！请按任意键返回')

              elif a == '2':
                print('当前名片系统总览：', names)
                input('请按任意键进行下一步')

            else:
              break


        def modify():  # 修改名片

          i = input('请选择修改方式   1：直接修改    2：按索引修改')

          if i.isdigit() is True:
            i = int(i)
            if i == 1:
              a = input('请输入要修改的名片')
              if a in names:
                c = names.index(a)
                print('name', a, '索引', c)
                b = input('请确认您修改的名片Y/N')
                if b == 'Y':
                  d = input('修改为：')
                  names[c] = d
                  print('修改成功', names[c])
                  input('请按任意键进行下一步')
                else:
                  modify()

              else:
                print('抱歉，您要找的名片已经不在了')
                print('TPS:别急，您可以重新试试看，或者观摩一下名单！')
                input('请按任意键返回主页')
            # -------------害，妥协了还是随便写了个----------------
            elif i == 2:
              a = input('请输入要修改的索引位置')
              if a.isdigit() is True:
                a = int(a)
                if a <= len(names) - 1:
                  print('name', names[a], '索引', a)
                  b = input('请确认您修改的名片Y/N')
                  if b == 'Y':
                    d = input('修改为：')
                    names[a] = d
                    print('修改成功', names[a])
                    input('请按任意键进行下一步')
                  else:
                    modify()
                else:
                  input('我这名单好像没你说的那么长，按任意键继续')
                  modify()
              else:
                input('😏小兔崽子，数字数字！请按任意键返回！')
          else:
            input('😏小兔崽子，数字数字！请按任意键返回！')

          # elif a == 'esc':
          #   break


        if do_it == '退出':
          break


        elif do_it == '修改':
          modify()


        elif do_it == '查找':
          findas()


        elif do_it == '添加':
          a = input('请输入要添加的名片')
          growa(a)


        elif do_it == '删除':
          dell()

        elif do_it == '密码':
          adminr()

    else:
      input('账号或密码输入错误，请按任意键返回！')

  else:
    break
print('谢谢使用，程序已结束')


