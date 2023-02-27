import random
print('猜拳游戏开始')
ply = 5
while ply > 3:
    yell = int(input('玩家请出拳：石头、剪刀、布==1、2、3、'))
    if yell > 3:
        print('请输入正确指令')
    else:
        if yell == 1:
            print('玩家出布')
        elif yell == 2:
            print('玩家出剪刀')
        elif yell == 3:
            print('玩家出石头')
        com = random.randint(1,3)
        if com == 1:
            print('电脑出布')
        elif com == 2:
            print('电脑出剪刀')
        elif com == 3:
            print('电脑出石头')
        if yell == 3 and com == 2 or yell == 2 and com == 1 or  yell == 1 and com == 3:
            print('玩家获胜')
        elif yell == com:
            print('平局')
        else:
            print('玩家失败')
