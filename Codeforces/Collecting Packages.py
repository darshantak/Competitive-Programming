for _ in range(int(input())):
    n=int(input())
    l=[]
    l.append([0,0])
    for i in range(n):
        temp=list(map(int,input().split()))
        l.append(temp)
    # print(l)
    l.sort(key=lambda x: [x[0],x[1]])
    # print(l)
    fin=""                                                                                                                 
    for i in range(len(l)-1):
        flag=0
        a=l[i+1][0]-l[i][0]
        b=l[i+1][1]-l[i][1]
        if a>=0 and b>=0:
            fin=fin+'R'*a+'U'*b
            flag=1
        else:
            flag=0
            break
    if flag:
        print("YES")
        print(fin)
    else:
        print("NO")