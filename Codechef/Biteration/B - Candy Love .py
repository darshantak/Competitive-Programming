n=int(input())
v=list(map(int,input().split()))
x=int(input())
y=1
canda=v[n-1]*x
temp=0
count=0
for i in range(n):
    temp=temp+v[i]
    if temp<canda:
        count+=1
    else: