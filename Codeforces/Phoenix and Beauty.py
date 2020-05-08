for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    maxi=max(a)
    l=[]
    if maxi<k:
        maxi=k
    for i in range(k):
        l.append(maxi)
        maxi-=1
    l=l*n
    print(l)
    if k==2 and n==2:
        print(len(a))
        print(*a)
    # elif k==1:
    #     print(len(a))
    #     print(*a)
    else:
        flag=0
        for i in a:
            if i in l:  
                flag=1
            else:
                flag=0
                break

        if flag:
            print(len(l))
            print(*l)
        else:
            print(-1)

    incomplete