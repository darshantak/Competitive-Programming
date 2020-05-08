n,m=map(int,input().split())
a,b=['']*m,['']*m
for i in range (0,m):
    a[i],b[i]=map(str,input().split())
p=[str(x) for x in input().split()]
for i in p:
    if i in a:
        x=a.index(i)
        if len(a[x])<=len(b[x]):
            print(a[x],end=' ')
        else:
            print(b[x], end=' ')
    else:
        x=b.index(i)
        if len(a[x])<=len(b[x]):
            print(a[x],end=' ')
        else:
            print(b[x], end=' ')
 