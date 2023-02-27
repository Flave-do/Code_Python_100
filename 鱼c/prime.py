k = 2

while k <= 10 :
    i = 1
    a = 0
    while i <= 10 :
        j = 1
        while j < i :
            j +=1
            if i*j == k :
                print(i*j,"=",i,"*",j,)
                a=1
        i += 1
    if a == 0 :
        print(k,"是一个质数",sep=" ")

    k +=1


