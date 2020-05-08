n=int(input())
m=list(map(int,input().split()))
x=[]
for i in range(1,n-1):
    if m[i+1]>m[i] and m[i-1]>m[i]:
        x.append(i)
if len(x)==0:
    print(*m)
elif len(x)==1:
    m[x[0]+1]=m[x[0]]
    print(*m)
else:
    