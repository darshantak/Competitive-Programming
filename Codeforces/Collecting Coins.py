for i in range(int(input())):
    a,b,c,n=map(int,input().split())
    flag=0
    temp=a+b+c+n
    if temp%3!=0:
        flag=0
    else:
        x=(temp//3)-a
        y=(temp//3)-b
        z=(temp//3)-c
        # print(x,y,z)
        if x>=0 and y>=0 and z>=0:
            flag=1
    if flag:
        print("YES")
    else:
        print("NO")    