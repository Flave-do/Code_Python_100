
import random
ball=["红","红","红","黄","黄","黄","绿","绿","绿","绿","绿","绿"]
i =random.sample(range(0, 11), 8)
for j in i:
    print(ball[j],end=" " )