n=int(input())
l=list(map(int,input().split()))
c=sorted(l.copy())
 
x=-1
for i in range(n):
    if l[i]!=c[i]:
        x=i
        break
y=-1
for i in range(n-1,-1,-1):
    if l[i]!=c[i]:
        y=i
        break
 
if x==-1 and y==-1:
    print('yes')
    print(1,1)
else:
    l[x:y+1]=reversed(l[x:y+1])
    flag=0
    print(x,y)
    print(l)
    for i,j in zip(l,c):
        if i!=j:
            print('no')
            flag=1
            break
    if flag==0:
        print('yes')