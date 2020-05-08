for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    temp=[]
    count=0
    y=0
    for j in b:
        
        i=0
        if j in temp:
            count+=1
            x=temp.index(j)
            temp.pop(x)
            y=len(temp)
            continue
        while len(a)!=0:        
            if a[i]==j:
                count=count+(2*(y)+1)
                a.pop(i)
                break
            else:
                y+=1
                temp.append(a[i])
                a.pop(i)
                i=0
            # print(y)
        # print(temp)
        # print(a)
        # print(count)
    print(count)
            