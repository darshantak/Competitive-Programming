for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split(" ")))
    x.sort(reverse=True)
    temp=2048
    flag=0
    if temp in x:
        flag=1
    else:
        for i in range(n):
            if temp>0:
                temp=temp-x[i]
            elif temp<0:
                temp=temp+x[i]
            if temp==0:
                flag=1
                break
    if flag==0:
        print("NO")
    else:
        print("YES")