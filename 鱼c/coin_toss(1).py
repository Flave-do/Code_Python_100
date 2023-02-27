import random

counts = int(input("请输入抛硬币的次数："))
i = 0
j = 0
k = 0
continuously_j = 0
continuously_k = 0
b = 0
c = 0
jm = 0
km = 0
print("开始抛硬币实验：")

while i < counts:
    num = random.randint(1, 2)

    if  counts < 100:

        if num % 2:
            j +=1
            print("正面", end=" ")
            if continuously_j + 1 == i :
               b += 1
               continuously_j +=1
               if jm < b :
                   jm = b
               else:
                   jm = jm

            else:
                b = 1
                continuously_j =i
        else:
            k +=1
            print("反面", end=" ")
            if continuously_k +1== i:
                c +=1
                continuously_k +=1
                if km < c:
                    km = c
                else:
                    km=km
            else:
                c = 1
                continuously_k = i
        i +=1

    else:
        if num % 2:
            j +=1
            if continuously_j + 1 == i :
               b += 1
               continuously_j +=1
               if jm < b :
                   jm = b
               else:
                   jm = jm

            else:
                b = 1
                continuously_j =i
        else:
            k +=1
            if continuously_k +1== i:
                c +=1
                continuously_k +=1
                if km < c:
                    km = c
                else:
                    km=km
            else:
                c = 1
                continuously_k = i
        i +=1

print( )
print("一共模拟了",counts,"次抛硬币，结果如下：")
print("正面:",j,"次")
print("反面：",k,"次")
print("最多连续正面：",jm,"次")
print("最多连续反面：",km,"次")