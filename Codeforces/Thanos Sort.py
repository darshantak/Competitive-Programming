def search(s):
    x=[0,]
    for i in range(len(s)-1):
        if s[i+1]<s[i]:
            x.append(i)
    x.append(len(s)-1)
    fin=0
    #print(x)
    for i in range(len(x)-1):
        temp=x[i+1]-x[i]
        if temp>fin:
            fin=temp
    return fin
n=int(input())
s=list(map(int,input().split()))
l=sorted(s)
r=sorted(s,reverse=True)
if s==l:
    print(n)
elif s==r:
    print(1)
else:
    l=s[0:n//2]
    r=s[n//2:n]
    fin1=search(l)
    fin2=search(r)
    print(max(fin1,fin2))