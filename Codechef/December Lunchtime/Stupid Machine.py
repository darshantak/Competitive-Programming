def exe(n):
    m=min(n)
    count=m*len(n)
    ind=n.index(m)
    for i in range(len(n),ind+1):
        n[i]-=m
    return count
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    temp=0
    c=0
    while s[0]!=0:
        if 0 in s:
            i=s.index(0)
            s=s[0:i]
            c=exe(s)
            temp+=c
        else:
            c=exe(s)
            temp+=c
    print(temp)
    
    
    
