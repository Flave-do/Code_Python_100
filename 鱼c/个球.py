import random


red_ball = ['红球','红球','红球','红球']      # 将球存储到盒子中
white_ball = ['白球','白球']
blue_ball = ['蓝球']

boxes = [[],[],[]]        # 准备一个嵌套列表代表三个球盒子（同类型用列表）


for box in boxes:         # 取三个红球分别放进每一个盒子，保证每一个盒子有球
    box.append(red_ball.pop())
    # 去掉注释符可验证：
    # print(box)

balls = red_ball+white_ball+blue_ball       # 把剩下的球全部放一起


for ball in balls:
    box_index = random.randint(0,len(boxes)-1)       # len=3，0->2的随机数模拟三个盒子，即参数位置
    boxes[box_index].append(ball)                    # 将球分别放进三个盒子
i = 1
for ball2 in boxes:

    print("盒子",i,"的球有" ,len(ball2),"个")
    i +=1
    for ball in ball2:
        print(ball)

























