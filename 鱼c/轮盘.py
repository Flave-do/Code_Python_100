'''
round1 = range(0,10)
round1_ = []

for i in round1:
    i/=10             #对数据逐个处理
    round1_.append(i)
round1 = round1_





print(round1)

'''

import random

j = 0
first_prize = 0
second_prize = 0
third_prize = 0

while j < 1000 :
    i_ = random.sample(range(0,10), 1)
    i = i_[0]
    if 0.9 <= i / 10 < 1 :      #如果取值在0.9到1之间
        first_prize += 1
    elif 0.6 <= i / 10 < 0.9 :      #如果取值在0.6到0.9之间
        second_prize += 1
    elif 0 <= i / 10 < 0.6 :      #如果取值在0到0.6之间
        third_prize += 1
    j += 1
print('一等奖人数为：',first_prize)
print('二等奖人数为：',second_prize)
print('三等奖人数为：',third_prize)



























