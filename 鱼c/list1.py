
#def size(list1) :
 #   i=0
  #  dict = list1[i]
   # a = dict['age']
  #  i  += 1
  #  print(a)

#  print(sorted(list1.items()))

'''
方法一：
list1 = [{"age":12}, {"age":18}, {"age":-1}]
i = len(list1)   #取出列表长度
j = 0
list2 = []       #空列表，稍后有用

while j < i :
    for value in list1[j].values() : #将字典的键逐个取出来
        list2.append(value)                 #将值储存到列表中方便比较大小
    j += 1
while len(list2) >= 1 :
    num1 = max(list2)          #找出最大的值
    position = list2.index(num1)          #取出最大值在的位置
    print(list1[position],end=' ')       #输出最大值
    if len(list2) != 1 : print('>',end=' ')  #方便好看输出比较符
    list2.pop(position)          #弹出最大值


'''


list1 = [{"age":12}, {"age":18}, {"age":-1}]
list1.sort(key = lambda x : x['age'],reverse = True)
print(list1)










