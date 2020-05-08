for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    first=a[0]
    s=sum(a[1:])
    temp=m-first
    if s>=temp:
        print(m)
    else:
        print(s+first)
        